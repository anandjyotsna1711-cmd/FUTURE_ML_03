import re
from collections import Counter

def calculate_similarity(job_description, resume_text):
    def tokenize(text):
        return re.findall(r'\b[a-zA-Z0-9+#.-]+\b', text.lower())

    job_words = Counter(tokenize(job_description))
    resume_words = Counter(tokenize(resume_text))

    common = sum((job_words & resume_words).values())
    total = sum(job_words.values())

    if total == 0:
        return 0.0

    return common / total