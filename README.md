# 🛠️ How to Run Locally
1. Clone the Repository
Bash
git clone https://github.com/satish942/ResumeJobDescriptionMatcher.git
cd ResumeJobDescriptionMatcher
2. Set Up Virtual Environment (Recommended)
Bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Run the Application
Bash
streamlit run app.py
🔑 Getting a Gemini API Key
To use the app, you need a Google Gemini API key:

Go to Google AI Studio.

Sign in with your Google account.

Click "Get API key" and create a new key.

Paste the key into the sidebar of the Streamlit app when prompted.

🌐 Deployment to Streamlit Community Cloud
Commit & Push: Ensure app.py, requirements.txt, and README.md are pushed to your GitHub repo.

Connect: Go to share.streamlit.io and sign in with your GitHub account (satish942).

New App: Click "Create app" > "Yup, I have an app".

Configure: * Repository: satish942/ResumeJobDescriptionMatcher

Main file path: app.py

Deploy: Click Deploy! Your app will be live at the URL provided.
## screen shots 

<img width="952" height="563" alt="image" src="https://github.com/user-attachments/assets/1a1f658a-8e25-474f-bb38-b9b7d61353f8" />

<img width="959" height="562" alt="image" src="https://github.com/user-attachments/assets/a9547d1a-4ede-4ad8-9c67-b092d8c2d339" />

<img width="956" height="565" alt="image" src="https://github.com/user-attachments/assets/04ed8ea7-529b-45eb-9379-c5930c2ad27d" />

## Stream lit cloud deployment steps : [https://resume-job-description-match.streamlit.app/]
Connect and Deploy
Go to share.streamlit.io.

Sign in with GitHub: Since you're currently having access issues, click Sign Out first, then sign back in using your satish942 GitHub account.

Click the "Create app" button in the top right.

Select "Yup, I have an app".

Fill in the deployment details:

Repository: Select satish942/your-repo-name.

Branch: Usually main or master.

Main file path: app.py (or whatever your main file is named).

(Optional) Click Advanced settings if you need to:

Set the Python version (defaults to 3.12+).

Add Secrets (like API keys or database credentials) that would normally be in a .env file.

Click Deploy!


<img width="953" height="502" alt="image" src="https://github.com/user-attachments/assets/57701873-2ce4-42d1-91e0-29ccbd5e3465" />



3. Go to [share.streamlit.io](https://share.streamlit.io/).
4. Sign in with your GitHub account.
5. Click **New app**.
6. Select your repository, branch (usually `main`), and the main file path (`app.py`).
7. Click **Deploy!**
Your app will be live on the internet shortly.
