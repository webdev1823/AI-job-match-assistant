# AI Job Match Assistant

A small GenAI web app: paste a resume and a job description, then get a match analysis (score, matching and
missing skills, improvements), a tailored summary, or a short cover letter from an LLM.

**Stack:** Python, Streamlit, LLM API (Google Gemini, free tier), pypdf, prompt engineering, Pytest

## Run
```bash
python -m venv venv && source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
export GEMINI_API_KEY=your_key                        # Windows: set GEMINI_API_KEY=your_key
streamlit run app.py
pytest -q
```

## Files
- `prompts.py` - prompt templates + input validation
- `llm.py` - LLM API call
- `app.py` - Streamlit UI (resume PDF upload or pasted text)
- `pdf_utils.py` - extracts text from an uploaded PDF
