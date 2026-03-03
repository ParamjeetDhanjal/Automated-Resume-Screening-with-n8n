from fastapi import FastAPI, Form, UploadFile, File, HTTPException,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = FastAPI(title="Resume Intake API")

webhook_url = os.getenv("WEBHOOK_URL")

templates = Jinja2Templates(directory="templates")

@app.post("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze_resume")
async def submit_resume(
    name: str = Form(...),
    gmail: str = Form(...),
    phone: str = Form(...),
    resume: UploadFile = File(...)
):
    # Validate file type
    if resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    # Read file bytes
    file_bytes = await resume.read()

    # Prepare multipart form data for n8n
    files = {
        "resume": (resume.filename, file_bytes, resume.content_type)
    }

    data = {
        "name": name,
        "gmail": gmail,
        "phone": phone
    }

    try:
        response = requests.post(webhook_url, data=data, files=files, timeout=60)
        response.raise_for_status()

        # Handle empty or non-JSON response from n8n
        if not response.text or response.text.strip() == "":
            return {"status": "success", "message": "Resume submitted successfully. You will receive an email shortly."}

        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"status": "success", "message": "Resume submitted successfully. You will receive an email shortly."}

    except requests.exceptions.Timeout:
        return {"status": "success", "message": "Resume is being processed. You will receive an email shortly."}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))