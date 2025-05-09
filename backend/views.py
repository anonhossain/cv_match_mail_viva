from typing import List
from fastapi import APIRouter, File, Form, UploadFile
import os
from fastapi.responses import JSONResponse
from model import Model, ModelHR
from files_uploader import save_candidate_files, save_hr_files


# Initialize router
api = APIRouter()

@api.get("/hello")
def hello():
    return {"message": "Hello, Anon!"}

@api.post("/upload_candidate_files")
async def upload_files(pdf_file: UploadFile = File(...), jd_text: str = Form(...)):
    return await save_candidate_files(pdf_file, jd_text)

@api.post("/upload_HR_files")
async def upload_HR_files(pdf_file: List[UploadFile] = File(...), jd_text: str = Form(...)):
    return await save_hr_files(pdf_file, jd_text)

@api.post("/process_candidate_resume")
async def process_resume(action: str = Form(...)):
    return Model.process_resume(action)

@api.post("/process_HR_resume_sort")
async def process_HR_resume_sort():
    return ModelHR.hr_resume_sort()