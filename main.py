import os
import time

from mutagen.mp3 import MP3

from data.download_videos_youtube import download_videos_from_file
from logic.create_music_video import make_music_video
from logic.delete_clips import delete_clips
from logic.export_clips_from_videos import export_clips
from logic.get_song_bpm import get_bpm_from_mp3_name
from data.reencoding import reencode_videos


def main(clip_length_beats=2):

    file_path = r"C:\Users\chaci\Desktop\PROJEKT\data\info_about_youtube_viedos\links_youtube_videos.txt"

    video_folder = r"C:\Users\chaci\Desktop\PROJEKT\data\input_videos"
    encoded_videos = r"C:\Users\chaci\Desktop\PROJEKT\data\input_reencoded_videos"

    clips_folder = r"C:\Users\chaci\Desktop\PROJEKT\data\input_clips"
    output_folder = r"C:\Users\chaci\Desktop\PROJEKT\data\output_music_videos"

    # download_videos_from_file(file_path, video_folder)
    reencode_videos(video_folder, encoded_videos)

    # Get BPM for each song in the SONGS folder
    songs_folder = r"C:\Users\chaci\Desktop\PROJEKT\data\input_songs"
    for song_file in os.listdir(songs_folder):
        if song_file.endswith('.mp3'):
            # Get BPM
            bpm = get_bpm_from_mp3_name(song_file)
            if bpm is not None:
                print(f"The BPM of '{song_file}' is {bpm}.")

            # Get song duration
            song_path = os.path.join(songs_folder, song_file)
            audio = MP3(song_path)
            song_duration = audio.info.length

            export_clips(bpm, clips_folder, song_duration, video_folder, clip_length_beats)
            time.sleep(2)

            make_music_video(song_path, clips_folder, output_folder, bpm, clip_length_beats)
            time.sleep(2)
            delete_clips(clips_folder)


if __name__ == "__main__":
    main(2)
