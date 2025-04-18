
# 💼 AI Resume Analyzer + Job Matcher (Gemini-Powered)

A professional Streamlit web application that helps job seekers analyze their resumes against job descriptions using Google Gemini AI, identify skill gaps, and generate personalized cover letters — all in a beautiful dark-themed UI.

---

## 🚀 Features

### ✅ Resume-JD Match Analysis
- Upload your PDF resume and paste a job description
- Extracts content and calculates semantic **similarity score**
- Assigns a grade (A+ to C) based on relevance

### 🧠 Gemini AI Resume Suggestions
- Analyzes your resume and JD to generate **targeted improvements**
- Feedback on formatting, skills, projects, keywords, and more
- Displayed in an elegant, formatted panel

### 📝 Cover Letter Generator
- AI generates a **personalized cover letter** tailored to the JD
- Includes achievements, enthusiasm, and resume highlights
- Download as `.txt` and integrate into your application

### 📊 Skill Gap Analyzer (IIT Hackathon Level)
- Compares skills in resume vs required job description
- Outputs ✅ matched and ❌ missing skills
- Future updates: add links to courses (e.g., Coursera)

### 🖼️ Resume PDF Preview
- Preview the uploaded resume (browser-permitting)
- Fallback: download option available for browsers that block inline PDF

---

## 📦 Project Structure

```
📁 resume-analyzer/
├── app.py                   ← Streamlit app (one file version)
├── ai_suggester.py          ← Handles Gemini suggestions + cover letter
├── resume_parser.py         ← Extracts text from PDF resumes
├── job_matcher.py           ← Uses NLP to calculate similarity score
├── components/
│   └── skill_gap_analyzer.py← Extracts & compares skills with JD
├── data/resumes/            ← Stores uploaded resumes
├── .env                     ← API key (GEMINI_API_KEY)
└── requirements.txt         ← Dependencies
```

---

## 📌 Installation

### 🧰 Requirements

- Python 3.9+
- Google Gemini API Key (Get from: https://makersuite.google.com/app)
- Chrome/Firefox (recommended)

### 🔧 Setup

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Add your API key to .env
echo "GEMINI_API_KEY=your-api-key-here" > .env

# Run the app
streamlit run app.py
```

---

## 🌐 Deployment

You can deploy this app easily to:
- [Hugging Face Spaces](https://huggingface.co/spaces)
- [Streamlit Community Cloud](https://share.streamlit.io)
- [Render](https://render.com)

Ensure your `.env` is configured via secrets or environment variables in production.

---

## 👨‍💻 Author

**Rajat Gupta**  
🚀 Portfolio: [rajat-gupta-portfolio.netlify.app](https://rajat-gupta-portfolio.netlify.app)  
📧 Contact: available on portfolio

---

## 📜 License

This project is licensed under the MIT License.

---

> “The resume is your story — let AI help you tell it the best way possible.”
