import json
from llm.gemini_client import gemini_generate
from llm.prompts import FILE_SELECTOR_PROMPT

def select_priority_files(readme, files):
    prompt = FILE_SELECTOR_PROMPT.format(
        readme=readme,
        files="\n".join(files)
    )
    response = gemini_generate(prompt)
    return json.loads(response)
