# 🧠 Resume Optimizer API with GROQ Integration

A Flask-based API that analyzes and optimizes resumes based on job descriptions using spaCy for NLP and GROQ's LLM for AI-powered feedback.

🟢 **Live API Endpoint**: [https://my-repo-4dtz.onrender.com/smart-upload](https://my-repo-4dtz.onrender.com/smart-upload)

---

## 🚀 Features

- Upload `.pdf` or `.docx` resumes
- Extracts skills using NLP (spaCy)
- Compares resume with job description
- Provides AI-generated feedback:
  - Match Score (out of 100)
  - Top 3 strengths
  - 3 Suggestions for improvement
- Identifies and highlights missing skills

---

## 🧠 Technologies Used

- Python 3
- Flask
- spaCy
- PyPDF2
- docx2txt
- GROQ LLM API
- Render (Deployment)

---

## 🔌 API Endpoints

### ✅ `POST /smart-upload`

Upload a resume and job description.

#### Request (form-data):

| Field           | Type     | Description                           |
|----------------|----------|---------------------------------------|
| jobDescription | `string` | Text of the job description            |
| resume         | `file`   | Resume file (`.pdf` or `.docx`)       |

#### Example cURL:

```bash
curl -X POST https://my-repo-4dtz.onrender.com/smart-upload \
  -F "jobDescription=Looking for a Python developer with NLP experience" \
  -F "resume=@resume.pdf"
