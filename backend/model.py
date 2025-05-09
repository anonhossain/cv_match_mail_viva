
import os
import shutil
import google.generativeai as genai
import PyPDF2 as pdf
import pdfplumber
from prompt import *
#import env
from dotenv import load_dotenv

load_dotenv()

# Access variables from the .env file
CANDIDATE_CV_FILE = os.getenv('CANDIDATE_CV_FILE')
CANDIDATE_JD_FILE = os.getenv('CANDIDATE_JD_FILE')

HR_CV_FILES = os.getenv('HR_CV_FILES')
HR_JD_FILE = os.getenv('HR_JD_FILE')

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
MODEL = os.getenv('MODEL')

# Configure your API key from the .env file
genai.configure(api_key=GOOGLE_API_KEY)

class Model:
    @staticmethod
    def get_gemini_response(prompt):
        model_instance = genai.GenerativeModel(MODEL)
        response = model_instance.generate_content(prompt)
        return response.text

    @staticmethod
    def extract_text_from_pdf(resume_file_path):
        resume_file_path = os.path.join(resume_file_path, "resume.pdf")
        with open(resume_file_path, 'rb') as file:
            reader = pdf.PdfReader(file)
            text = ""
            for page in range(len(reader.pages)):
                page_text = reader.pages[page].extract_text()
                text += str(page_text)
        return text

    @staticmethod
    def load_job_description(job_description_file_path):
        jd_path = os.path.join(job_description_file_path, "jd.txt")
        with open(jd_path,'r') as file:
            return file.read()

    @staticmethod
    def process_resume(action: str):
        if action not in ["match", "skills_suggestion", "question_generation", "project_suggestion", "draft_cover_letter", "draft_email"]:
            return {"error": "Invalid action. Choose 'match', 'skills_suggestion', 'question_generation', 'project_suggestion', 'draft_cover_letter', or 'draft_email'."}
        
        job_desc = Model.load_job_description(CANDIDATE_JD_FILE)
        resume_text = Model.extract_text_from_pdf(CANDIDATE_CV_FILE)
        
        # Choose the appropriate prompt function based on the action
        if action == "match":
            prompt = match_prompt(job_desc, resume_text)
        elif action == "skills_suggestion":
            prompt = skills_suggestion_prompt(job_desc, resume_text)
        elif action == "question_generation":
            prompt = question_generation_prompt(job_desc, resume_text)
        elif action == "project_suggestion":
            prompt = project_suggestion_prompt(job_desc, resume_text)
        elif action == "draft_cover_letter":
            prompt = draft_cover_letter_prompt(job_desc, resume_text)
        elif action == "draft_email":
            prompt = draft_email_prompt(job_desc, resume_text)
        response_text = Model.get_gemini_response(prompt)
        return {"result": response_text}

class ModelHR:

    @staticmethod
    def extract_text_from_pdf(resume_file_path):
        resume_file_path = os.path.join(resume_file_path, "resume.pdf")
        with open(resume_file_path, 'rb') as file:
            reader = pdf.PdfReader(file)
            text = ""
            for page in range(len(reader.pages)):
                page_text = reader.pages[page].extract_text()
                text += str(page_text)
        return text
    
    @staticmethod
    def get_gemini_response(prompt):
        """Get response from Gemini AI."""
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text

    @staticmethod
    def extract_pdf_text(file_path):
        """Extract text from PDF file."""
        with pdfplumber.open(file_path) as pdf:
            return "".join(page.extract_text() for page in pdf.pages)
    
    @staticmethod
    def hr_resume_sort():
       
        HR_job_desc = Model.load_job_description(HR_JD_FILE)

        pdf_files = [
            file for file in os.listdir(HR_CV_FILES)
            if file.lower().endswith('.pdf')
        ]
        percentage_mapping = {}
        for pdf_file in pdf_files:
            pdf_path = os.path.join(HR_CV_FILES, pdf_file)
            HR_resume_text = ModelHR.extract_pdf_text(pdf_path)
            prompt = hr_sort_prompt(HR_job_desc, HR_resume_text)
            response =ModelHR.get_gemini_response(prompt).strip()

            try:
                percentage = int(response.replace("\n", "").strip())
            except ValueError:
                percentage = 0 
            
            percentage_mapping[pdf_file] = percentage
        percentage_mapping = dict(sorted(percentage_mapping.items(), key=lambda item: item[1], reverse=True))
        return percentage_mapping