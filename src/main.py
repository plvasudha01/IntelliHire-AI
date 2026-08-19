from parser import extract_text
from cleaner import clean_resume_text
from extractor import extract_resume_data
from ats_scorer import (
    calculate_ats_score,
    generate_recommendations,
)


if __name__ == "__main__":
    resume_path = "data/resumes/P.L.VASUDHA.RES.pdf"
    job_path = "data/job_descriptions/software_engineer.txt"

    try:
        # Resume processing
        raw_text = extract_text(resume_path)
        cleaned_text = clean_resume_text(raw_text)
        resume_data = extract_resume_data(cleaned_text)

        # Load job description
        with open(job_path, "r", encoding="utf-8") as file:
            job_description = file.read()

        # Calculate ATS score
        result = calculate_ats_score(
            resume_data,
            cleaned_text,
            job_description,
        )

        # Generate recommendations
        recommendations = generate_recommendations(
            resume_data,
            result,
        )

        print("\n==============================")
        print("       INTELLIHIRE-AI")
        print("==============================")

        print(f"\nATS SCORE: {result['score']}/100")

        print("\n--- Required Skills ---")

        for skill in result.get("required_skills", []):
            print(f"★ {skill}")

        print("\n--- Preferred Skills ---")

        for skill in result.get("preferred_skills", []):
            print(f"☆ {skill}")

        print("\n--- Matched Skills ---")

        for skill in result["matched_skills"]:
            print(f"✓ {skill}")

        print("\n--- Missing Skills ---")

        for skill in result["missing_skills"]:
            print(f"✗ {skill}")

        print("\n--- Score Breakdown ---")

        print(f"Skill Match:       {result['skill_match']}%")
        print(f"Keyword Match:     {result['keyword_match']}%")
        print(f"Project Relevance: {result['project_relevance']}%")
        print(f"Education Match:   {result['education_match']}%")

        print("\n--- ATS Recommendations ---")

        for recommendation in recommendations:
            print(f"• {recommendation}")

    except Exception as e:
        print(f"Error: {e}")