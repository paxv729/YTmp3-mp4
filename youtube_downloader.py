import os
from pytube import YouTube
from moviepy.editor import AudioFileClip

def download_video(url, download_path):
    try:
        yt = YouTube(url)
        print(f"Downloading video: {yt.title}")
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        if stream:
            stream.download(output_path=download_path)
            print(f"Video downloaded successfully: {yt.title}")
        else:
            print("No suitable video stream found.")
    except Exception as e:
        print(f"Error downloading video: {e}")

def download_audio(url, download_path):
    try:
        yt = YouTube(url)
        print(f"Downloading audio: {yt.title}")
        stream = yt.streams.filter(only_audio=True).first()
        if stream:
            audio_path = stream.download(output_path=download_path)
            mp3_path = os.path.join(download_path, yt.title + ".mp3")
            
            print(f"Converting to MP3: {yt.title}")
            audio_clip = AudioFileClip(audio_path)
            audio_clip.write_audiofile(mp3_path)
            audio_clip.close()
            os.remove(audio_path)
            
            print(f"MP3 conversion complete: {yt.title}")
        else:
            print("No suitable audio stream found.")
    except Exception as e:
        print(f"Error downloading audio: {e}")

def main():
    print("YouTube MP3/MP4 Downloader")
    download_path = input("Enter the download folder path: ")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    url = input("Enter the YouTube video URL: ")
    choice = input("Enter the format (MP3/MP4): ").strip().lower()

    if choice == "mp4":
        download_video(url, download_path)
    elif choice == "mp3":
        download_audio(url, download_path)
    else:
        print("Invalid choice. Please enter 'MP3' or 'MP4'.")

if __name__ == "__main__":
    main()