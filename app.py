import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_helper import analyze_resume
from utils.prompt_template import PROMPT


# Page Configuration
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄"
)

# App Title
st.title("📄 AI Resume Screening System")

# Job Description Input
job_description = st.text_area(
    "Paste Job Description"
)

# Resume Upload
uploaded_resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# Analyze Button
if st.button("Analyze Resume"):

    if not job_description:
        st.warning("Please enter a Job Description.")

    elif not uploaded_resume:
        st.warning("Please upload a resume.")

    else:

        # Extract text from PDF
        resume_text = extract_text_from_pdf(
            uploaded_resume
        )

        # Build prompt
        prompt = PROMPT.format(
    jd=job_description,
    resume=resume_text
)

        # Show loading indicator
        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(
                prompt
            )

        # Display Result
        st.subheader("Analysis Result")

        st.write(result)