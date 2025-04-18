import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY is missing in your .env file!")

# Configure Gemini
genai.configure(api_key=api_key)

# Use a supported model from your list
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")


# ✅ Define the function at module level
def suggest_resume_improvements(resume_text, job_desc):
    prompt = f"""
You are an expert resume coach.

Given the resume and job description, suggest detailed improvements to make the resume a better match for the job.
Include suggestions related to skills, formatting, keywords, achievements, and tailoring for the role.

Resume:
{resume_text}

Job Description:
{job_desc}

Suggestions:
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error generating suggestions: {str(e)}"
