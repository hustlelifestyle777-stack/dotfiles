from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from widgets.search_bar import SearchBar
from widgets.instrument_card import InstrumentCard
from PySide6.QtCore import Qt

class LivePage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Universal Search Bar
        self.search_bar = SearchBar()
        layout.addWidget(self.search_bar)
        title = QLabel("TRD KAIZEN")
        title.setAlignment(alignment=Qt.AlignHCenter)

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

