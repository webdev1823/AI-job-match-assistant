import streamlit as st

from llm import ask_llm
from pdf_utils import extract_pdf_text
from prompts import TASKS, build_prompt

st.set_page_config(page_title="AI Job Match Assistant")
st.title("AI Job Match Assistant")
st.caption("Upload or paste your resume, add a job description, then pick a task.")

task = st.selectbox("What do you need?", list(TASKS))

uploaded = st.file_uploader("Upload your resume (PDF)", type="pdf")
pasted = st.text_area("...or paste your resume text", height=200)
resume = pasted
if uploaded is not None:
    try:
        resume = extract_pdf_text(uploaded.getvalue())
        st.success(f"Read {len(resume)} characters from {uploaded.name}")
    except Exception as e:  # unreadable or scanned PDF -> fall back to pasted text
        st.warning(f"Could not read the PDF: {e}")

jd = st.text_area("Job description", height=200)

if st.button("Generate"):
    try:
        prompt = build_prompt(task, resume, jd)
    except ValueError as e:
        st.warning(str(e))
    else:
        with st.spinner("Thinking..."):
            try:
                st.markdown(ask_llm(prompt))
            except Exception as e:  # e.g. missing API key / network error
                st.error(f"LLM call failed: {e}")
