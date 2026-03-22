# AI Resume vs Job Description Matcher

This is a Streamlit web application that uses Google's Gemini AI to evaluate a resume against a job description. It provides a match percentage, identifies matching and missing skills, and gives actionable advice for improvement.

## Features
- **Upload Resume**: Supports PDF, DOCX, and TXT files.
- **Job Description**: Paste the target job description.
- **AI Analysis**: Uses the Google Gemini API to compare the texts and extract insights.
- **Results**: 
  - Match percentage
  - Matched skills
  - Missing skills
  - Improvement advice

## How to Run Locally

1. **Clone the repository** (if you've pushed it to GitHub):
   ```bash
   git clone <your-github-repo-url>
   cd ResumeJobDescriptionMatcher
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

## Getting a Gemini API Key
To use the app, you need a Google Gemini API key. 
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. Click "Get API key" and create a new key.
4. Paste it into the sidebar of the Streamlit app.

## How to Deploy to Streamlit Community Cloud

1. Commit all your code (`app.py`, `requirements.txt`, `.gitignore`, `README.md`) and push it to a new public repository on GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io/).
3. Sign in with your GitHub account.
4. Click **New app**.
5. Select your repository, branch (usually `main`), and the main file path (`app.py`).
6. Click **Deploy!**
Your app will be live on the internet shortly.
