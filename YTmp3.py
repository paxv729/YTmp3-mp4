from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video_as_mp3(video_url, output_folder):
    try:
        # YouTube video ko download karen
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        
        print(f"Downloading '{yt.title}'...")
        audio_file_path = stream.download(output_path=output_folder)
        
        # MP4 ko MP3 mein convert karen
        base, ext = os.path.splitext(audio_file_path)
        mp3_file_path = base + '.mp3'
        audio = AudioSegment.from_file(audio_file_path)
        audio.export(mp3_file_path, format="mp3")
        
        # Temporary MP4 file delete karen
        os.remove(audio_file_path)
        
        print(f"Downloaded and converted to MP3: {mp3_file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Input
video_url = input("Enter the YouTube video URL: ")
output_folder = "downloads"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Call the function
download_youtube_video_as_mp3(video_url, output_folder)