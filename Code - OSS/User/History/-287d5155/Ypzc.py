from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class LivePage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel("LIVE PAGE")
        layout.addWidget(label)