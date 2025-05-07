from fastapi import APIRouter, File, Form, UploadFile
import os
from fastapi.responses import JSONResponse
from files_uploader import save_uploaded_files

# Initialize router
api = APIRouter()

@api.get("/hello")
def hello():
    return {"message": "Hello, Anon!"}

@api.post("/upload_files")
async def upload_files(pdf_file: UploadFile = File(...), jd_text: str = Form(...)):
    return await save_uploaded_files(pdf_file, jd_text)