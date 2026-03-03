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

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze_resume")
async def submit_resume(
    name: str = Form(...),
    gmail: str = Form(...),
    phone: str = Form(...),
    resume: UploadFile = File(...)
):
    if resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    file_bytes = await resume.read()

    files = {
        "resume": (resume.filename, file_bytes, resume.content_type)
    }

    data = {
        "name": name,
        "gmail": gmail,
        "phone": phone
    }

    try:
        requests.post(webhook_url, data=data, files=files, timeout=5)
    except:
        pass  
    return {
        "status": "success", 
        "message": "Resume submitted successfully. You will receive an email shortly."
    }