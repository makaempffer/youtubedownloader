import yt_dlp
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video():
    youtube_url = url_entry.get()
    output_path = filedialog.askdirectory()
    
    if not youtube_url or not output_path:
        messagebox.showerror("Error", "Please provide a valid URL and output path.")
        return
    
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download the best quality
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Save with video title
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def download_audio():
    youtube_url = url_entry.get()
    output_path = filedialog.askdirectory()
    
    if not youtube_url or not output_path:
        messagebox.showerror("Error", "Please provide a valid URL and output path.")
        return
    
    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Download best audio
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Save with video title
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Extract audio
                'preferredcodec': 'mp3',  # Save as MP3
                'preferredquality': '192',  # Set quality
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        
        messagebox.showinfo("Success", "Audio downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("YouTube Downloader")

tk.Label(root, text="YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Download Video", command=download_video).pack(pady=10)
tk.Button(root, text="Download Audio (MP3)", command=download_audio).pack(pady=10)

root.mainloop()
