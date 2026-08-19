import re


def extract_email(text: str):
    match = re.search(
        r"[\w\.-]+@[\w\.-]+\.\w+",
        text
    )
    return match.group(0) if match else None


def extract_phone(text: str):
    match = re.search(
        r"\+?\d[\d\s-]{9,}\d",
        text
    )
    return match.group(0).strip() if match else None


def extract_cgpa(text: str):
    match = re.search(
        r"\bCGPA\s*[:\-]?\s*(\d+(?:\.\d+)?)",
        text,
        re.IGNORECASE
    )

    return float(match.group(1)) if match else None


def extract_name(text: str):
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if not lines:
        return None

    # Usually the first line of the resume is the candidate name.
    return lines[0]


def extract_linkedin(text: str):
    match = re.search(
        r"(?:https?://)?(?:www\.)?"
        r"linkedin\.com/in/[A-Za-z0-9_-]+",
        text,
        re.IGNORECASE
    )

    return match.group(0) if match else None


def extract_section(
    text: str,
    start: str,
    end_sections: list[str]
):
    end_pattern = "|".join(
        re.escape(section)
        for section in end_sections
        if section.lower() != start.lower()
    )

    pattern = rf"""
        {re.escape(start)}
        (.*?)
        (?:
            {end_pattern}
            |$
        )
    """

    match = re.search(
        pattern,
        text,
        re.IGNORECASE | re.DOTALL | re.VERBOSE
    )

    if not match:
        return ""

    return match.group(1).strip()


def extract_skills(text: str):
    """
    Detect technical skills from the complete resume text.

    A skill is returned only when its actual keyword
    appears in the resume.
    """

    skill_patterns = {

        # -------------------------
        # Programming Languages
        # -------------------------

        "Python": r"\bpython\b",

        "C": r"(?<![A-Za-z])C(?![A-Za-z+#])",

        "C++": r"(?<![A-Za-z])C\+\+(?![A-Za-z])",

        "Java": r"\bjava\b",

        "JavaScript": r"\bjavascript\b",

        # -------------------------
        # Web Development
        # -------------------------

        "HTML": r"\bhtml\b",

        "CSS": r"\bcss\b",

        "React": r"\breact(?:\.js)?\b",

        "Flask": r"\bflask\b",

        "Django": r"\bdjango\b",

        "REST API": r"\brest(?:ful)?\s+api\b",

        # -------------------------
        # Databases
        # -------------------------
	"SQL": r"sql",

        "MongoDB": r"\bmongodb\b",

        "MySQL": r"\bmysql\b",

        "PostgreSQL": r"\bpostgres(?:ql)?\b",

        # -------------------------
        # Machine Learning
        # -------------------------

        "Machine Learning": (
            r"\bmachine\s+learning\b"
            r"|\bml\s+fundamentals\b"
        ),

        "Deep Learning": r"\bdeep\s+learning\b",

        "Data Science": (
            r"\bdata\s+science\b"
            r"|\bai\s*&\s*data\s+science\b"
        ),

        "Data Analysis": (
            r"\bdata\s+analysis\b"
            r"|\bdata\s+analytics\b"
        ),

        "Data Processing": r"\bdata\s+processing\b",

        # -------------------------
        # Python / ML Libraries
        # -------------------------

        "Pandas": r"\bpandas\b",

        "NumPy": r"\bnumpy\b",

        "Scikit-learn": (
            r"\bscikit[- ]learn\b"
            r"|\bsklearn\b"
        ),

        "Matplotlib": r"\bmatplotlib\b",

        "Seaborn": r"\bseaborn\b",

        "TensorFlow": r"\btensorflow\b",

        "PyTorch": r"\bpytorch\b",

        # -------------------------
        # Computer Science
        # -------------------------

        "Data Structures": (
            r"\bdata\s+structures?\b"
            r"|\bdsa\b"
        ),

        "Algorithms": (
            r"\balgorithms?\b"
            r"|\bdsa\b"
        ),

        # -------------------------
        # Development Tools
        # -------------------------

        "Git": r"(?<![A-Za-z])git(?![A-Za-z])",

        "GitHub": r"\bgithub\b",

        "Docker": r"\bdocker\b",

        "Linux": r"\blinux\b",

        # -------------------------
        # Cloud
        # -------------------------

        "AWS": r"(?<![A-Za-z])aws(?![A-Za-z])",

        "Azure": r"\bazure\b",

        "Google Cloud": r"\bgoogle\s+cloud\b",

        # -------------------------
        # Hardware
        # -------------------------

        "Arduino": r"\barduino\b",

        # -------------------------
        # Other
        # -------------------------

        "Node.js": r"\bnode\.js\b",

        "Google Workspace": r"\bgoogle\s+workspace\b",
    }

    found = []

    for skill, pattern in skill_patterns.items():

        if re.search(
            pattern,
            text,
            re.IGNORECASE
        ):
            found.append(skill)

    return found


def extract_resume_data(text: str):

    sections = [
        "OBJECTIVE",
        "EDUCATION",
        "TECHNICAL SKILLS",
        "PROJECTS",
        "CORE STRENGTHS",
        "CERTIFICATIONS",
        "ADDITIONAL INFORMATION",
        "DECLARATION",
    ]

    return {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "linkedin": extract_linkedin(text),

        "cgpa": extract_cgpa(text),

        "skills": extract_skills(text),

        "education": extract_section(
            text,
            "EDUCATION",
            sections
        ),

        "projects": extract_section(
            text,
            "PROJECTS",
            sections
        ),

        "certifications": extract_section(
            text,
            "CERTIFICATIONS",
            sections
        ),

        "objective": extract_section(
            text,
            "OBJECTIVE",
            sections
        ),
    }