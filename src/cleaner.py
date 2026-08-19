import re
def clean_resume_text(text: str) -> str:
    """Clean common PDF extraction artifacts from resume text."""

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove excessive spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Fix common split words caused by PDF extraction
    replacements = {
        "V ASUDHA": "VASUDHA",
        "EDUCA TION": "EDUCATION",
        "CER TIFICA TIONS": "CERTIFICATIONS",
        "DECLARA TION": "DECLARATION",
        "ADDITIONAL INFORMA TION": "ADDITIONAL INFORMATION",
        "T ools": "Tools",
        "W omen": "Women",
        "Infor mation": "Information",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Add a space between a word and CGPA when PDF extraction joins them
    text = re.sub(r"([A-Za-z])CGPA", r"\1 CGPA", text)

    # Remove spaces at the beginning/end of each line
    lines = [line.strip() for line in text.split("\n")]

    # Remove empty lines repeated multiple times
    cleaned_lines = []
    previous_empty = False

    for line in lines:
        if not line:
            if not previous_empty:
                cleaned_lines.append(line)
            previous_empty = True
        else:
            cleaned_lines.append(line)
            previous_empty = False

    return "\n".join(cleaned_lines).strip()