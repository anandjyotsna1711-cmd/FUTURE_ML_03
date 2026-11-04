
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

                        matched = sorted(job_skills & resume_skills)
                        missing = sorted(job_skills - resume_skills)

                        results.append({
                            "name": file.filename,
                            "score": score,
                            "matched": matched,
                            "missing": missing,
                            "matched_count": len(matched),
                            "missing_count": len(missing),
                            "total_required": len(job_skills)
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

    # Only successfully processed candidates are included in analytics
    valid_results = [
        candidate for candidate in results
        if "score" in candidate
    ]

    # Overall statistics
    total_candidates = len(valid_results)

    average_score = (
        round(
            sum(c["score"] for c in valid_results) / total_candidates,
            2
        )
        if total_candidates else 0
    )

    highest_score = (
        valid_results[0]["score"] if valid_results else 0
    )

    # Categorise candidates
    strong_matches = sum(
        1 for c in valid_results if c["score"] >= 80
    )

    moderate_matches = sum(
        1 for c in valid_results if 60 <= c["score"] < 80
    )

    low_matches = sum(
        1 for c in valid_results if c["score"] < 60
    )

    # Data for the charts
    analytics = {
        "labels": [c["name"] for c in valid_results],
        "scores": [c["score"] for c in valid_results],
        "distribution": [
            strong_matches,
            moderate_matches,
            low_matches
        ]
    }

    stats = {
        "total_candidates": total_candidates,
        "average_score": average_score,
        "highest_score": highest_score,
        "strong_matches": strong_matches,
        "moderate_matches": moderate_matches,
        "low_matches": low_matches
    }

    return render_template(
    "index.html",
    results=results,
    analytics=analytics,
    stats=stats
)

if __name__ == "__main__":
    app.run(debug=True)
