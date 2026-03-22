import streamlit as st
import google.generativeai as genai
import os
import json
import PyPDF2
from docx import Document

# Streamlit App Configuration
st.set_page_config(page_title="Resume vs Job Description Matcher", page_icon="📝", layout="wide")

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return None

# Function to extract text from DOCX
def extract_text_from_docx(uploaded_file):
    try:
        doc = Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        st.error(f"Error reading DOCX: {e}")
        return None

# Function to extract text from TXT
def extract_text_from_txt(uploaded_file):
    try:
        return uploaded_file.getvalue().decode("utf-8")
    except Exception as e:
        st.error(f"Error reading TXT: {e}")
        return None

# Function to get Gemini Response
def get_gemini_response(prompt, api_key):
    try:
        genai.configure(api_key=api_key)
        # Using gemini-1.5-flash which is fast and good for this task
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error communicating with Gemini API: {e}")
        return None

st.title("📄 AI Resume vs Job Description Matcher")
st.markdown("Upload your resume and paste the job description to see how well you match!")

# Sidebar for API Key
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key_input = st.text_input("Enter your Google Gemini API Key", type="password")
    st.markdown("Get an API key from [Google AI Studio](https://aistudio.google.com/)")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Your Resume")
    uploaded_resume = st.file_uploader("Upload Resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
    
    resume_text = ""
    if uploaded_resume is not None:
        file_extension = uploaded_resume.name.split(".")[-1].lower()
        if file_extension == "pdf":
            resume_text = extract_text_from_pdf(uploaded_resume)
        elif file_extension == "docx":
            resume_text = extract_text_from_docx(uploaded_resume)
        elif file_extension == "txt":
            resume_text = extract_text_from_txt(uploaded_resume)
        
        if resume_text:
            st.success("Resume uploaded and parsed successfully!")
            with st.expander("Show extracted resume text"):
                st.write(resume_text)

with col2:
    st.subheader("2. Job Description")
    job_description = st.text_area("Paste the job description here", height=250)

st.markdown("---")

if st.button("🔍 Analyze Match", type="primary"):
    if not api_key_input:
        st.warning("Please enter your Gemini API Key in the sidebar.")
    elif not resume_text:
        st.warning("Please upload a valid resume.")
    elif not job_description.strip():
        st.warning("Please paste a job description.")
    else:
        with st.spinner("Analyzing resume against job description using AI..."):
            prompt = f"""
            You are an expert Applicant Tracking System (ATS) and Technical Recruiter.
            Evaluate the following resume against the provided job description.
            
            Provide your response strictly in valid JSON format with the following keys:
            - "match_percentage": An integer between 0 and 100 representing the match score.
            - "matched_skills": A list of strings of the technical and soft skills that match.
            - "missing_skills": A list of strings of the skills required by the job description but missing from the resume.
            - "improvement_advice": A short paragraph advising the candidate on how to improve their resume for this specific role.
            
            Job Description:
            {job_description}
            
            Resume:
            {resume_text}
            
            Response must be ONLY a valid JSON object.
            """
            
            response_text = get_gemini_response(prompt, api_key_input)
            
            if response_text:
                try:
                    # Clean the response in case the model wraps it in markdown blocks
                    cleaned_response = response_text.replace("```json", "").replace("```", "").strip()
                    result = json.loads(cleaned_response)
                    
                    st.subheader("📊 Analysis Results")
                    
                    # Display match percentage using a progress bar and metric
                    match_score = result.get("match_percentage", 0)
                    st.metric(label="Match Percentage", value=f"{match_score}%")
                    st.progress(match_score / 100)
                    
                    res_col1, res_col2 = st.columns(2)
                    
                    with res_col1:
                        st.subheader("✅ Matched Skills")
                        matched_skills = result.get("matched_skills", [])
                        if matched_skills:
                            for skill in matched_skills:
                                st.markdown(f"- {skill}")
                        else:
                            st.write("No matching skills found.")
                            
                    with res_col2:
                        st.subheader("❌ Missing Skills")
                        missing_skills = result.get("missing_skills", [])
                        if missing_skills:
                            for skill in missing_skills:
                                st.markdown(f"- {skill}")
                        else:
                            st.write("No missing skills found!")
                            
                    st.subheader("💡 Improvement Advice")
                    st.info(result.get("improvement_advice", "No advice provided."))
                    
                except json.JSONDecodeError:
                    st.error("Error parsing the AI response. Please try again.")
                    with st.expander("Show raw AI response"):
                        st.write(response_text)
                        
# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with Streamlit & Google Gemini API</p>", unsafe_allow_html=True)
