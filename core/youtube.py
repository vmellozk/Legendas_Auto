import yt_dlp
import sys
import os

def resource_path(relative_path):
    # Para suportar PyInstaller
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def download_audio_youtube(video_url, output_path):
    try:
        ffmpeg_dir = resource_path(os.path.join("ffmpeg", "bin"))
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'ffmpeg_location': ffmpeg_dir,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print("Erro no download do áudio:", str(e))
