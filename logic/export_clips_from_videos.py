import os
import random

from moviepy.video.io.VideoFileClip import VideoFileClip

from data.download_videos_youtube import download_videos_from_file


def export_clips(song_bpm, clips_folder, song_duration, video_folder, clip_length_beats=2):
    beats_per_minute = song_bpm
    beats_per_second = beats_per_minute / 60
    clip_duration = clip_length_beats / beats_per_second
    total_clips_required = int(song_duration / clip_duration)

    if not os.path.exists(clips_folder):
        os.makedirs(clips_folder)

    video_files = [video_file for video_file in os.listdir(video_folder) if video_file.endswith('.mp4')]

    total_exported_duration = 0  # To track the total duration of exported input_clips

    for idx, video_file in enumerate(video_files):
        video_path = os.path.join(video_folder, video_file)
        video_title = video_file[:-4]

        video_clip = VideoFileClip(video_path)
        num_clips_from_video = total_clips_required // len(video_files) + 1

        for clip_idx in range(num_clips_from_video):
            max_start_time = video_clip.duration - clip_duration
            clip_start_time = random.uniform(0, max_start_time)

            # Ensure that the clip_end_time does not exceed the video duration
            clip_end_time = min(clip_start_time + clip_duration, video_clip.duration)

            clip = video_clip.subclip(clip_start_time, clip_end_time)

            clip_file_path = os.path.join(clips_folder, f"clip_{idx + 1}_{clip_idx + 1}.mp4")

            # Specify the codec parameter for writing the clip
            clip.write_videofile(clip_file_path, codec='libx264', audio=False)

            print(f"Exported clip {idx + 1}_{clip_idx + 1} from {video_title}")

            total_exported_duration += clip_end_time - clip_start_time

        video_clip.close()

    # Check if the total exported duration is greater than the song duration
    if total_exported_duration < song_duration:
        print("Warning: Total exported input_clips duration is less than the song duration.")


if __name__ == "__main__":
    file_path = "G:\\Python\\PROJEKT\\links_youtube_videos.txt"
    video_folder = "G:\\Python\\PROJEKT\\VIDEOS"
    clips_folder = "G:\\Python\\PROJEKT\\input_clips"
    song_bpm = 120
    song_duration = 240  # In seconds (e.g., 4 minutes)

    download_videos_from_file(file_path, video_folder)
    export_clips(song_bpm, clips_folder, song_duration, video_folder)

    print("Done exporting input_clips")
