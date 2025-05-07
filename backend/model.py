# backend/model.py

import os
import shutil
import google.generativeai as genai
import PyPDF2 as pdf
#import env
from dotenv import load_dotenv

load_dotenv()

# Access variables from the .env file
CV_FILE = os.getenv('CV_FILE')
JD_FILE = os.getenv('JD_FILE')

# Configure your API key from the .env file
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

class Model:
    @staticmethod
    def get_gemini_response(prompt):
        model_instance = genai.GenerativeModel(os.getenv('MODEL'))
        response = model_instance.generate_content(prompt)
        return response.text

    @staticmethod
    def extract_text_from_pdf(resume_file_path):
        with open(resume_file_path, 'rb') as file:
            reader = pdf.PdfReader(file)
            text = ""
            for page in range(len(reader.pages)):
                page_text = reader.pages[page].extract_text()
                text += str(page_text)
        return text

    @staticmethod
    def load_job_description(job_description_file_path):
        with open(job_description_file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def process_resume(action: str):
        if action not in ["match", "skills_suggestion", "question_generation", "project_suggestion", ]:
            return {"error": "Invalid action. Choose 'match', 'skills_suggestion', 'question_generation', 'project_suggestion', "}
        
        job_desc = Model.load_job_description(JD_FILE)
        resume_text = Model.extract_text_from_pdf(CV_FILE)
        
        def match_prompt(job_desc, resume_text):
            return f"""
            Go through the job description and resume and provide a score from 0 to 100 based on how well the resume matches the job description.
            just provide the score and nothing else.

            Job Description:
            {job_desc}

            Resume:
            {resume_text}
            """ 
            
        def skills_suggestion_prompt(job_desc, resume_text):
            return f"""
            Go through the job description and resume and provide a list of skills that are missing in the resume but are required for the job.
            Job Description:
            {job_desc}

            Resume:
            {resume_text}
            """
        def question_generation_prompt(job_desc, resume_text):
            return f"""
            Go through the job description and resume and provide a list of questions that can be asked to the candidate based on the resume and job description.

            Job Description:
            {job_desc}

            Resume:
            {resume_text}
            """
        
        def project_suggestion_prompt(job_desc, resume_text):
            return f"""
            Go through the job description and resume and provide a list of projects that can be suggested to the candidate based on the resume and job description.

            Job Description:
            {job_desc}

            Resume:
            {resume_text}
            """
        
        # Choose the appropriate prompt function based on the action
        if action == "match":
            prompt = match_prompt(job_desc, resume_text)
        elif action == "skills_suggestion":
            prompt = skills_suggestion_prompt(job_desc, resume_text)
        elif action == "question_generation":
            prompt = question_generation_prompt(job_desc, resume_text)
        elif action == "project_suggestion":
            prompt = project_suggestion_prompt(job_desc, resume_text)
        response_text = Model.get_gemini_response(prompt)
        return {"result": response_text}
