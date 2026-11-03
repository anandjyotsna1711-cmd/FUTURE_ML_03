from src.preprocessing import clean_text
import re

SKILLS = [
    "python", "java", "c", "c++", "sql",
    "machine learning", "deep learning",
    "artificial intelligence", "data science",
    "data analysis", "pandas", "numpy",
    "scikit-learn", "tensorflow", "pytorch",
    "html", "css", "javascript", "react",
    "flask", "django", "git", "github",
    "communication", "problem solving",
    "teamwork", "mongodb", "mysql",
    "nlp", "spacy", "nltk"
]

def extract_skills(text):
    text = clean_text(text)
    found = set()

    for skill in SKILLS:
        pattern = r'(?<![a-z0-9])' + re.escape(skill) + r'(?![a-z0-9])'

        if re.search(pattern, text):
            found.add(skill)

    return found