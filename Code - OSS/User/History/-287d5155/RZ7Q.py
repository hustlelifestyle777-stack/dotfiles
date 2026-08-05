from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from widgets.search_bar import SearchBar
from widgets.live_instrument_card import LiveInstrumentCard
from PySide6.QtCore import Qt, Signal

class LivePage(QWidget):
    openTradePage = Signal()
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # Universal Search Bar
        self.search_bar = SearchBar()
        layout.addWidget(self.search_bar)
        title = QLabel("TRD KAIZEN")
        title.setAlignment(Qt.AlignCenter)

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

            button = LiveInstrumentCard(item)
            button.newLiveTrade.connect(self.open_trade_page)
            

            card_layout.addWidget(button,
            alignment=Qt.AlignCenter)

            layout.addWidget(card)

        layout.addStretch(1)

    def open_trade_page(self):
        self.openTradePage.emit()


