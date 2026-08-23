# IntelliHire-AI

AI-powered resume screening and candidate ranking system that evaluates resumes against job descriptions and generates an ATS compatibility score.

## Features

* Upload and analyze resumes in PDF format
* Compare resumes with different job descriptions
* Extract relevant information from resumes
* Generate an ATS compatibility score
* Identify matching skills
* Identify missing skills
* Display candidate analysis through a Flask web interface

## Tech Stack

* Python
* Flask
* Natural Language Processing (NLP)
* Scikit-learn
* HTML
* CSS
* PDF text extraction

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/plvasudha01/IntelliHire-AI.git
cd IntelliHire-AI
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

### 1. Start the application

```bash
python app/app.py
```

### 2. Open the web application

Open the local Flask URL shown in the terminal, typically:

```text
http://127.0.0.1:5000
```

### 3. Analyze a resume

1. Upload a candidate resume in PDF format.
2. Provide the job description.
3. Submit the analysis.
4. Review the ATS compatibility score.
5. Review matching and missing skills.
6. Review the candidate analysis results.

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
├── LICENSE
├── .gitignore
└── README.md
```

## License

This project is licensed under the MIT License.
