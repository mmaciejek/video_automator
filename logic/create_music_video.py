import os
import random

from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip


def get_unique_filename(output_folder, base_filename):
    base_name, ext = os.path.splitext(base_filename)
    unique_filename = os.path.join(output_folder, f"{base_name}_music_video")
    num = 1
    while os.path.exists(f"{unique_filename}{num}.mp4"):
        num += 1
    return f"{unique_filename}{num}.mp4"


def resize_to_1080p(clip):
    return clip.resize(height=1080)


def make_music_video(song_file, clips_folder, output_folder, bpm, clip_length_beats=2):
    video_files = os.listdir(clips_folder)
    random.shuffle(video_files)

    beats_per_minute = bpm
    beats_per_second = beats_per_minute / 60
    clip_duration = clip_length_beats / beats_per_second

    clips = []
    for idx, video_file in enumerate(video_files):
        video_path = os.path.join(clips_folder, video_file)
        clip = VideoFileClip(video_path)
        original_clip_duration = clip.duration

        if idx == 0:
            adjusted_duration = original_clip_duration - 0.1
            clip = clip.subclip(0, adjusted_duration)
        else:
            # Adjust the duration of each clip to be exactly 2 beats
            num_beats = original_clip_duration * beats_per_second
            target_duration = num_beats / beats_per_second
            clip = clip.subclip(0, target_duration)

        # Resize the clip to 1080p
        clip = resize_to_1080p(clip)
        clips.append(clip)

    # Concatenate all the input_clips to create the final video
    final_clip = concatenate_videoclips(clips, method="compose")

    # Load the background music
    background_music = AudioFileClip(song_file)
    song_duration = background_music.duration

    # Set the audio of the final video with the background music
    final_clip = final_clip.set_audio(background_music)

    # Crop the final video to match the duration of the audio
    final_clip = final_clip.subclip(0, song_duration)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a unique filename for the output video
    base_filename = os.path.basename(song_file)
    output_file = get_unique_filename(output_folder, base_filename)

    # Save the final video with the unique filename and the audio merged
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

    # Close all the input_clips to release resources
    for clip in clips:
        clip.close()


if __name__ == "__main__":
    song_file = r"G:\Python\PROJEKT\SONGS\Z KONOPI 187.mp3"
    clips_folder = r"G:\Python\PROJEKT\CLIPS"
    output_folder = r"G:\Python\PROJEKT\OUTPUT"

    make_music_video(song_file, clips_folder, output_folder)
