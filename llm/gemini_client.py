from google import genai
from config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def gemini_generate(prompt: str, temperature=0.5, max_tokens=4096):
    response = client.models.generate_content(
        model="gemini-3-pro",  
        contents=prompt,
        config={
            "temperature": temperature,
            "max_output_tokens": max_tokens,
        }
    )
    return response.text
