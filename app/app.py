
from flask import Flask, render_template, request
from pathlib import Path
import sys


# Allow Flask to access the src folder
BASE_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = BASE_DIR / "src"

sys.path.insert(0, str(SRC_DIR))


from parser import extract_text
from cleaner import clean_resume_text
from extractor import extract_resume_data
from ats_scorer import (
    calculate_ats_score,
    generate_recommendations,
)


app = Flask(__name__)


UPLOAD_FOLDER = BASE_DIR / "data" / "resumes"
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


def process_resume(resume_path, job_description):
    raw_text = extract_text(
        str(resume_path)
    )

    cleaned_text = clean_resume_text(
        raw_text
    )

    resume_data = extract_resume_data(
        cleaned_text
    )

    result = calculate_ats_score(
        resume_data,
        cleaned_text,
        job_description,
    )

    recommendations = generate_recommendations(
        resume_data,
        result,
    )

    return (
        resume_data,
        result,
        recommendations,
    )


@app.route("/analyze", methods=["POST"])
def analyze():
    resume = request.files.get("resume")
    job_description = request.form.get("job_description", "").strip()

    if not resume or not resume.filename:
        return "Please upload a resume.", 400
    if not job_description:
        return "Please enter a job description.", 400

    filename = Path(resume.filename).name
    extension = Path(filename).suffix.lower()

    if extension not in {".pdf", ".docx"}:
        return "Only PDF and DOCX resumes are supported.", 400

    resume_path = UPLOAD_FOLDER / filename
    resume.save(resume_path)

    try:
        resume_data, result, recommendations = process_resume(
            resume_path,
            job_description,
        )
        return render_template(
            "results.html",
            resume=resume_data,
            result=result,
            recommendations=recommendations,
        )
    except Exception as e:
        return f"Error analyzing resume: {e}", 500




if __name__ == "__main__":
    app.run(
        debug=True
    )

