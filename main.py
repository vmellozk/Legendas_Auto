import sys
from PySide6.QtWidgets import QApplication
from gui.ui_main import AudioConverterApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AudioConverterApp()
    window.show()
    sys.exit(app.exec())
