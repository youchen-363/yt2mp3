# YouTube Audio Downloader

A simple Python script to download YouTube videos as MP3 audio files.

## Requirements

- Python 3.6 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use:

### Step 1: Setup
1. Create a `url.txt` file in the project folder
2. Add YouTube URLs to `url.txt` (one URL per line)

### Step 2: Run
```bash
python downloader.py
```

### Example folder structure:
```
ytb-videos-dwl/
├── downloader.py
├── requirements.txt
├── url.txt
└── videos/                               (created automatically)
    └── [downloaded MP3 files]
```

## Features:

- Downloads YouTube videos as high-quality MP3 files
- Batch processing from URL list
- Automatic folder creation for downloads
- Error handling for failed downloads

## Troubleshooting:

### Common issues:
- ✅ **url.txt missing**: Make sure the file exists in the project directory
- ✅ **No internet**: Check your internet connection
- ✅ **Permission denied**: Run the script with appropriate permissions
- ✅ **Download failed**: The URL may be invalid or the video unavailable

## Dependencies:
Check `requirements.txt` for the full list of required packages.

## Notes:
- Downloaded files are saved in the `videos/` directory
- The script will create the `videos/` folder automatically if it doesn't exist
- Make sure you have sufficient disk space for downloads