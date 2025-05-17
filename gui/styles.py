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
