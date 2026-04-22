import json
from llm.llama_client import llama_complete
from llm.prompts import FILE_SELECTOR_PROMPT

def select_priority_files(readme, files):
    prompt = FILE_SELECTOR_PROMPT.format(
        readme=readme,
        files="\n".join(files)
    )
    response = llama_complete(prompt)
    return json.loads(response)
