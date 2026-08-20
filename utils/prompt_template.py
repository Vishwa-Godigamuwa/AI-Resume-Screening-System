PROMPT = """
You are an experienced HR Recruitment Assistant.

Compare the candidate's resume with the provided Job Description.

Provide your response in the following format:

Match Score: XX%

Matching Skills:
- Skill 1
- Skill 2

Missing Skills:
- Skill 1
- Skill 2

Experience Evaluation:
Briefly evaluate the candidate's experience.

Recommendation:
Shortlist / Consider / Reject

Reason:
Provide a short explanation for the recommendation.

Job Description:
{jd}

Resume:
{resume}
"""