import ffmpeg

def extract_audio(video_path, audio_path):
    (
        ffmpeg
        .input(video_path)
        .output(audio_path, ac=1, ar='16k')
        .overwrite_output()
        .run()
    )
    return audio_path
