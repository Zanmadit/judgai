from google import genai
from config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

response = client.models.generate_content(
        model="model",
        config={
            "temperature": 0.7,
            "top_p": 0.95,
            "max_output_tokens": 2048,
            "response_mime_type": "application/json", # Pydantic schema -> JSON
        },
    )