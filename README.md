🎵 YouTube Audio Downloader (MP3)
This is a simple Python GUI tool that allows users to download audio from YouTube videos in MP3 format using yt-dlp and tkinter.

💡 You can also enable video downloading by uncommenting a line in the code.

📦 Features
Download high-quality audio in MP3 format.

Simple and clean GUI using tkinter.

Automatically names the file with the video's title.

Uses yt-dlp, a powerful downloader supporting many websites.

🛠️ Requirements
Python 3.7+

yt-dlp

ffmpeg (for audio extraction)

🧪 Installation
Clone this repo (or just copy the script):

bash
Copiar
Editar
git clone https://github.com/makaempffer/youtube-audio-downloader.git
cd youtube-audio-downloader
Install dependencies:

bash
Copiar
Editar
pip install yt-dlp
Install FFmpeg:

On Ubuntu/Debian:

bash
Copiar
Editar
sudo apt install ffmpeg
On macOS (with Homebrew):

bash
Copiar
Editar
brew install ffmpeg
On Windows:
Download FFmpeg from https://ffmpeg.org/download.html
and add it to your system PATH.

🚀 Usage
Run the script with Python:

bash
Copiar
Editar
python downloader.py
Paste the YouTube video URL.

Click "Download Audio (MP3)".

Choose a directory to save the file.

Wait for the magic. 🎶

📺 Optional: Enable Video Downloading (uncomment code)

# tk.Button(root, text="Download Video", command=download_video).pack(pady=10)
📄 License
This project is licensed under the MIT License.

(Semi generated with gpt).
