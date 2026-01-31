import os
import cv2

def extract_video_frames(video_path, output_idr, fps=1):
    if not os.path.exists(output_idr):
        os.makedirs(output_idr)

    cap = cv2.VideoCapture(video_path)
    count = 0
    sec = 0
    success, image = cap.read()

    while success:
        if int(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000) == sec:
            frame_path = os.path.join(output_idr, f"frame_{count:03d}.jpg")
            cv2.imwrite(frame_path, image)
            count += 1
            sec += 1
        success, image = cap.read()
    cap.release()
    return [os.path.join(output_idr, f) for f in os.listdir(output_idr)]