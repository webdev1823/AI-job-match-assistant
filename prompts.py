"""Prompt templates (prompt engineering) for the three assistant tasks."""

MIN_CHARS = 50

TASKS = {
    "Match analysis": (
        "Compare the RESUME with the JOB DESCRIPTION. Give: (1) a match score out of 100, "
        "(2) skills that match, (3) missing skills or keywords, (4) 3 specific improvements to the resume. "
        "Only use facts present in the resume; never invent experience."
    ),
    "Rewrite summary": (
        "Write a 3-4 line professional summary for the RESUME that is tailored to the JOB DESCRIPTION. "
        "Only use facts present in the resume; never invent experience."
    ),
    "Cover letter": (
        "Write a short, professional cover letter (under 200 words) for the JOB DESCRIPTION using only "
        "facts present in the RESUME."
    ),
}


def validate_inputs(resume: str, jd: str) -> None:
    if len(resume.strip()) < MIN_CHARS or len(jd.strip()) < MIN_CHARS:
        raise ValueError(f"Please paste at least {MIN_CHARS} characters for both the resume and the job description.")


def build_prompt(task: str, resume: str, jd: str) -> str:
    if task not in TASKS:
        raise ValueError(f"Unknown task: {task}")
    validate_inputs(resume, jd)
    return f"{TASKS[task]}\n\nRESUME:\n{resume.strip()}\n\nJOB DESCRIPTION:\n{jd.strip()}"
