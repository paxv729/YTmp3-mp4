from youtube_dl import YoutubeDL
import os

def download_video_as_mp3(video_url, output_folder):
    try:
        # Ensure output folder exists
        os.makedirs(output_folder, exist_ok=True)
        
        options = {
            'format': 'bestaudio/best',  # Audio stream ko download karein
            'extractaudio': True,        # Sirf audio extract karein
            'audioformat': 'mp3',        # MP3 format set karein
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Output file format
            'noplaylist': True,          # Playlist download na karein
        }
        with YoutubeDL(options) as ydl:
            print(f"Downloading audio from: {video_url}")
            ydl.download([video_url])
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")

# Input
video_url = input("Enter the YouTube video URL: ")
output_folder = "downloads"

# Function ko call karein
download_video_as_mp3(video_url, output_folder)
