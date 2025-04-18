import streamlit as st
import os
import re
import base64
from resume_parser import extract_resume_text
from job_matcher import get_similarity
from ai_suggester import suggest_resume_improvements
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# Dark Theme Styling
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        background-color: #0e1117;
        color: #f0f6fc;
    }
    .stTextInput > div > div > input,
    .stTextArea > div > textarea {
        background-color: #161b22;
        color: #c9d1d9;
    }
    .stDownloadButton button {
        background-color: #238636;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1 style="text-align: center; color: #58a6ff;">📄 AI Resume Analyzer + Job Matcher</h1>
    <p style="text-align: center; font-size: 18px;">Upload your resume and compare it with your dream job description using Gemini-powered AI ✨</p>
    <hr style="border-top: 2px solid #30363d;">
""", unsafe_allow_html=True)

# Sidebar Input
with st.sidebar:
    st.header("📤 Upload & Input")
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    job_desc = st.text_area("Paste Job Description", height=300)
    st.markdown("---")
    st.info("Need help? Paste a job post from LinkedIn, Indeed, etc.")

# Main Logic
if uploaded_file and job_desc:
    os.makedirs("data/resumes", exist_ok=True)
    save_path = os.path.join("data", "resumes", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())

    # PDF Preview
    st.markdown("### 🖼️ Resume Preview")
    base64_pdf = base64.b64encode(open(save_path, "rb").read()).decode('utf-8')
    st.markdown(f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600"></iframe>', unsafe_allow_html=True)

    # Resume Analysis
    with st.spinner("🔍 Extracting resume text..."):
        resume_text = extract_resume_text(save_path)

    with st.spinner("📊 Calculating similarity score..."):
        score = get_similarity(resume_text, job_desc)

    # Grading Function
    def get_grade(score):
        if score >= 90:
            return "A+"
        elif score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        else:
            return "C"

    grade = get_grade(score)
    st.markdown("## 📈 Resume vs JD Match Score")
    col1, col2 = st.columns(2)
    col1.metric(label="Similarity Score", value=f"{score:.2f}%", delta="Ideal: 85%+")
    col2.metric(label="Resume Grade", value=grade)

    if score < 85:
        with st.spinner("🤖 Asking Gemini for smart suggestions..."):
            suggestions = suggest_resume_improvements(resume_text, job_desc)

        # Format suggestions to HTML
        st.markdown("## ✨ Gemini's Smart Suggestions")
        formatted = suggestions
        formatted = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", formatted)
        formatted = formatted.replace("\n* ", "\n<li>").replace("\n• ", "\n<li>")
        sections = formatted.split("\n\n")
        formatted_html = ""
        for section in sections:
            if "<li>" in section:
                formatted_html += f"<ul style='margin-bottom: 16px;'>{section}</ul>"
            else:
                formatted_html += f"<p style='margin-bottom: 16px;'>{section}</p>"

        st.markdown(
            f"""
            <div style='background-color: #161b22; padding: 25px 30px; border-radius: 10px;
                        box-shadow: 0 2px 10px rgba(0,0,0,0.5); font-size: 16px; line-height: 1.6;
                        color: #c9d1d9;'>
                {formatted_html}
            </div>
            """, unsafe_allow_html=True
        )

        st.download_button("📥 Download Suggestions", suggestions, "resume_suggestions.txt")

        # Cover Letter Generator
        st.markdown("## 📝 AI-Generated Cover Letter")
        if st.button("Generate Cover Letter ✨"):
            with st.spinner("Crafting a personalized cover letter..."):
                cover_letter_prompt = f"""
You are a professional resume and cover letter writer.

Given the resume and job description below, generate a personalized and professional cover letter tailored for the role.
Keep it concise, enthusiastic, and include 2-3 achievements or project highlights from the resume.

Resume:
{resume_text}

Job Description:
{job_desc}

Cover Letter:
"""
                cover_letter = suggest_resume_improvements(resume_text, cover_letter_prompt)

            formatted_cover = cover_letter.replace("\n", "<br>")
            st.markdown(
                f"""
                <div style='background-color: #1e1e1e; padding: 20px; border-radius: 10px;
                            box-shadow: 0 2px 8px rgba(0,0,0,0.3); color: #f0f0f0; font-size: 16px; line-height: 1.6;'>
                    {formatted_cover}
                </div>
                """, unsafe_allow_html=True
            )

            st.download_button("📄 Download Cover Letter", cover_letter, "cover_letter.txt")

    else:
        st.success("🎉 Your resume is highly aligned with the job description! Great job!")

# Footer
st.markdown("""
    <hr style="border-top: 2px solid #30363d;">
    <p style="text-align: center; font-size: 14px; color: #8b949e;">
        Made with ❤️ by <a style="color: #58a6ff;" href="https://rajat-gupta-portfolio.netlify.app" target="_blank">Rajat Gupta</a> | Powered by <strong>Gemini AI</strong>
    </p>
""", unsafe_allow_html=True)
