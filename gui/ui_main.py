import os
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QFileDialog,
    QVBoxLayout, QTabWidget, QMessageBox
)

from core.youtube import download_audio_youtube
from core.instagram import download_video_instagram
from core.transcription import transcribe_and_save_audio_youtube


class AudioConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Conversor de Áudio em Texto")
        self.setFixedSize(400, 300)

        tabs = QTabWidget()
        tabs.addTab(self.youtube_tab_ui(), "YouTube")
        tabs.addTab(self.instagram_tab_ui(), "Instagram")

        self.setCentralWidget(tabs)

    def youtube_tab_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.youtube_url = QLineEdit()
        self.youtube_url.setPlaceholderText("Cole sua URL aqui")
        layout.addWidget(QLabel("URL do YouTube:"))
        layout.addWidget(self.youtube_url)

        self.output_dir = QLineEdit()
        self.output_dir.setPlaceholderText("Escolha a pasta de destino")
        layout.addWidget(QLabel("Salvar em:"))
        layout.addWidget(self.output_dir)

        browse_button = QPushButton("Procurar")
        browse_button.clicked.connect(self.select_output_dir)
        layout.addWidget(browse_button)

        download_button = QPushButton("Baixar Áudio YT")
        download_button.clicked.connect(self.download_audio_youtube_ui)
        layout.addWidget(download_button)

        convert_button = QPushButton("Baixar e Converter Áudio em Texto")
        convert_button.clicked.connect(self.download_and_transcribe)
        layout.addWidget(convert_button)

        widget.setLayout(layout)
        return widget

    def instagram_tab_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.instagram_url = QLineEdit()
        self.instagram_url.setPlaceholderText("Cole sua URL aqui")
        layout.addWidget(QLabel("URL do Instagram:"))
        layout.addWidget(self.instagram_url)

        self.output_dir_ig = QLineEdit()
        self.output_dir_ig.setPlaceholderText("Escolha a pasta de destino")
        layout.addWidget(QLabel("Salvar em:"))
        layout.addWidget(self.output_dir_ig)

        browse_button = QPushButton("Procurar")
        browse_button.clicked.connect(self.select_output_dir_ig)
        layout.addWidget(browse_button)

        download_button = QPushButton("Baixar Vídeo IG")
        download_button.clicked.connect(self.download_video_instagram_ui)
        layout.addWidget(download_button)

        widget.setLayout(layout)
        return widget

    def select_output_dir(self):
        path = QFileDialog.getExistingDirectory(self, "Selecionar Diretório")
        if path:
            self.output_dir.setText(path)

    def select_output_dir_ig(self):
        path = QFileDialog.getExistingDirectory(self, "Selecionar Diretório")
        if path:
            self.output_dir_ig.setText(path)

    def show_message(self, message):
        QMessageBox.information(self, "Info", message)

    def download_audio_youtube_ui(self):
        url = self.youtube_url.text()
        output = self.output_dir.text()
        if url and output:
            download_audio_youtube(url, os.path.join(output, 'audio.mp3'))
            self.show_message("Download realizado!")

    def download_and_transcribe(self):
        url = self.youtube_url.text()
        output = self.output_dir.text()
        audio_path = os.path.join(output, 'audio.mp3')
        transcription_path = os.path.join(output, 'transcription.txt')
        if url and output:
            download_audio_youtube(url, audio_path)
            transcribe_and_save_audio_youtube(audio_path, transcription_path)
            self.show_message("Download e transcrição realizados!")

    def download_video_instagram_ui(self):
        url = self.instagram_url.text()
        output = self.output_dir_ig.text()
        if url and output:
            try:
                download_video_instagram(url, output)
                self.show_message("Download do vídeo IG concluído!")
            except Exception as e:
                self.show_message(f"Erro: {str(e)}")
