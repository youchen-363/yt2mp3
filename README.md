# 🎵 yt2mp3

A simple Python script to download YouTube videos as **MP3 audio files**.

---

## 📦 Requirements
- Python 3.6+
- Dependencies listed in `requirements.txt`

---

## 🚀 Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/yt2mp3.git
   cd yt2mp3
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎬 How to Use

### 1. **Prepare your URLs**
Create a file named `url.txt` in the project directory. Add one YouTube URL per line.

### 2. **Run the script**
```bash
python downloader.py
```

### 📁 Example folder structure:
```
yt2mp3/
├── downloader.py
├── requirements.txt
├── url.txt
└── videos/             # Created automatically
    └── [downloaded MP3 files]
```

---

## ✅ Features
- 📥 Download YouTube videos as high-quality MP3s
- 📚 Batch download from `url.txt`
- 📂 Automatically creates a `videos/` folder
- 🛡️ Basic error handling for failed downloads

---

## 🧰 Troubleshooting

| Issue | Solution |
|-------|----------|
| `url.txt` missing | Make sure the file exists in the root folder |
| No internet | Check your connection |
| Permission denied | Run the script with proper access rights |
| Download failed | Ensure the URL is valid and the video is available |

---

## 📌 Notes
- All MP3 files are saved in the `videos/` directory.
- The folder is created automatically if not present.
- Ensure sufficient disk space is available.

---

## 🙏 Acknowledgements

This project relies on [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), an open-source YouTube downloader.

For licensing information, see the [License](#-license) section below.

---

## 🔒 License

This project is licensed under the [Creative Commons BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/).

Commercial use is not permitted.

This script depends on [`yt-dlp`](https://github.com/yt-dlp/yt-dlp), which is licensed under the [Unlicense](https://unlicense.org/).
