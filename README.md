
# RECRUITRA — Intelligent Resume Screening System

RECRUITRA is a resume screening application developed to simplify the initial stages of candidate evaluation. It analyzes uploaded resumes against a given job description, identifies relevant and missing skills, calculates compatibility scores, and ranks candidates accordingly.

## Features

- Upload multiple resumes in PDF and TXT formats.
- Extract text from candidate resumes.
- Identify relevant technical and soft skills.
- Compare candidate profiles against job requirements.
- Calculate weighted compatibility scores.
- Rank candidates based on their matching scores.
- Display matched and missing skills.
- Search and sort candidate screening results.
- Interactive and responsive web interface.

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- PyPDF

## Project Structure

```text
RECRUITRA/
├── data/
│   ├── resumes/
│   └── job_descriptions/
├── src/
│   ├── preprocessing.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── matching_engine.py
│   └── ranking.py
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How It Works

1. The recruiter enters a job description.
2. Multiple candidate resumes are uploaded.
3. Resume text is extracted from PDF or TXT files.
4. Text preprocessing prepares the content for analysis.
5. Relevant skills are identified using keyword-based extraction.
6. Candidate resumes are compared with the job description.
7. A weighted compatibility score is calculated.
8. Candidates are ranked based on their scores.

## Scoring Method

RECRUITRA combines two matching components:

- Skill Match: 65%
- Text Similarity: 35%

The final score is calculated using:

`Final Score = (Skill Match × 0.65 + Text Similarity × 0.35) × 100`

The current implementation uses keyword-based skill extraction and a frequency-based text overlap method.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/anandjyotsna1711-cmd/FUTURE_ML_03
cd RECRUITRA
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open the application at:

`http://127.0.0.1:5000`

## Future Improvements

- Advanced NLP-based resume understanding.
- TF-IDF and cosine similarity-based matching.
- Support for DOCX resumes.
- Improved skill extraction and categorization.
- Candidate filtering based on experience and education.
- More detailed candidate evaluation reports.

## Project Information

Developed as part of the Future Interns Machine Learning Internship — Task 3.

**Project Name:** RECRUITRA  
**Category:** Resume Screening and Candidate Ranking  
**Developer:** Jyotsna A
