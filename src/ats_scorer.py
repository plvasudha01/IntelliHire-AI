import re


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text: str) -> str:
    """Normalize text for reliable ATS matching."""

    if not text:
        return ""

    text = str(text).lower()
    text = text.replace("–", "-")
    text = text.replace("—", "-")
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ============================================================
# SKILL DEFINITIONS
# ============================================================

SKILL_PATTERNS = {

    "Python": [r"\bpython\b"],

    "C": [
        r"(?<![a-z])c(?![a-z+#])"
    ],

    "C++": [
        r"(?<![a-z])c\+\+(?![a-z])"
    ],

    "Java": [r"\bjava\b"],

    "JavaScript": [r"\bjavascript\b"],

    "HTML": [r"\bhtml\b"],

    "CSS": [r"\bcss\b"],

    "React": [
        r"\breact(?:\.js)?\b"
    ],

    "Flask": [r"\bflask\b"],

    "Django": [r"\bdjango\b"],

    "REST API": [
        r"\brest\s*api\b",
        r"\brestful\s*api\b",
        r"\brestful\b"
    ],

    "SQL": [
        r"(?<![a-z])sql(?![a-z])"
    ],

    "MongoDB": [r"\bmongodb\b"],

    "MySQL": [r"\bmysql\b"],

    "PostgreSQL": [
        r"\bpostgresql\b",
        r"\bpostgres\b"
    ],

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

    "Pandas": [r"\bpandas\b"],

    "NumPy": [r"\bnumpy\b"],

    "Scikit-learn": [
        r"\bscikit[-\s]?learn\b",
        r"\bsklearn\b"
    ],

    "Matplotlib": [r"\bmatplotlib\b"],

    "Seaborn": [r"\bseaborn\b"],

    "TensorFlow": [r"\btensorflow\b"],

    "PyTorch": [r"\bpytorch\b"],

    "Data Structures": [
        r"\bdata\s+structures?\b",
        r"\bdsa\b"
    ],

    "Algorithms": [
        r"\balgorithms?\b",
        r"\bdsa\b"
    ],

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
    "html": ["html"],
    "css": ["css"],
    "react": ["react"],
    "sql": ["sql"],
    "mongodb": ["mongodb"],
    "mysql": ["mysql"],
    "postgresql": ["postgresql", "postgres"],
    "node.js": ["node.js", "nodejs"],
    "flask": ["flask"],
    "django": ["django"],
    "rest api": ["rest api", "restful api", "restful"],
    "machine learning": [
        "machine learning",
        "ml fundamentals"
    ],
    "deep learning": ["deep learning"],
    "data analysis": [
        "data analysis",
        "data analytics"
    ],
    "data science": [
        "data science",
        "ai & data science",
        "artificial intelligence and data science"
    ],
    "data processing": ["data processing"],
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
# SKILL EXTRACTION
# ============================================================

def extract_skills_from_text(text: str):
    """Detect supported technical skills from text."""

    normalized = normalize_text(text)
    found = []

    for skill, patterns in SKILL_PATTERNS.items():
        if _matches_any_pattern(normalized, patterns):
            found.append(skill)

    return found


def _matches_any_pattern(text, patterns):
    """Return True when any pattern matches."""

    return any(
        re.search(pattern, text, re.IGNORECASE)
        for pattern in patterns
    )


def extract_job_keywords(job_description: str):
    """Extract supported technical skills from a JD."""

    return extract_skills_from_text(job_description)


# ============================================================
# JD SECTION EXTRACTION
# ============================================================

REQUIRED_SECTION_PATTERNS = [
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


PREFERRED_SECTION_PATTERNS = [
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


def _extract_section(text, patterns):
    """Extract the first matching JD section."""

    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            return match.group(1)

    return ""


def _get_skill_sections(job_description):
    """Return required and preferred JD sections."""

    text = normalize_text(job_description)

    required = _extract_section(
        text,
        REQUIRED_SECTION_PATTERNS
    )

    preferred = _extract_section(
        text,
        PREFERRED_SECTION_PATTERNS
    )

    return text, required, preferred


# ============================================================
# REQUIRED / PREFERRED CLASSIFICATION
# ============================================================
def _find_section(text, patterns):
    """Return the first matching section from the job description."""
    for pattern in patterns:
        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            return match.group(1)

    return ""


def _classify_skill_by_context(text, skill):
    """Classify a skill using nearby contextual wording."""

    position = text.find(skill.lower())

    if position < 0:
        return "general"

    context_start = max(0, position - 120)
    context_end = min(len(text), position + 180)

    context = text[context_start:context_end]

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

    if any(word in context for word in required_words):
        return "required"

    if any(word in context for word in preferred_words):
        return "preferred"

    return "general"


def _skill_in_section(skill, section):
    """Check whether a skill appears in a section."""
    patterns = SKILL_PATTERNS.get(skill, [])

    return any(
        re.search(
            pattern,
            section,
            re.IGNORECASE
        )
        for pattern in patterns
    )

def classify_job_skills(job_description, job_skills):
    """Classify JD skills using sections and contextual wording."""

    text = normalize_text(job_description)

    required_patterns = [
        r"required\s+skills?(.*?)(?="
        r"preferred\s+skills?|"
        r"nice\s+to\s+have|"
        r"desired\s+skills?|"
        r"bonus|"
        r"qualifications?|"
        r"$)",
        r"requirements?(.*?)(?="
        r"preferred\s+skills?|"
        r"nice\s+to\s+have|"
        r"desired\s+skills?|"
        r"bonus|"
        r"$)",
    ]

    preferred_patterns = [
        r"preferred\s+skills?(.*?)(?="
        r"required\s+skills?|"
        r"requirements?|"
        r"qualifications?|"
        r"$)",
        r"nice\s+to\s+have(.*?)(?="
        r"required\s+skills?|"
        r"requirements?|"
        r"$)",
        r"desired\s+skills?(.*?)(?="
        r"required\s+skills?|"
        r"requirements?|"
        r"$)",
    ]

    required_section = _find_section(
        text,
        required_patterns
    )

    preferred_section = _find_section(
        text,
        preferred_patterns
    )

    categories = {
        "required": [],
        "preferred": [],
        "general": [],
    }

    for skill in job_skills:
        if _skill_in_section(skill, required_section):
            category = "required"

        elif _skill_in_section(skill, preferred_section):
            category = "preferred"

        else:
            category = _classify_skill_by_context(
                text,
                skill
            )

        categories[category].append(skill)

    return (
        categories["required"],
        categories["preferred"],
        categories["general"],
    )


def _classify_skill(
    skill,
    text,
    required_section,
    preferred_section
):
    """Classify one skill."""

    patterns = SKILL_PATTERNS.get(
        skill,
        []
    )

    if _matches_any_pattern(
        required_section,
        patterns
    ):
        return "required"

    if _matches_any_pattern(
        preferred_section,
        patterns
    ):
        return "preferred"

    return _classify_from_context(
        skill,
        text
    )


def _classify_from_context(skill, text):
    """Classify a skill using nearby JD wording."""

    position = text.find(
        skill.lower()
    )

    if position < 0:
        return "general"

    context = _get_skill_context(
        text,
        position
    )

    if _contains_required_word(context):
        return "required"

    if _contains_preferred_word(context):
        return "preferred"

    return "general"


def _get_skill_context(text, position):
    """Get text surrounding a skill occurrence."""

    start = max(
        0,
        position - 120
    )

    end = min(
        len(text),
        position + 180
    )

    return text[start:end]


def _contains_required_word(context):
    """Check for required-skill wording."""

    words = [
        "required",
        "must have",
        "mandatory",
        "essential",
        "must-have",
    ]

    return any(
        word in context
        for word in words
    )


def _contains_preferred_word(context):
    """Check for preferred-skill wording."""

    words = [
        "preferred",
        "nice to have",
        "nice-to-have",
        "desired",
        "bonus",
        "plus",
    ]

    return any(
        word in context
        for word in words
    )


# ============================================================
# RESUME SKILL MATCHING
# ============================================================

def resume_has_skill(resume_skills, skill):
    """Check whether a resume contains a skill."""

    normalized = {
        normalize_text(item)
        for item in resume_skills
        if item
    }

    aliases = SKILL_ALIASES.get(
        skill.lower(),
        [skill.lower()]
    )

    return any(
        normalize_text(alias) in normalized
        for alias in aliases
    )


def _skill_weight(
    skill,
    required_skills,
    preferred_skills
):
    """Return the matching weight for a skill."""

    if skill in required_skills:
        return 2.0

    if skill in preferred_skills:
        return 0.75

    return 1.0


def calculate_skill_match(
    resume_skills,
    job_skills,
    job_description,
    required_skills,
    preferred_skills
):
    """Calculate weighted technical skill match."""

    if not job_skills:
        return 0.0, [], []

    matched = []
    missing = []

    total_weight = 0.0
    matched_weight = 0.0

    for skill in job_skills:
        weight = _skill_weight(
            skill,
            required_skills,
            preferred_skills
        )

        total_weight += weight

        if resume_has_skill(
            resume_skills,
            skill
        ):
            matched.append(skill)
            matched_weight += weight
        else:
            missing.append(skill)

    percentage = _calculate_percentage(
        matched_weight,
        total_weight
    )

    return (
        percentage,
        matched,
        missing
    )


def _calculate_percentage(value, total):
    """Calculate a percentage safely."""

    if total == 0:
        return 0.0

    return value / total * 100


# ============================================================
# KEYWORD MATCH
# ============================================================

KEYWORD_STOP_WORDS = {
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


def _extract_keywords(text):
    """Extract meaningful words from text."""

    words = set(
        re.findall(
            r"\b[a-z][a-z0-9+#.-]{2,}\b",
            normalize_text(text)
        )
    )

    return words - KEYWORD_STOP_WORDS


def calculate_keyword_match(
    resume_text,
    job_description
):
    """Calculate meaningful keyword overlap."""

    resume_words = _extract_keywords(
        resume_text
    )

    job_words = _extract_keywords(
        job_description
    )

    if not job_words:
        return 0.0

    matched = resume_words & job_words

    return _calculate_percentage(
        len(matched),
        len(job_words)
    )


# ============================================================
# PROJECT RELEVANCE
# ============================================================

PROJECT_CONCEPT_GROUPS = {

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


def calculate_project_relevance(
    projects,
    job_description
):
    """Calculate project relevance to the target JD."""

    project_text = normalize_text(projects)
    job_text = normalize_text(job_description)

    if not project_text:
        return 0.0

    relevant = 0
    matched = 0

    for keywords in PROJECT_CONCEPT_GROUPS.values():
        if not _contains_any(job_text, keywords):
            continue

        relevant += 1

        if _contains_any(project_text, keywords):
            matched += 1

    if relevant == 0:
        return 50.0

    return _calculate_percentage(
        matched,
        relevant
    )


def _contains_any(text, keywords):
    """Check whether text contains any keyword."""

    return any(
        keyword in text
        for keyword in keywords
    )


# ============================================================
# EDUCATION MATCH
# ============================================================

EDUCATION_TERMS = [
    "computer science",
    "artificial intelligence",
    "data science",
    "information technology",
    "software engineering",
    "computer engineering",
    "cse",
]


def calculate_education_match(
    education,
    job_description
):
    """Calculate education alignment."""

    education_text = normalize_text(
        education
    )

    job_text = normalize_text(
        job_description
    )

    if not education_text:
        return 30.0

    matches = _count_education_matches(
        education_text,
        job_text
    )

    if matches > 0:
        return 100.0

    if _contains_computer_background(
        education_text
    ):
        return 70.0

    return 30.0


def _count_education_matches(
    education_text,
    job_text
):
    """Count relevant education terms."""

    matches = 0

    for term in EDUCATION_TERMS:
        if term not in education_text:
            continue

        if term in job_text:
            matches += 1
            continue

        if term in {
            "computer science",
            "computer engineering",
            "cse",
        }:
            matches += 1

    return matches


def _contains_computer_background(text):
    """Check for general computing education."""

    return (
        "computer" in text
        or "engineering" in text
    )


# ============================================================
# ATS SCORE COMPONENTS
# ============================================================

def _calculate_skill_component(
    resume_data,
    job_description
):
    """Calculate skill-related ATS data."""

    job_skills = extract_job_keywords(
        job_description
    )

    required, preferred, general = (
        classify_job_skills(
            job_description,
            job_skills
        )
    )

    percentage, matched, missing = (
        calculate_skill_match(
            resume_data.get("skills", []),
            job_skills,
            job_description,
            required,
            preferred
        )
    )

    return {
        "job_skills": job_skills,
        "required_skills": required,
        "preferred_skills": preferred,
        "general_skills": general,
        "matched_skills": matched,
        "missing_skills": missing,
        "skill_match": round(
            percentage,
            2
        ),
    }


def _calculate_other_components(
    resume_data,
    resume_text,
    job_description
):
    """Calculate non-skill ATS components."""

    keyword = calculate_keyword_match(
        resume_text,
        job_description
    )

    project = calculate_project_relevance(
        resume_data.get("projects", ""),
        job_description
    )

    education = calculate_education_match(
        resume_data.get("education", ""),
        job_description
    )

    return {
        "keyword_match": round(
            keyword,
            2
        ),
        "project_relevance": round(
            project,
            2
        ),
        "education_match": round(
            education,
            2
        ),
    }


def _calculate_final_score(components):
    """Calculate final weighted ATS score."""

    return (
        components["skill_match"] * 0.40
        + components["keyword_match"] * 0.25
        + components["project_relevance"] * 0.20
        + components["education_match"] * 0.15
    )


# ============================================================
# COMPLETE ATS SCORE
# ============================================================

def calculate_ats_score(
    resume_data,
    resume_text,
    job_description
):
    """Calculate the complete ATS score."""

    skill_data = _calculate_skill_component(
        resume_data,
        job_description
    )

    other_data = _calculate_other_components(
        resume_data,
        resume_text,
        job_description
    )

    components = {
        **skill_data,
        **other_data,
    }

    score = _calculate_final_score(
        components
    )

    return {
        "score": round(score, 2),
        **components,
    }


# ============================================================
# ATS RECOMMENDATIONS
# ============================================================

def _missing_skill_recommendation(ats_result):
    """Generate missing-skill recommendation."""

    missing = ats_result.get(
        "missing_skills",
        []
    )

    if not missing:
        return None

    required = ats_result.get(
        "required_skills",
        []
    )

    priority = []

    for skill in required:
        if skill in missing:
            priority.append(skill)

    for skill in missing:
        if skill not in priority:
            priority.append(skill)

        if len(priority) >= 5:
            break

    return (
        "Consider adding these missing skills "
        "if you genuinely have experience with them: "
        + ", ".join(priority[:5])
        + "."
    )


def _skill_score_recommendation(ats_result):
    """Generate skill-score recommendation."""

    score = ats_result.get(
        "skill_match",
        0
    )

    if score >= 60:
        return None

    return (
        "Your technical skill match is below 60%. "
        "Tailor the resume to the specific job description."
    )


def _keyword_score_recommendation(ats_result):
    """Generate keyword-score recommendation."""

    score = ats_result.get(
        "keyword_match",
        0
    )

    if score >= 50:
        return None

    return (
        "Your resume has relatively low keyword overlap "
        "with the job description. Use relevant terminology "
        "from the job description where it truthfully "
        "describes your experience."
    )


def _project_recommendation(ats_result):
    """Generate project relevance recommendation."""

    score = ats_result.get(
        "project_relevance",
        0
    )

    if score >= 70:
        return (
            "Your projects are strongly relevant to this role. "
            "Highlight the most relevant project near the top "
            "of your resume."
        )

    return (
        "Add or emphasize projects that directly relate "
        "to the target role."
    )


def _education_recommendation(ats_result):
    """Generate education recommendation."""

    score = ats_result.get(
        "education_match",
        0
    )

    if score < 80:
        return None

    return (
        "Your educational background is well aligned "
        "with this role."
    )


def _project_metrics_recommendation(resume_data):
    """Generate project metrics recommendation."""

    projects = resume_data.get(
        "projects",
        ""
    )

    if not projects:
        return None

    return (
        "Add measurable outcomes to project descriptions "
        "where possible, such as accuracy, performance "
        "improvement, dataset size, or processing time."
    )


def generate_recommendations(
    resume_data,
    ats_result
):
    """Generate recommendations from ATS results."""

    recommendations = []

    recommendation_functions = [
        _missing_skill_recommendation,
        _skill_score_recommendation,
        _keyword_score_recommendation,
        _project_recommendation,
        _education_recommendation,
    ]

    for function in recommendation_functions:
        recommendation = function(
            ats_result
        )

        if recommendation:
            recommendations.append(
                recommendation
            )

    metrics = _project_metrics_recommendation(
        resume_data
    )

    if metrics:
        recommendations.append(metrics)

    return recommendations