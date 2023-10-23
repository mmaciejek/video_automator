import os
import shutil
import subprocess

input_folder = r'C:\Users\chaci\Desktop\PROJEKT\data\input_songs'
output_folder = r'C:\Users\chaci\Desktop\PROJEKT\data\songs_wav'

# Replace 'full_path_to_ffmpeg' with the actual path to the FFmpeg executable.
ffmpeg_path = r"C:\Users\chaci\Downloads\ffmpeg\bin\ffmpeg.exe"

# List all the files in the input folder
input_files = os.listdir(input_folder)

for file in input_files:
    if file.endswith('.wav'):
        input_file_path = os.path.join(input_folder, file)
        output_file_path = os.path.join(output_folder, file)

        # Convert WAV to MP3 with a bitrate of 320 kbps
        mp3_output_file = os.path.splitext(input_file_path)[0] + '.mp3'
        cmd = f'"{ffmpeg_path}" -i "{input_file_path}" -b:a 320k "{mp3_output_file}"'
        subprocess.call(cmd, shell=True)

        # Move the original WAV file to the output folder
        shutil.move(input_file_path, output_file_path)

print("WAV to MP3 conversion (320 kbps) and file movement complete.")
