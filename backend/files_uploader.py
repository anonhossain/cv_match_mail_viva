import os
import shutil
from fastapi import UploadFile
#import env
from dotenv import load_dotenv

load_dotenv()

# Access variables from the .env file
CANDIDATE_CV_FILE = os.getenv('CANDIDATE_CV_FILE')
CANDIDATE_JD_FILE = os.getenv('CANDIDATE_JD_FILE')

# Make sure folders exist
os.makedirs(CANDIDATE_CV_FILE, exist_ok=True)
os.makedirs(CANDIDATE_JD_FILE, exist_ok=True)

async def save_uploaded_files(pdf_file: UploadFile, jd_text: str):
    # Save PDF
    pdf_path = os.path.join(CANDIDATE_CV_FILE, "resume.pdf")
    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(pdf_file.file, buffer)

    # Save JD text
    jd_path = os.path.join(CANDIDATE_JD_FILE, "jd.txt")
    with open(jd_path, "w", encoding="utf-8") as f:
        f.write(jd_text)

    return {"message": "Files uploaded successfully"}
