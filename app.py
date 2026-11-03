
from flask import Flask, render_template, request
from src.resume_parser import extract_text
from src.skill_extractor import extract_skills
from src.matching_engine import calculate_similarity
from src.ranking import score_candidate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []

    if request.method == "POST":
        job_description = request.form.get("job_description", "")
        files = request.files.getlist("resumes")

        if job_description.strip() and files:
            job_skills = extract_skills(job_description)

            for file in files:
                if file.filename:
                    try:
                        resume_text = extract_text(file)
                        resume_skills = extract_skills(resume_text)

                        similarity = calculate_similarity(
                            job_description, resume_text
                        )

                        score = score_candidate(
                            job_skills, resume_skills, similarity
                        )

                        results.append({
                            "name": file.filename,
                            "score": score,
                            "matched": sorted(job_skills & resume_skills),
                            "missing": sorted(job_skills - resume_skills)
                        })

                    except Exception as error:
                        results.append({
                            "name": file.filename,
                            "error": str(error)
                        })

            results.sort(
                key=lambda x: x.get("score", -1),
                reverse=True
            )

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
