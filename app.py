from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import shutil, os
from utils import extract_video_frames
from google import genai
import openai
from config import settings

UPLOAD_FOLDER = "project_upload"

client = openai.OpenAI(
    api_key=settings.GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

app = FastAPI()

@app.post("/upload_project")
async def upload_project(
    readme: UploadFile = File(...),
    video: UploadFile = File(...),
    src_file: UploadFile = File(...)
):
    project_dir = UPLOAD_FOLDER
    os.makedirs(project_dir, exist_ok=True)

    readme_path = os.path.join(project_dir, readme.filename)
    with open(readme_path, "wb") as f:
        shutil.copyfileobj(readme.file, f)
    
    video_path = os.path.join(project_dir, video.filename)
    with open(video_path, "wb") as f:
        shutil.copyfileobj(video.file, f)

    src_path = os.path.join(project_dir, src_file.filename)
    with open(src_path, "wb") as f:
        shutil.copyfileobj(src_file.file, f)

    frames_dir = os.path.join(project_dir, "frames")
    frames = extract_video_frames(video_path, frames_dir)

    return JSONResponse({
        "message": "Files upload and processed",
        "frames": frames
    })


@app.post("/evaulate_project")
async def evaluate_project(project_name: str = Form(...)):
    project_dir = os.path.join(UPLOAD_FOLDER)
    readme_path = os.path.join(project_dir, "README.md")

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_text = f.read()
    
    response = client.chat.completions.create(
        model="gemini-3-pro-preview",
        messages=[
            {"role": "system", "content": "You are AI Hackaton judge"},
            {"role": "user", "content": f"Evaluate this project: \n{readme_text}"}
        ]
    )


    gemini_output = response.choices[0].message.content

    return JSONResponse({
        "gemini_response": gemini_output
    })
