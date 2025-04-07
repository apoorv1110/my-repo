# 🧠 Resume Optimizer API with GROQ Integration

A Flask-based API that analyzes and optimizes resumes based on job descriptions using spaCy for NLP and GROQ's LLM for AI-powered feedback.

🟢 **Live API Endpoint**: [https://my-repo-4dtz.onrender.com](https://my-repo-4dtz.onrender.com)

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
```
# 🧠 Resume Analysis API - `/analyze` Endpoint

This endpoint allows you to directly analyze and compare a candidate's resume text with a job description using NLP (spaCy). It identifies missing skills and provides helpful suggestions.

---

## ✅ POST `/analyze`

Compare resume text and job description directly (no file upload required).

### 📥 Request

**Content-Type:** `application/json`

```json
{
  "jobDescription": "Looking for a backend developer with Flask and SQL.",
  "candidateData": "I am skilled in Django, REST APIs, and Python."
}
```
## 🛠️ Local Development Setup

Follow these steps to run the API locally on your machine:

---

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/resume-optimizer.git
cd resume-optimizer
```
### 2. Add Your GROQ API Key
#### Create a .env file in the root directory and add your key:
```bash
GROQ_API_KEY=your_actual_groq_api_key_here
```
### 3. Install Dependencies
#### Install the required Python packages and download the necessary spaCy language model:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
### 4. Run the Application
#### Start the Flask app locally:
```bash
python app.py
```
