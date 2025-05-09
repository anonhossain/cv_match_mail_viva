from typing import List
from fastapi import APIRouter, File, Form, UploadFile
import os
from fastapi.responses import JSONResponse
from files_uploader import save_candidate_files, save_hr_files, save_uploaded_files

# Initialize router
api = APIRouter()

@api.get("/hello")
def hello():
    return {"message": "Hello, Anon!"}

@api.post("/upload_files")
async def upload_files(pdf_file: UploadFile = File(...), jd_text: str = Form(...)):
    return await save_candidate_files(pdf_file, jd_text)

@api.post("/upload_HR_files")
async def upload_HR_files(pdf_file: List[UploadFile] = File(...), jd_text: str = Form(...)):
    return await save_hr_files(pdf_file, jd_text, is_hr=True)