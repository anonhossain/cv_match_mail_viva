
def match_prompt(job_desc, resume_text):
    return f"""
    Your task is to match the resume with the job description and provide a score from 0 to 100 based on the match.
    Just give the score, no other text.
    Here watch the job description and resume carefully and then give the score.
    The score should be based on the skills, experience, and projects mentioned in the resume. 
    See the skills in job description and resume and then give the score.

    Job Description:
    {job_desc}

    Resume:
    {resume_text}
    """

def skills_suggestion_prompt(job_desc, resume_text):
    return f"""
    Your task is to provide suggestions for improving the resume based on the job description. 
    At first go through the job description thoroughly. Read that nicely and understand it and identify the skills required for the job.
    Then go through the resume of the candidate. Read that nicely and understand it and identify the skills mentioned in the resume.
    Identify the missing skills.
    Focus on the skills and experience that are relevant to the job description.
    Tell how the Skills can be earned or improved.
    Also highlight prerequisite required for that skills that are not mentioned in the resume.

    Job Description:
    {job_desc}

    Resume:
    {resume_text}
    """

def question_generation_prompt(job_desc, resume_text):
    return f"""
    You are a Highly Expert HR. Your main task is to go through the job description thoroughly. Read that nicely and understand it.
    Then go through the resume of the candidate. Read that nicely and understand it.
    Then you have to generate the questions that could be asked based on the skills, job role, previous experience, and projects mentioned in the CV.
    Also, generate technical questions from CV projects and experience.
    The questions must be standard and should be related to the job description and the skills mentioned in the CV.
    Also ask some advance-level questions based on skills and projects which relate to the job description.
    No need to ask general questions. The total number of questions will be between 10-15.
    As it is for candidate, also provide the answer to the questions.
    The answer should be in easy English and should be understandable by the candidate.

    Job Description:
    {job_desc}

    Resume:
    {resume_text}
    """

def project_suggestion_prompt(job_desc, resume_text):
    return f"""
    You are a Highly Expert HR. Your main task is to go through the job description thoroughly. Read that nicely and understand it.
    Then go through the resume of the candidate. Read that nicely and understand it.
    Then suggest 4-5 projects. Projects should satisfy most of the skills mentioned in the job description.
    Also write how the projects can be done and what language and framework can be used.

    Job Description:
    {job_desc}

    Resume:
    {resume_text}
    """

def draft_cover_letter_prompt(job_desc, resume_text):
    return f"""
    You are a Highly Expert HR. Your main task is to go through the job description thoroughly. Read that nicely and understand it.
    Then go through the resume of the candidate. Read that nicely and understand it.
    Then you have to generate the cover letter for the candidate based on the skills, job role, previous experience, and projects mentioned in the CV.
    The cover letter must be standard and in easy English.

    Job Description:
    {job_desc}

    Resume:
    {resume_text}
    """

def draft_email_prompt(job_desc, resume_text):
    return f"""
    Go through the job description thoroughly. Read that nicely and understand it.
    Then go through the resume of the candidate. Read that nicely and understand it.
    Then you have to generate the email for the candidate based on the skills, job role, previous experience, and projects mentioned in the CV.
    The email must be standard and in easy English.

    Job Description:
    {job_desc}

    Resume:
    {resume_text}
    """


def hr_sort_prompt (HR_job_desc,HR_resume_text):
    return f"""
    You are an expert in the field of HR. You have been asked to evaluate a candidate for a job position. The job description and the resume of the candidate are provided below. Your task is to show the percentage match between the job description and CV in one line. Just write the number without using %.
    Job Description:
    {HR_job_desc}

    Resume:
    {HR_resume_text}
    """
    
def generate_questions_prompt (jd_text,resume_text):
    
    return f"""
    You are a Highly Expert HR. Your main task is to go through the job description throughly. Read that nicely and understand that nicely. Then go through the resume of the candidate. Read that nicely and understand that nicely. Then you have to generate the questions that could be asked based on the skills, job role, previous experience, and projects mentioned in the CV. Also, generate technical questions from CV projects and experience. The Question must be of high Standard and should be related to the job role and the skills mentioned in the CV. Also ask some Advance level questions based on Skills and project which relate to the job description. No need to ask general questions. The total number question will be between 10-15

    Job Description:
    {jd_text}

    Resume:
    {resume_text}
    """