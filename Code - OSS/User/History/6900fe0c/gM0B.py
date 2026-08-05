from PySide6.QtWidgets import QScrollArea
from PySide6.QtCore import Qt


class ScrollPage(QScrollArea):
    def __init__(self, widget):
        super().__init__()

        self.setWidget(widget)
        self.setWidgetResizable(True)

        self.setFrameShape(QScrollArea.NoFrame)

        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.setVerticalScrollBarPolicy(
            Qt.ScrollBarAsNeeded
        )