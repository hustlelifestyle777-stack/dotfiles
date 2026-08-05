from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFrame
)
from PySide6.QtCore import Qt
from widgets.search_bar import SearchBar
from widgets.instrument_card import InstrumentCard
from widgets.bottom_nav import BottomNav


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TRD KAIZEN")
        self.resize(1200, 800)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(50, 25, 50, 25)
        layout.setSpacing(8)

        search = SearchBar()

        title = QLabel("TRD KAIZEN")
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(search, alignment=Qt.AlignHCenter)
        layout.addWidget(title)
        layout.addStretch(1)
        instruments = [
            "NIFTY",
            "BANKNIFTY",
            "SENSEX",
            "CRUDE OIL",
            "NATURAL GAS",
            "BTCUSD",
            "EURUSD"
        ]

        for item in instruments:
            card = QFrame()
            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(0, 2, 0, 2)
            card_layout.setSpacing(0)

            button = InstrumentCard(item)
            

            card_layout.addWidget(button,
            alignment=Qt.AlignCenter)

            layout.addWidget(card)

        layout.addStretch(1)
        bottom_nav = BottomNav()
        layout.addWidget(bottom_nav, alignment=Qt.AlignCenter)