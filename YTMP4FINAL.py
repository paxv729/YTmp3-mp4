import yt_dlp
import os

def download_video(url, file_type="mp4", resolution="best"):
    download_path = "/storage/emulated/0/Download/%(title)s.%(ext)s"  # Android download folder

    # Correcting format selection for video resolution
    if file_type == 'mp4':
        ydl_opts = {
            'format': f'bestvideo[height<={resolution}]+bestaudio/best',
            'outtmpl': download_path,  # Set the download path
        }
    elif file_type == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',  # Only audio, best quality
            'outtmpl': download_path,
        }
    else:
        print("Unsupported file type. Please choose 'mp4' or 'mp3'.")
        return

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    file_type = input("Enter the file type to download (mp4/mp3): ").lower()
    resolution = input("Enter resolution (1080p, 720p, 480p): ").lower()

    # Set default resolution if invalid input is provided
    if resolution not in ['1080p', '720p', '480p']:
        print("Invalid resolution. Defaulting to best resolution.")
        resolution = 'best'

    download_video(url, file_type, resolution)