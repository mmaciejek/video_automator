import os
import subprocess


def reencode_videos(input_folder, output_folder):
    # List all the files in the input folder
    input_files = os.listdir(input_folder)
    ffmpeg_path = r"C:\Users\chaci\Downloads\ffmpeg\bin\ffmpeg.exe"

    # Iterate through the files and reencode them
    for file in input_files:
        if file.endswith('.mp4'):
            input_file_path = os.path.join(input_folder, file)
            output_file_path = os.path.join(output_folder, file)

            # Check if the output file already exists
            if os.path.exists(output_file_path):
                print(f"Skipping '{file}' as it already exists in the output folder.")
            else:
                # Use the provided FFmpeg path to reencode the video
                cmd = f'"{ffmpeg_path}" -i "{input_file_path}" -c:v libx264 -preset veryfast -crf 23 -c:a copy "{output_file_path}"'
                subprocess.call(cmd, shell=True)
                print(f"Reencoded '{file}' and saved it to the output folder.")

    print("Videos reencoding complete.")


if __name__ == '__main__':
    # Example usage:
    input_folder = r'C:\Users\chaci\Desktop\PROJEKT\data\input_videos'
    output_folder = r'C:\Users\chaci\Desktop\PROJEKT\data\input_reencoded_videos'

    reencode_videos(input_folder, output_folder)
