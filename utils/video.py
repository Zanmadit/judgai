import cv2, os

def extract_frames(video_path, out_dir, every_n=30):
    os.makedirs(out_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)

    frames = []
    i = 0
    idx = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i % every_n == 0:
            path = os.path.join(out_dir, f"frame_{idx}.jpg")
            cv2.imwrite(path, frame)
            frames.append(path)
            idx += 1
        i += 1

    cap.release()
    return frames
