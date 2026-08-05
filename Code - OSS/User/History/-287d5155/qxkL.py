from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from widgets.search_bar import SearchBar


class LivePage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Universal Search Bar
        self.search_bar = SearchBar()
        layout.addWidget(self.search_bar)

        # Temporary content
        label = QLabel("LIVE PAGE")
        layout.addWidget(label)

        layout.addStretch()