import yt_dlp
import os

def download_audio(video_url):
    # Automatically creating the output folder "downloads" if not exists
    output_folder = "downloads"
    os.makedirs(output_folder, exist_ok=True)

    # Set the download options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Best audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '192',  # MP3 quality (192kbps)
        }],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  # Set output path to "downloads"
    }

    # Download the video and convert to MP3
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Get the YouTube video URL
video_url = input("Enter the YouTube video URL: ")
download_audio(video_url)