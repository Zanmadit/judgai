from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os, shutil
from config import settings

from core.github_loader import load_repo, get_readme, get_file_list
from core.repo_analyzer import select_priority_files
from core.code_reader import read_files
from core.video_analyzer import analyze_video
from core.judge import judge_project

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit")
async def submit(
    team_name: str = Form(...),
    github_url: str = Form(...),
    video: UploadFile = File(...)
):
    team_dir = f"{settings.UPLOAD_DIR}/{team_name}"
    os.makedirs(team_dir, exist_ok=True)

    video_path = f"{team_dir}/{video.filename}"
    with open(video_path, "wb") as f:
        shutil.copyfileobj(video.file, f)

    repo = load_repo(github_url)
    readme = get_readme(repo)
    files = get_file_list(repo)

    priority_files = select_priority_files(readme, files)
    code = read_files(repo, priority_files)

    video_data = analyze_video(video_path, team_dir)

    verdict = judge_project(
        claims=readme,
        code=code,
        video_summary=video_data
    )

    return {
        "team": team_name,
        "files_checked": priority_files,
        "verdict": verdict
    }
