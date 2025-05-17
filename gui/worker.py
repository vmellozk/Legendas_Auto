from PySide6.QtCore import QThread, Signal
import os
import time
from core.youtube import download_audio_youtube
from core.transcription import transcribe_and_save_audio_youtube

class DownloadTranscribeWorker(QThread):
    log_signal = Signal(str)
    finished_signal = Signal(str)
    error_signal = Signal(str)

    def __init__(self, url, output_dir, filename):
        super().__init__()
        self.url = url
        self.output_dir = output_dir
        self.filename = filename
        
    def log(self, message):
        self.log_signal.emit(message)

    def run(self):
        try:
            filename = self.filename or "transcription"
            
            self.log("Processando o seu vídeo para gerar a legenda...")
            time.sleep(3)

            audio_base = os.path.join(self.output_dir, self.filename)
            counter = 1
            while os.path.exists(f"{audio_base}.mp3"):
                audio_base = f"{os.path.join(self.output_dir, filename)}_{counter}"
                counter += 1

            transcription_path = os.path.join(self.output_dir, filename)
            counter_txt = 1
            temp_transcription_path = f"{transcription_path}.txt"
            while os.path.exists(temp_transcription_path):
                temp_transcription_path = f"{transcription_path}_{counter_txt}.txt"
                counter_txt += 1
            transcription_path = temp_transcription_path

            self.log("Transcrevendo o áudio para texto com inteligência artificial...")
            download_audio_youtube(self.url, audio_base)

            self.log("Finalizando a geração da legenda e salvando o arquivo...")
            audio_path = f"{audio_base}.mp3"
            transcribe_and_save_audio_youtube(audio_path, transcription_path)

            self.finished_signal.emit(transcription_path)

        except Exception as e:
            self.error_signal.emit(str(e))
