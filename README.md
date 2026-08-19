# IntelliHire-AI

AI-powered resume screening and candidate ranking system that evaluates resumes against job descriptions and generates an ATS compatibility score.

## Features

- Upload and analyze resumes in PDF format
- Compare resumes with different job descriptions
- Extract relevant information from resumes
- Generate an ATS compatibility score
- Identify matching skills
- Identify missing skills
- Display candidate analysis through a Flask web interface

## Tech Stack

- Python
- Flask
- Natural Language Processing (NLP)
- Scikit-learn
- HTML
- CSS
- PDF text extraction

## How It Works

1. Upload a candidate's resume.
2. Provide the job description.
3. The system extracts and cleans the resume text.
4. Resume content is compared with the job description.
5. Relevant skills and keywords are identified.
6. An ATS compatibility score is generated.
7. The results are displayed through the web interface.

## Project Structure

```text
IntelliHire-AI/
│
├── app/
│   ├── app.py
│   └── templates/
│
├── src/
│   ├── ats_scorer.py
│   ├── cleaner.py
│   ├── extractor.py
│   ├── main.py
│   └── parser.py
│
├── data/
│   └── job_descriptions/
│
├── requirements.txt
├── .gitignore
└── README.md
