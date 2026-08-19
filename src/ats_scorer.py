import re


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text: str) -> str:
    """Normalize text for reliable ATS matching."""

    if not text:
        return ""

    text = str(text).lower()

    # Normalize dash characters
    text = text.replace("–", "-")
    text = text.replace("—", "-")

    # Normalize common PDF extraction problems
    text = text.replace("\u00a0", " ")

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# SKILL DEFINITIONS
# ============================================================

SKILL_PATTERNS = {

    # Programming
    "Python": [
        r"\bpython\b"
    ],

    "C": [
        r"(?<![a-z])c(?![a-z+#])"
    ],

    "C++": [
        r"(?<![a-z])c\+\+(?![a-z])"
    ],

    "Java": [
        r"\bjava\b"
    ],

    "JavaScript": [
        r"\bjavascript\b"
    ],

    # Web
    "HTML": [
        r"\bhtml\b"
    ],

    "CSS": [
        r"\bcss\b"
    ],

    "React": [
        r"\breact(?:\.js)?\b"
    ],

    "Flask": [
        r"\bflask\b"
    ],

    "Django": [
        r"\bdjango\b"
    ],

    "REST API": [
        r"\brest\s*api\b",
        r"\brestful\s*api\b",
        r"\brestful\b"
    ],

    # Database
    "SQL": [
        r"(?<![a-z])sql(?![a-z])"
    ],

    "MongoDB": [
        r"\bmongodb\b"
    ],

    "MySQL": [
        r"\bmysql\b"
    ],

    "PostgreSQL": [
        r"\bpostgresql\b",
        r"\bpostgres\b"
    ],

    # Data / ML
    "Machine Learning": [
        r"\bmachine\s+learning\b",
        r"\bml\s+fundamentals\b"
    ],

    "Deep Learning": [
        r"\bdeep\s+learning\b"
    ],

    "Data Analysis": [
        r"\bdata\s+analysis\b",
        r"\bdata\s+analytics\b"
    ],

    "Data Science": [
        r"\bdata\s+science\b",
        r"\bai\s*&\s*data\s+science\b",
        r"\bartificial\s+intelligence\s+and\s+data\s+science\b"
    ],

    "Data Processing": [
        r"\bdata\s+processing\b"
    ],

    "Pandas": [
        r"\bpandas\b"
    ],

    "NumPy": [
        r"\bnumpy\b"
    ],

    "Scikit-learn": [
        r"\bscikit[-\s]?learn\b",
        r"\bsklearn\b"
    ],

    "Matplotlib": [
        r"\bmatplotlib\b"
    ],

    "Seaborn": [
        r"\bseaborn\b"
    ],

    "TensorFlow": [
        r"\btensorflow\b"
    ],

    "PyTorch": [
        r"\bpytorch\b"
    ],

    # Core CS
    "Data Structures": [
        r"\bdata\s+structures?\b",
        r"\bdsa\b"
    ],

    "Algorithms": [
        r"\balgorithms?\b",
        r"\bdsa\b"
    ],

    # Development tools
    "Git": [
        r"(?<![a-z])git(?!hub)"
    ],

    "GitHub": [
        r"\bgithub\b"
    ],

    "Docker": [
        r"\bdocker\b"
    ],

    "Linux": [
        r"\blinux\b"
    ],

    # Cloud
    "AWS": [
        r"\baws\b",
        r"\bamazon\s+web\s+services\b"
    ],

    "Azure": [
        r"\bazure\b"
    ],

    "Google Cloud": [
        r"\bgoogle\s+cloud\b"
    ],

    # Other
    "Node.js": [
        r"\bnode\.?js\b",
        r"\bnodejs\b"
    ],

    "Arduino": [
        r"\barduino\b"
    ],

    "Google Workspace": [
        r"\bgoogle\s+workspace\b"
    ],
}


# ============================================================
# SKILL ALIASES
# ============================================================

SKILL_ALIASES = {

    "python": ["python"],

    "c": ["c"],

    "c++": ["c++"],

    "java": ["java"],

    "javascript": ["javascript"],

    "sql": ["sql"],

    "mongodb": ["mongodb"],

    "mysql": ["mysql"],

    "postgresql": [
        "postgresql",
        "postgres"
    ],

    "node.js": [
        "node.js",
        "nodejs"
    ],

    "flask": ["flask"],

    "django": ["django"],

    "rest api": [
        "rest api",
        "restful api",
        "restful"
    ],

    "machine learning": [
        "machine learning",
        "ml fundamentals"
    ],

    "deep learning": [
        "deep learning"
    ],

    "data analysis": [
        "data analysis",
        "data analytics"
    ],

    "data science": [
        "data science",
        "ai & data science",
        "artificial intelligence and data science"
    ],

    "data processing": [
        "data processing"
    ],

    "pandas": ["pandas"],

    "numpy": ["numpy"],

    "scikit-learn": [
        "scikit-learn",
        "scikit learn",
        "sklearn"
    ],

    "matplotlib": ["matplotlib"],

    "seaborn": ["seaborn"],

    "tensorflow": ["tensorflow"],

    "pytorch": ["pytorch"],

    "data structures": [
        "data structures",
        "data structure",
        "dsa"
    ],

    "algorithms": [
        "algorithms",
        "algorithm",
        "dsa"
    ],

    "git": ["git"],

    "github": ["github"],

    "docker": ["docker"],

    "linux": ["linux"],

    "aws": [
        "aws",
        "amazon web services"
    ],

    "azure": ["azure"],

    "google cloud": ["google cloud"],

    "arduino": ["arduino"],

    "google workspace": [
        "google workspace"
    ],
}


# ============================================================
# EXTRACT SKILLS FROM TEXT
# ============================================================

def extract_skills_from_text(text: str):
    """
    Detect technical skills directly from any text.
    Used for both resumes and job descriptions.
    """

    text = normalize_text(text)

    found = []

    for skill, patterns in SKILL_PATTERNS.items():

        for pattern in patterns:

            if re.search(
                pattern,
                text,
                re.IGNORECASE
            ):
                found.append(skill)
                break

    return found


# ============================================================
# JOB SKILL EXTRACTION
# ============================================================

def extract_job_keywords(job_description: str):
    """
    Extract all supported technical skills from the JD.
    """

    return extract_skills_from_text(
        job_description
    )


# ============================================================
# REQUIRED / PREFERRED CLASSIFICATION
# ============================================================

def classify_job_skills(
    job_description,
    job_skills
):
    """
    Classify JD skills using section headings.

    If the JD explicitly contains sections such as:

        Required Skills
        Preferred Skills

    those sections are used directly.

    Otherwise, contextual wording is used.
    """

    text = normalize_text(
        job_description
    )

    required_skills = []
    preferred_skills = []
    general_skills = []

    # --------------------------------------------------------
    # Find required section
    # --------------------------------------------------------

    required_section = ""

    required_patterns = [
        r"required\s+skills?(.*?)(?="
        r"preferred\s+skills?|"
        r"nice\s+to\s+have|"
        r"desired\s+skills?|"
        r"bonus|"
        r"qualifications?|"
        r"$"
        r")",

        r"requirements?(.*?)(?="
        r"preferred\s+skills?|"
        r"nice\s+to\s+have|"
        r"desired\s+skills?|"
        r"bonus|"
        r"$"
        r")",
    ]

    for pattern in required_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            required_section = match.group(1)
            break

    # --------------------------------------------------------
    # Find preferred section
    # --------------------------------------------------------

    preferred_section = ""

    preferred_patterns = [
        r"preferred\s+skills?(.*?)(?="
        r"required\s+skills?|"
        r"requirements?|"
        r"qualifications?|"
        r"$"
        r")",

        r"nice\s+to\s+have(.*?)(?="
        r"required\s+skills?|"
        r"requirements?|"
        r"$"
        r")",

        r"desired\s+skills?(.*?)(?="
        r"required\s+skills?|"
        r"requirements?|"
        r"$"
        r")",
    ]

    for pattern in preferred_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            preferred_section = match.group(1)
            break

    # --------------------------------------------------------
    # Classify each skill
    # --------------------------------------------------------

    for skill in job_skills:

        skill_patterns = SKILL_PATTERNS.get(
            skill,
            []
        )

        in_required = any(
            re.search(
                pattern,
                required_section,
                re.IGNORECASE
            )
            for pattern in skill_patterns
        )

        in_preferred = any(
            re.search(
                pattern,
                preferred_section,
                re.IGNORECASE
            )
            for pattern in skill_patterns
        )

        if in_required:

            required_skills.append(skill)

        elif in_preferred:

            preferred_skills.append(skill)

        else:

            # Contextual fallback
            skill_position = text.find(
                skill.lower()
            )

            if skill_position >= 0:

                context_start = max(
                    0,
                    skill_position - 120
                )

                context_end = min(
                    len(text),
                    skill_position + 180
                )

                context = text[
                    context_start:context_end
                ]

                required_words = [
                    "required",
                    "must have",
                    "mandatory",
                    "essential",
                    "must-have",
                ]

                preferred_words = [
                    "preferred",
                    "nice to have",
                    "nice-to-have",
                    "desired",
                    "bonus",
                    "plus",
                ]

                if any(
                    word in context
                    for word in required_words
                ):
                    required_skills.append(skill)

                elif any(
                    word in context
                    for word in preferred_words
                ):
                    preferred_skills.append(skill)

                else:
                    general_skills.append(skill)

            else:

                general_skills.append(skill)

    return (
        required_skills,
        preferred_skills,
        general_skills
    )


# ============================================================
# CHECK WHETHER RESUME HAS A SKILL
# ============================================================

def resume_has_skill(
    resume_skills,
    skill
):
    """
    Check skill using exact normalized aliases.
    """

    resume_normalized = {
        normalize_text(skill)
        for skill in resume_skills
        if skill
    }

    aliases = SKILL_ALIASES.get(
        skill.lower(),
        [skill.lower()]
    )

    for alias in aliases:

        if normalize_text(alias) in resume_normalized:
            return True

    return False


# ============================================================
# SKILL MATCH
# ============================================================

def calculate_skill_match(
    resume_skills,
    job_skills,
    job_description,
    required_skills,
    preferred_skills
):
    """
    Calculate weighted technical skill match.

    Required skills = highest weight
    Preferred skills = medium weight
    General skills = normal weight
    """

    if not job_skills:

        return (
            0.0,
            [],
            []
        )

    matched = []
    missing = []

    total_weight = 0.0
    matched_weight = 0.0

    for skill in job_skills:

        # Weight
        if skill in required_skills:

            weight = 2.0

        elif skill in preferred_skills:

            weight = 0.75

        else:

            weight = 1.0

        total_weight += weight

        if resume_has_skill(
            resume_skills,
            skill
        ):

            matched.append(skill)
            matched_weight += weight

        else:

            missing.append(skill)

    if total_weight == 0:

        percentage = 0.0

    else:

        percentage = (
            matched_weight
            / total_weight
            * 100
        )

    return (
        percentage,
        matched,
        missing
    )


# ============================================================
# KEYWORD MATCH
# ============================================================

def calculate_keyword_match(
    resume_text,
    job_description
):
    """
    Calculate meaningful keyword overlap.

    Common stop words are removed so the score reflects
    technical/job-related terminology rather than words like
    'and', 'the', 'with', etc.
    """

    resume_text = normalize_text(
        resume_text
    )

    job_text = normalize_text(
        job_description
    )

    stop_words = {
        "the",
        "and",
        "for",
        "with",
        "from",
        "that",
        "this",
        "are",
        "you",
        "your",
        "our",
        "will",
        "have",
        "has",
        "not",
        "but",
        "all",
        "any",
        "can",
        "who",
        "their",
        "they",
        "job",
        "role",
        "work",
        "using",
        "use",
        "into",
        "about",
        "also",
        "should",
        "must",
        "would",
        "years",
        "year",
        "experience",
    }

    resume_words = set(
        re.findall(
            r"\b[a-z][a-z0-9+#.-]{2,}\b",
            resume_text
        )
    )

    job_words = set(
        re.findall(
            r"\b[a-z][a-z0-9+#.-]{2,}\b",
            job_text
        )
    )

    resume_words -= stop_words
    job_words -= stop_words

    if not job_words:

        return 0.0

    matched_words = (
        resume_words
        & job_words
    )

    return (
        len(matched_words)
        / len(job_words)
        * 100
    )


# ============================================================
# PROJECT RELEVANCE
# ============================================================

def calculate_project_relevance(
    projects,
    job_description
):
    """
    Calculate how strongly the candidate's projects
    relate to the job description.
    """

    project_text = normalize_text(
        projects
    )

    job_text = normalize_text(
        job_description
    )

    if not project_text:

        return 0.0

    concept_groups = {

        "machine learning": [
            "machine learning",
            "ml",
            "classification",
            "regression",
            "prediction",
            "similarity",
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
            "python"
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
            "database"
        ],

        "automation": [
            "automation",
            "arduino",
            "sensor",
            "control system",
        ],

        "web development": [
            "web",
            "flask",
            "django",
            "api",
            "application",
        ],
    }

    relevant_groups = 0
    matched_groups = 0

    for keywords in concept_groups.values():

        job_requires_group = any(
            keyword in job_text
            for keyword in keywords
        )

        if not job_requires_group:
            continue

        relevant_groups += 1

        project_matches_group = any(
            keyword in project_text
            for keyword in keywords
        )

        if project_matches_group:

            matched_groups += 1

    if relevant_groups == 0:

        # If the JD has no recognizable concept,
        # give a neutral score instead of zero.
        return 50.0

    return (
        matched_groups
        / relevant_groups
        * 100
    )


# ============================================================
# EDUCATION MATCH
# ============================================================

def calculate_education_match(
    education,
    job_description
):
    """
    Determine how well the candidate's education
    matches the role.
    """

    education_text = normalize_text(
        education
    )

    job_text = normalize_text(
        job_description
    )

    if not education_text:

        return 30.0

    relevant_terms = [

        "computer science",

        "artificial intelligence",

        "data science",

        "information technology",

        "software engineering",

        "computer engineering",

        "cse",
    ]

    matches = 0

    for term in relevant_terms:

        if term in education_text:

            if (
                term in job_text
                or term in {
                    "computer science",
                    "computer engineering",
                    "cse",
                }
            ):

                matches += 1

    if matches > 0:

        return 100.0

    if (
        "computer" in education_text
        or "engineering" in education_text
    ):

        return 70.0

    return 30.0


# ============================================================
# COMPLETE ATS SCORE
# ============================================================

def calculate_ats_score(
    resume_data,
    resume_text,
    job_description
):
    """
    Calculate the complete ATS score.
    """

    # --------------------------------------------------------
    # Job skills
    # --------------------------------------------------------

    job_skills = extract_job_keywords(
        job_description
    )

    (
        required_skills,
        preferred_skills,
        general_skills
    ) = classify_job_skills(
        job_description,
        job_skills
    )

    # --------------------------------------------------------
    # Skill matching
    # --------------------------------------------------------

    (
        skill_percentage,
        matched_skills,
        missing_skills
    ) = calculate_skill_match(
        resume_data.get(
            "skills",
            []
        ),
        job_skills,
        job_description,
        required_skills,
        preferred_skills
    )

    # --------------------------------------------------------
    # Keyword matching
    # --------------------------------------------------------

    keyword_percentage = (
        calculate_keyword_match(
            resume_text,
            job_description
        )
    )

    # --------------------------------------------------------
    # Project relevance
    # --------------------------------------------------------

    project_percentage = (
        calculate_project_relevance(
            resume_data.get(
                "projects",
                ""
            ),
            job_description
        )
    )

    # --------------------------------------------------------
    # Education
    # --------------------------------------------------------

    education_percentage = (
        calculate_education_match(
            resume_data.get(
                "education",
                ""
            ),
            job_description
        )
    )

    # --------------------------------------------------------
    # Final weighted score
    # --------------------------------------------------------

    score = (

        skill_percentage * 0.40

        + keyword_percentage * 0.25

        + project_percentage * 0.20

        + education_percentage * 0.15
    )

    return {

        "score": round(
            score,
            2
        ),

        "job_skills": job_skills,

        "required_skills": required_skills,

        "preferred_skills": preferred_skills,

        "general_skills": general_skills,

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "skill_match": round(
            skill_percentage,
            2
        ),

        "keyword_match": round(
            keyword_percentage,
            2
        ),

        "project_relevance": round(
            project_percentage,
            2
        ),

        "education_match": round(
            education_percentage,
            2
        ),
    }


# ============================================================
# ATS RECOMMENDATIONS
# ============================================================

def generate_recommendations(
    resume_data,
    ats_result
):
    """
    Generate useful recommendations based on
    actual ATS results.
    """

    recommendations = []

    missing_skills = ats_result.get(
        "missing_skills",
        []
    )

    # --------------------------------------------------------
    # Missing skills
    # --------------------------------------------------------

    if missing_skills:

        high_priority = []

        # Required missing skills first
        required = ats_result.get(
            "required_skills",
            []
        )

        for skill in required:

            if skill in missing_skills:
                high_priority.append(skill)

        # Then preferred/general
        for skill in missing_skills:

            if (
                skill not in high_priority
                and len(high_priority) < 5
            ):
                high_priority.append(skill)

        high_priority = high_priority[:5]

        recommendations.append(
            "Consider adding these missing skills "
            "if you genuinely have experience with them: "
            + ", ".join(high_priority)
            + "."
        )

    # --------------------------------------------------------
    # Skill score
    # --------------------------------------------------------

    skill_match = ats_result.get(
        "skill_match",
        0
    )

    if skill_match < 60:

        recommendations.append(
            "Your technical skill match is below 60%. "
            "Tailor the resume to the specific job description."
        )

    # --------------------------------------------------------
    # Keyword score
    # --------------------------------------------------------

    keyword_match = ats_result.get(
        "keyword_match",
        0
    )

    if keyword_match < 50:

        recommendations.append(
            "Your resume has relatively low keyword overlap "
            "with the job description. Use relevant terminology "
            "from the job description where it truthfully "
            "describes your experience."
        )

    # --------------------------------------------------------
    # Projects
    # --------------------------------------------------------

    project_relevance = ats_result.get(
        "project_relevance",
        0
    )

    if project_relevance >= 70:

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

    # --------------------------------------------------------
    # Education
    # --------------------------------------------------------

    education_match = ats_result.get(
        "education_match",
        0
    )

    if education_match >= 80:

        recommendations.append(
            "Your educational background is well aligned "
            "with this role."
        )

    # --------------------------------------------------------
    # Project metrics
    # --------------------------------------------------------

    projects = resume_data.get(
        "projects",
        ""
    )

    if projects:

        recommendations.append(
            "Add measurable outcomes to project descriptions "
            "where possible, such as accuracy, performance "
            "improvement, dataset size, or processing time."
        )

    return recommendations