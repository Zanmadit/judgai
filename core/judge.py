from llm.gemini_client import gemini_generate
from llm.prompts import JUDGE_PROMPT

def judge_project(claims, code, video_summary):
    prompt = JUDGE_PROMPT.format(
        claims=claims,
        code=code,
        video=video_summary
    )
    return gemini_generate(prompt, temperature=0.4)
