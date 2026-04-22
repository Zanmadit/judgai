import requests
from config import settings

def llama_complete(prompt, temperature=0.3, max_tokens=2048):
    payload = {
        "prompt": prompt,
        "temperature": temperature,
        "n_predict": max_tokens,
    }
    r = requests.post(settings.LLAMA_ENDPOINT, json=payload)
    return r.json()["content"]
