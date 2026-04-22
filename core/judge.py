from llm.llama_client import llama_complete
from llm.prompts import JUDGE_PROMPT

def judge_project(claims, code, video_summary):
    prompt = JUDGE_PROMPT.format(
        claims=claims,
        code=code,
        video=video_summary
    )
    return llama_complete(prompt, temperature=0.4)
