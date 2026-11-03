def score_candidate(job_skills, resume_skills, similarity):
    if job_skills:
        skill_match = len(job_skills & resume_skills) / len(job_skills)
    else:
        skill_match = 0

    score = (skill_match * 0.65 + similarity * 0.35) * 100

    return round(score, 2)