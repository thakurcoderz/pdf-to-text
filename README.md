# PDF to Text Web App

A simple web application built with FastAPI that lets you upload a PDF, extracts its text, and allows you to download the resulting text file. The UI is styled with Tailwind CSS for a modern look.

## Features
- Upload a PDF file via a web form
- Extracts all text from the PDF
- Download the extracted text as a `.txt` file
- Clean, responsive UI with Tailwind CSS

## Requirements
- Python 3.8+
- See `requirements.txt` for Python dependencies

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/thakurcoderz/pdf-to-text.git
   cd pdf-to-text
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your browser and go to [http://localhost:8000](http://localhost:8000)
3. Upload a PDF, extract its text, and download the result!

## Project Structure
```
├── app.py                # Main FastAPI app
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates (Tailwind CSS)
│   ├── upload.html
│   └── result.html
├── uploads/              # Uploaded PDF files (auto-created)
├── texts/                # Extracted text files (auto-created)
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Notes
- Uploaded PDFs and extracted text files are stored in `uploads/` and `texts/` respectively.
- For production, consider cleaning up these folders regularly.

## License
MIT 