import re


def normalize_text(text: str) -> str:
    """Normalize text for matching."""
    return re.sub(r"\s+", " ", text.lower()).strip()


def extract_job_keywords(job_description: str):
    """Extract important technical keywords from a job description."""

    skills = [
        "Python",
        "C",
        "C++",
        "Java",
        "SQL",
        "MongoDB",
        "Node.js",
        "JavaScript",
        "HTML",
        "CSS",
        "React",
        "Flask",
        "Django",
        "Machine Learning",
        "Deep Learning",
        "Data Analysis",
        "Data Science",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "Git",
        "GitHub",
        "AWS",
        "Docker",
        "Linux",
        "REST API",
        "Data Structures",
        "Algorithms",
    ]

    job_text = normalize_text(job_description)

    found = []

    for skill in skills:
        if re.search(
            rf"\b{re.escape(skill.lower())}\b",
            job_text,
        ):
            found.append(skill)

    return found


def calculate_skill_match(resume_skills, job_skills):
    """Calculate skill match percentage using skill aliases."""

    aliases = {
        "machine learning": ["machine learning", "ml"],
        "data science": ["data science", "ai & data science"],
        "data analysis": ["data analysis", "data analytics"],
        "scikit-learn": ["scikit-learn", "sklearn"],
        "github": ["github"],
        "data structures": ["data structures", "dsa"],
        "algorithms": ["algorithms", "algorithm"],
        "rest api": ["rest api", "restful api"],
    }

    resume_normalized = {
        skill.lower()
        for skill in resume_skills
    }

    matched = []
    missing = []

    for skill in job_skills:
        skill_lower = skill.lower()

        possible_matches = aliases.get(
            skill_lower,
            [skill_lower],
        )

        found = any(
            item in resume_normalized
            for item in possible_matches
        )

        if found:
            matched.append(skill)
        else:
            missing.append(skill)

    percentage = (
        len(matched) / len(job_skills) * 100
        if job_skills
        else 0
    )

    return percentage, matched, missing

def calculate_keyword_match(resume_text, job_description):
    """Calculate general keyword overlap."""

    resume_words = set(
        re.findall(
            r"\b[a-zA-Z][a-zA-Z0-9+#.-]{2,}\b",
            normalize_text(resume_text),
        )
    )

    job_words = set(
        re.findall(
            r"\b[a-zA-Z][a-zA-Z0-9+#.-]{2,}\b",
            normalize_text(job_description),
        )
    )

    if not job_words:
        return 0

    matched_words = resume_words.intersection(job_words)

    return (len(matched_words) / len(job_words)) * 100


def calculate_project_relevance(projects, job_description):
    """Calculate project relevance using related technical concepts."""

    project_text = normalize_text(projects)
    job_text = normalize_text(job_description)

    concept_groups = {
        "machine learning": [
            "machine learning",
            "ml",
            "classification",
            "regression",
            "prediction",
        ],
        "data analysis": [
            "data analysis",
            "data analytics",
            "data preprocessing",
            "data visualization",
            "dataset",
            "insights",
        ],
        "python": [
            "python",
        ],
        "software development": [
            "software",
            "application",
            "development",
            "system",
        ],
        "data science": [
            "data science",
            "data preprocessing",
            "data analysis",
        ],
        "sql": [
            "sql",
            "database",
        ],
        "automation": [
            "automation",
            "arduino",
            "sensor",
            "control systems",
        ],
    }

    relevant_groups = 0
    matched_groups = 0

    for group, keywords in concept_groups.items():
        job_requires_group = any(
            keyword in job_text
            for keyword in keywords
        )

        if job_requires_group:
            relevant_groups += 1

            project_matches_group = any(
                keyword in project_text
                for keyword in keywords
            )

            if project_matches_group:
                matched_groups += 1

    if relevant_groups == 0:
        return 0

    return (matched_groups / relevant_groups) * 100

def calculate_education_match(education, job_description):
    """Check whether the education appears relevant."""

    education_text = normalize_text(education)
    job_text = normalize_text(job_description)

    relevant_terms = [
        "computer science",
        "artificial intelligence",
        "data science",
        "information technology",
        "software engineering",
        "computer engineering",
    ]

    matches = 0

    for term in relevant_terms:
        if term in education_text and term in job_text:
            matches += 1

    if matches > 0:
        return 100

    if "computer" in education_text:
        return 70

    return 30


def calculate_ats_score(resume_data, resume_text, job_description):
    """Calculate the overall ATS score."""

    job_skills = extract_job_keywords(job_description)

    skill_percentage, matched_skills, missing_skills = (
        calculate_skill_match(
            resume_data.get("skills", []),
            job_skills,
        )
    )

    keyword_percentage = calculate_keyword_match(
        resume_text,
        job_description,
    )

    project_percentage = calculate_project_relevance(
        resume_data.get("projects", ""),
        job_description,
    )

    education_percentage = calculate_education_match(
        resume_data.get("education", ""),
        job_description,
    )

    score = (
        skill_percentage * 0.40
        + keyword_percentage * 0.25
        + project_percentage * 0.20
        + education_percentage * 0.15
    )

    return {
        "score": round(score, 2),
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "skill_match": round(skill_percentage, 2),
        "keyword_match": round(keyword_percentage, 2),
        "project_relevance": round(project_percentage, 2),
        "education_match": round(education_percentage, 2),
    }
def generate_recommendations(
    resume_data,
    ats_result,
):
    """Generate actionable ATS improvement recommendations."""

    recommendations = []

    missing_skills = ats_result.get(
        "missing_skills",
        [],
    )

    if missing_skills:
        high_priority = missing_skills[:5]

        recommendations.append(
            "Consider adding these missing skills if you "
            "genuinely have experience with them: "
            + ", ".join(high_priority)
            + "."
        )

    if ats_result.get("skill_match", 0) < 60:
        recommendations.append(
            "Your technical skill match is below 60%. "
            "Tailor the resume to the specific job description."
        )

    if ats_result.get("keyword_match", 0) < 50:
        recommendations.append(
            "Your resume has relatively low keyword overlap "
            "with the job description. Use relevant terminology "
            "from the job description where it truthfully "
            "describes your experience."
        )

    if ats_result.get("project_relevance", 0) >= 70:
        recommendations.append(
            "Your projects are strongly relevant to this role. "
            "Highlight the most relevant project near the top "
            "of your resume."
        )
    else:
        recommendations.append(
            "Add or emphasize projects that directly relate "
            "to the target role."
        )

    if ats_result.get("education_match", 0) >= 80:
        recommendations.append(
            "Your educational background is well aligned "
            "with this role."
        )

    projects = resume_data.get("projects", "")

    if projects:
        recommendations.append(
            "Add measurable outcomes to project descriptions "
            "where possible, such as accuracy, performance "
            "improvement, dataset size, or processing time."
        )

    return recommendations