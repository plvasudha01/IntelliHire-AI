from pathlib import Path

from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)

    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)

    return "\n".join(pages).strip()


def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a DOCX file."""
    document = Document(file_path)

    paragraphs = [
        paragraph.text.strip()
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n".join(paragraphs).strip()


def extract_text(file_path: str) -> str:
    """Extract text from a supported resume file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    if extension == ".docx":
        return extract_text_from_docx(file_path)

    raise ValueError(
        "Unsupported file format. Please use PDF or DOCX."
    )