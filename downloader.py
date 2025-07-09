import subprocess
import sys
import os

def check_yt_dlp():
    """Quick check if yt-dlp is available, install if not (no update check)"""
    try:
        # Just check if yt-dlp is installed
        result = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True, check=True)
        current_version = result.stdout.strip()
        print(f"yt-dlp is installed. Version: {current_version}")
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("yt-dlp not found. Installing...")
        try:
            subprocess.run([
                sys.executable, "-m", "pip", "install", "yt-dlp"
            ], check=True)
            print("yt-dlp installed successfully")
            
            # Verify installation
            result = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True, check=True)
            version = result.stdout.strip()
            print(f"Installed yt-dlp version: {version}")
            
        except subprocess.CalledProcessError as e:
            print(f"Failed to install yt-dlp: {e}")
            sys.exit(1)

def download_audio(url, script_dir):
    # Download best audio and convert to mp3
    videos_path = os.path.join(script_dir, "videos", "%(title)s [%(id)s].%(ext)s")
    command = [
        "yt-dlp",
        "-x",  # extract audio
        "--audio-format", "mp3",  # convert to mp3
        "--audio-quality", "0",   # best quality
        "-o", videos_path,  # output to videos folder with absolute path
        url
    ]
    subprocess.run(command, check=True)

def main():
    # Quick check yt-dlp availability (no update check)
    check_yt_dlp()
    
    # Get the directory where the executable/script is located
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        script_dir = os.path.dirname(sys.executable)
    else:
        # Running as Python script
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
    url_file_path = os.path.join(script_dir, "url.txt")
    
    # Ensure videos directory exists
    videos_dir = os.path.join(script_dir, "videos")
    os.makedirs(videos_dir, exist_ok=True)
    
    try:
        with open(url_file_path, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: url.txt not found at {url_file_path}")
        print("Please create a url.txt file with YouTube URLs, one per line.")
        input("Press Enter to exit...")
        return
    
    if not urls:
        print("No URLs found in url.txt")
        input("Press Enter to exit...")
        return
    
    print(f"Found {len(urls)} URL(s) to download")
    
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Downloading: {url}")
        try:
            download_audio(url, script_dir)
            print(f"✓ Successfully downloaded: {url}")
        except subprocess.CalledProcessError:
            print(f"✗ Failed to download: {url}")
    
    print(f"\nDownload complete! Check the 'videos' folder.")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
