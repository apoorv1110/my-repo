from flask import Flask, request, jsonify
import spacy
import os
import tempfile
import PyPDF2
import docx2txt
import requests

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Function to optimize resume based on job description
def optimize_resume(job_description, candidate_resume):
    job_doc = nlp(job_description)
    job_skills = [token.text for token in job_doc if token.pos_ in ["NOUN", "PROPN"]]

    resume_doc = nlp(candidate_resume)
    resume_skills = [token.text for token in resume_doc if token.pos_ in ["NOUN", "PROPN"]]

    missing_skills = set(job_skills) - set(resume_skills)

    suggestions = []
    if missing_skills:
        suggestions.append(f"Consider adding these skills: {', '.join(missing_skills)}")

    optimized_content = candidate_resume
    for skill in missing_skills:
        if skill.lower() in candidate_resume.lower():
            optimized_content = optimized_content.replace(
                skill,
                f"{skill} (Highlight this skill based on your experience)"
            )

    return {
        "content": optimized_content,
        "suggestions": suggestions,
        "missing_skills": list(missing_skills)
    }

# Function to extract text from uploaded PDF or DOCX file
def extract_text_from_file(file):
    ext = os.path.splitext(file.filename)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as temp:
        file.save(temp.name)
        file_path = temp.name

    try:
        if ext == '.pdf':
            text = ''
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
            return text

        elif ext == '.docx':
            return docx2txt.process(file_path)

        else:
            return None
    finally:
        os.remove(file_path)

# GROK API call (mock)
def analyze_resume_with_grok(job_desc, resume_text):
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Make sure this is set in your environment

    if not GROQ_API_KEY:
        return "GROQ_API_KEY not set."

    prompt = f"""
You are a recruitment expert. Analyze the following resume against the job description.
1. Give a match score out of 100.
2. List 3 strengths.
3. Suggest 3 improvements.

Job Description:
{job_desc}

Resume:
{resume_text}
"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error calling Groq API: {str(e)}"

@app.route('/')
def home():
    return "Resume Optimizer is running with GROK!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    job_description = data.get('jobDescription', '')
    candidate_data = data.get('candidateData', '')

    result = optimize_resume(job_description, candidate_data)
    return jsonify(result)

@app.route('/smart-upload', methods=['POST'])
def smart_upload():
    job_description = request.form.get('jobDescription', '')
    file = request.files.get('resume')

    if not file or not job_description:
        return jsonify({"error": "Missing job description or resume file"}), 400

    candidate_data = extract_text_from_file(file)
    if not candidate_data:
        return jsonify({"error": "Unable to extract text from resume"}), 400

    ai_feedback = analyze_resume_with_grok(job_description, candidate_data)

    return jsonify({
        "jobDescription": job_description,
        "resumeSummary": candidate_data[:500] + "...",
        "grokFeedback": ai_feedback
    })

if __name__ == '__main__':
    app.run(port=5000)
