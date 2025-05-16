import os
from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QLineEdit, QFileDialog,
    QVBoxLayout, QTabWidget, QMessageBox, QHBoxLayout, QGroupBox,
    QProgressBar, QTextEdit
)
from PySide6.QtCore import QStandardPaths

from core.youtube import download_audio_youtube
from core.instagram import download_video_instagram
from core.transcription import transcribe_and_save_audio_youtube
from PySide6.QtGui import QIcon

MINIMAL_STYLE = """
QWidget {
    background-color: #1e1e1e;
    color: #f0f0f0;
    font-family: "Segoe UI", sans-serif;
    font-size: 12pt;
}

QPushButton {
    background-color: #007acc;
    border: none;
    padding: 8px 16px;
    border-radius: 6px;
    color: white;
}

QPushButton:hover {
    background-color: #005f9e;
}

QGroupBox {
    border: 1px solid #444;
    border-radius: 8px;
    margin-top: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 4px;
    color: #aaa;
    font-weight: bold;
}

QLineEdit, QLabel {
    font-size: 11pt;
}

QProgressBar {
    background-color: #333;
    color: white;
    border: none;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #00bcd4;
    width: 20px;
}
"""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de Legendas com IA")
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.setMinimumSize(600, 400)
        self.setStyleSheet(MINIMAL_STYLE)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Header
        header = QLabel("🎙️ Gerador de Legendas")
        header.setStyleSheet("font-size: 20pt; font-weight: bold;")
        layout.addWidget(header)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.addTab(self.youtube_tab_ui(), "YouTube")
        self.tabs.addTab(self.instagram_tab_ui(), "Instagram")
        layout.addWidget(self.tabs)

        # Progresso e Logs
        self.progress = QProgressBar()
        self.logs = QTextEdit()
        self.logs.setReadOnly(True)
        self.logs.setPlaceholderText("Log de atividades...")
        layout.addWidget(self.progress)
        layout.addWidget(self.logs)

        # Rodapé
        footer = QLabel("Criado com 💙 por vmellozk")
        footer.setStyleSheet("font-size: 10pt; color: #888;")
        layout.addWidget(footer)

        self.setLayout(layout)

    def youtube_tab_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()

        url_group = QGroupBox("Cole sua URL aqui:")
        url_layout = QHBoxLayout()
        self.youtube_url = QLineEdit()
        url_layout.addWidget(self.youtube_url)
        url_group.setLayout(url_layout)
        layout.addWidget(url_group)

        output_group = QGroupBox("Salvar em:")
        output_layout = QHBoxLayout()
        self.output_dir = QLineEdit()
        browse_button = QPushButton("Pasta de destino")
        
        filename_group = QGroupBox("Nome do arquivo:")
        filename_layout = QHBoxLayout()
        self.filename_input = QLineEdit()
        self.filename_input.setText("audio")
        filename_layout.addWidget(self.filename_input)
        ext_label = QLabel(".mp3")
        filename_layout.addWidget(ext_label)
        filename_group.setLayout(filename_layout)
        layout.addWidget(filename_group)
        
        desktop_path = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation)
        self.output_dir.setText(desktop_path)
        browse_button.clicked.connect(self.select_output_dir)
        output_layout.addWidget(self.output_dir)
        output_layout.addWidget(browse_button)
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)

        actions_group = QGroupBox("Ação")
        actions_layout = QHBoxLayout()
        convert_button = QPushButton("Baixar e Converter Áudio em Texto")
        convert_button.clicked.connect(self.download_and_transcribe)

        actions_layout.addWidget(convert_button)
        actions_group.setLayout(actions_layout)
        layout.addWidget(actions_group)

        widget.setLayout(layout)
        return widget

    def instagram_tab_ui(self):
        widget = QWidget()
        layout = QVBoxLayout()

        url_group = QGroupBox("Cole sua URL aqui:")
        url_layout = QHBoxLayout()
        self.instagram_url = QLineEdit()
        url_layout.addWidget(self.instagram_url)
        url_group.setLayout(url_layout)
        layout.addWidget(url_group)

        output_group = QGroupBox("Salvar em:")
        output_layout = QHBoxLayout()
        self.output_dir_ig = QLineEdit()
        browse_button = QPushButton("Procurar")
        browse_button.clicked.connect(self.select_output_dir_ig)
        output_layout.addWidget(self.output_dir_ig)
        output_layout.addWidget(browse_button)
        output_group.setLayout(output_layout)
        layout.addWidget(output_group)

        actions_group = QGroupBox("Ação")
        actions_layout = QHBoxLayout()
        download_button = QPushButton("Baixar Vídeo IG")
        download_button.clicked.connect(self.download_video_instagram_ui)
        actions_layout.addWidget(download_button)
        actions_group.setLayout(actions_layout)
        layout.addWidget(actions_group)

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

    def download_and_transcribe(self):
        url = self.youtube_url.text().strip()
        output = self.output_dir.text().strip()
        filename = self.filename_input.text().strip()
        if not filename:
            filename = "audio"
            
        if url and output:
            audio_base = os.path.join(output, filename)
            counter = 1
            temp_audio_base = audio_base
            while os.path.exists(f"{temp_audio_base}.mp3"):
                temp_audio_base = f"{audio_base}_{counter}"
                counter += 1
            audio_base = temp_audio_base
            
            transcription_path = os.path.join(output, 'transcription')
            counter_txt = 1
            temp_transcription_path = f"{transcription_path}.txt"
            while os.path.exists(temp_transcription_path):
                temp_transcription_path = f"{transcription_path}_{counter_txt}.txt"
                counter_txt += 1
            transcription_path = temp_transcription_path

            download_audio_youtube(url, audio_base)
            audio_path = f"{audio_base}.mp3"
            
            transcribe_and_save_audio_youtube(audio_path, transcription_path)
            self.show_message("Download e transcrição realizados!")
            
        else:
            self.show_message("Por favor, preencha a URL e o diretório de saída.")

    def download_video_instagram_ui(self):
        url = self.instagram_url.text()
        output = self.output_dir_ig.text()
        if url and output:
            try:
                download_video_instagram(url, output)
                self.show_message("Download do vídeo IG concluído!")
            except Exception as e:
                self.show_message(f"Erro: {str(e)}")
