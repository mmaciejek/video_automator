# G:\Python\PROJEKT\package\get_song_bpm.py
from mutagen.mp3 import MP3


def get_bpm_from_mp3_name(mp3_filename):
    try:
        bpm = int(mp3_filename[-7:-4])  # Extract the last 2 digits as BPM (assuming the format is "songname_bpm.mp3")
        return bpm
    except ValueError:
        try:
            bpm = int(
                mp3_filename[-6:-4])  # Extract the last 3 digits as BPM (assuming the format is "songname_bpm.mp3")
            return bpm
        except ValueError:
            print(f"Invalid filename format for {mp3_filename}. BPM not found.")
            return None


def get_song_duration(mp3_filename):
    try:
        audio = MP3(mp3_filename)
        duration = audio.info.length  # Duration in seconds
        return duration
    except Exception as e:
        print(f"Error getting duration for {mp3_filename}: {str(e)}")
        return None


if __name__ == "__main__":
    # Example usage of get_bpm_from_mp3_name function with sample filenames
    mp3_filename1 = "4twistedddmind_tag156.mp3"
    mp3_filename2 = "OHSHIIT160_tag160.mp3"

    bpm1 = get_bpm_from_mp3_name(mp3_filename1)
    if bpm1 is not None:
        print(f"The BPM of '{mp3_filename1}' is {bpm1}.")

    bpm2 = get_bpm_from_mp3_name(mp3_filename2)
    if bpm2 is not None:
        print(f"The BPM of '{mp3_filename2}' is {bpm2}.")
