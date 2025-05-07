def match_prompt(job_desc, resume_text):
    return f"""
    Compare the job description and the resume and rate the match between them on a scale of 1-100.
    just give the score and no other explanation.

    Job Description:
    {job_desc}

    Resume:
    {resume_text}
    """

def skills_suggestion_prompt(job_desc, resume_text):
    return f"""
     Go through the job description thoroughly. Read that nicely and understand it. Provide the skills that are required for the job.

    Job Description:
    {job_desc}

    Resume:
    {resume_text}
    """

def question_generation_prompt(job_desc, resume_text):
    return f"""
    Go through the job description thoroughly. Read that nicely and understand it. Provide 5-10 questions that can be asked to the candidate based on the job description.

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