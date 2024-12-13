import os

def download_video():
    # User se URL input lena
    url = input("Enter the YouTube video URL: ")

    try:
        # Temporary file mein formats save karna
        print("\nFetching available video formats...\n")
        os.system(f"yt-dlp -F {url} > formats.txt")

        # Formats file read karna aur filter karna
        with open("formats.txt", "r") as f:
            lines = f.readlines()
            numbered_formats = {}
            print("Available Formats:")
            counter = 1
            desired_resolutions = ["144p", "240p", "480p", "1080p", "2k", "4k"]

            for line in lines:
                if any(res in line for res in desired_resolutions):  # Sirf desired formats filter karna
                    print(f"{counter}. {line.strip()}")
                    format_code = line.strip().split()[0]  # Format code extract karna
                    numbered_formats[counter] = format_code
                    counter += 1

        # Temporary file cleanup
        os.remove("formats.txt")

        # Agar koi format available na ho toh error dikhana
        if not numbered_formats:
            print("No desired formats found!")
            return

        # User se numbered format input lena
        choice = int(input("\nEnter the number of the desired quality: "))
        video_format_code = numbered_formats[choice]

        # Best audio format automatically select karna
        audio_format_code = "bestaudio"  # Always fetch the best audio available

        # Download path set karna (Android default Downloads folder)
        download_path = "/storage/emulated/0/Download"

        # Video aur audio ko merge karke download karna
        print("\nDownloading the video with audio...")
        os.system(f"yt-dlp -f \"{video_format_code}+{audio_format_code}\" -o \"{download_path}/%(title)s.%(ext)s\" {url}")
        print(f"\nDownload complete! Saved in: {download_path}")

    except Exception as e:
        print(f"Error: {e}")

# Script start hone ka entry point
if __name__ == "__main__":
    download_video()