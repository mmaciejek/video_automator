import os

import cv2


def delete_clips(clips_folder):
    for clip_file in os.listdir(clips_folder):
        clip_path = os.path.join(clips_folder, clip_file)
        cap = cv2.VideoCapture(clip_path)
        cap.release()  # Release the VideoCapture object
        os.remove(clip_path)  # Now you can safely delete the file


if __name__ == "__main__":
    # Example usage of export_clips method
    bpm = 30
