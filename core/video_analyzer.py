from utils.video import extract_frames
from utils.audio import extract_audio

def analyze_video(video_path, out_dir):
    frames = extract_frames(video_path, f"{out_dir}/frames")
    audio = extract_audio(video_path, f"{out_dir}/audio.wav")

    return {
        "frames": frames[:5],
        "audio": audio
    }
