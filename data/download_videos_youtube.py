import os
import re

from pytube import YouTube


def sanitize_filename(filename):
    # Remove invalid characters from the filename using regular expression
    return re.sub(r'[<>:"/\\|?*]', '', filename)


def download_videos_from_file(file_path, video_folder):
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)

    existing_video_titles = set()
    for video_file in os.listdir(video_folder):
        if video_file.endswith('.mp4'):
            video_title = video_file[:-4]
            existing_video_titles.add(video_title)

    with open(file_path, 'r') as file:
        video_links = file.read().strip().split('\n')

    for link in video_links:
        try:
            yt = YouTube(link)
            video_title = sanitize_filename(yt.title.replace(" ", "_"))

            if video_title in existing_video_titles:
                print(f"Skipping {yt.title}. Video already downloaded.")
                continue

            # List of desired resolutions in descending order
            desired_resolutions = ["1080p", "720p", "480p", "360p"]

            video = None
            for resolution in desired_resolutions:
                video = yt.streams.filter(progressive=False, file_extension='mp4', resolution=resolution).first()
                if video:
                    break

            if video:
                print(f"Downloading: {yt.title}")
                video_file_path = os.path.join(video_folder, f"{video_title}.mp4")
                video.download(output_path=video_folder, filename=f"{video_title}.mp4")
                print("Download completed successfully.")
            else:
                print(f"Skipping {yt.title}. Could not find a compatible video stream.")

        except Exception as e:
            print(f"Error downloading {link}: {str(e)}")
            retries = 4
            while retries > 0:
                retries -= 1
                print(f"Retrying download {2 - retries} time...")
                try:
                    # Retry the download
                    yt = YouTube(link)
                    video_title = sanitize_filename(yt.title.replace(" ", "_"))
                    # Rest of the code for download attempts...

                    if video_title in existing_video_titles:
                        print(f"Skipping {yt.title}. Video already downloaded.")
                        continue

                    # List of desired resolutions in descending order
                    desired_resolutions = ["1080p", "720p", "480p", "360p"]

                    # Find the first available stream with the desired resolutions
                    video = None
                    for resolution in desired_resolutions:
                        video = yt.streams.filter(progressive=False, file_extension='mp4',
                                                  resolution=resolution).first()
                        if video:
                            break

                    if video:
                        print(f"Downloading: {yt.title}")
                        video_file_path = os.path.join(video_folder, f"{video_title}.mp4")
                        video.download(output_path=video_folder, filename=f"{video_title}.mp4")
                        print("Download completed successfully.")
                    else:
                        print(f"Skipping {yt.title}. Could not find a compatible video stream.")

                except Exception as e:
                    print(f"Error downloading {link}: {str(e)}")
                    if retries == 0:
                        # If error persists after retries, delete the partially downloaded video file (if any)
                        video_file_path = os.path.join(video_folder, f"{video_title}.mp4")
                        if os.path.exists(video_file_path):
                            os.remove(video_file_path)


if __name__ == "__main__":
    file_path = "G:\\Python\\PROJEKT\\links_youtube_videos.txt"
    video_folder = "G:\\Python\\PROJEKT\\VIDEOS"
    download_videos_from_file(file_path, video_folder)
