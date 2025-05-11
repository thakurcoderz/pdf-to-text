import os
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from PyPDF2 import PdfReader

app = FastAPI()
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
TEXT_DIR = "texts"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(TEXT_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
def upload_pdf(request: Request, file: UploadFile = File(...)):
    # Save uploaded PDF
    pdf_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(pdf_path, "wb") as f:
        f.write(file.file.read())
    # Extract text
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    # Save text file
    base_name = os.path.splitext(file.filename)[0]
    text_filename = f"{base_name}.txt"
    text_path = os.path.join(TEXT_DIR, text_filename)
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Show download link
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "text_filename": text_filename}
    )

@app.get("/download/{text_filename}")
def download_text(text_filename: str):
    text_path = os.path.join(TEXT_DIR, text_filename)
    return FileResponse(text_path, media_type="text/plain", filename=text_filename) 