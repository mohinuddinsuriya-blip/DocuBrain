from fastapi import FastAPI, UploadFile
from ingestion.pdf_reader import read_pdf
from ingestion.cleaner import clean_text
from ingestion.chunker import chunk_text
from ai_engine.stakeholder_detector import detect_stakeholders
from ai_engine.timeline_extractor import extract_dates

app = FastAPI()

@app.post("/upload")

async def upload(file: UploadFile):

    text = read_pdf(file.file)

    text = clean_text(text)

    chunks = chunk_text(text)

    stakeholders = detect_stakeholders(text)

    timeline = extract_dates(text)

    return {
        "chunks": chunks[:5],
        "stakeholders": stakeholders,
        "timeline": timeline
    }