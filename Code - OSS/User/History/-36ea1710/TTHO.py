from PySide6.QtWidgets import QWidget, QVBoxLayout,QScrollArea

from ui.forms.trade_form import TradeForm


class LiveTradePage(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        # Scroll Area
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QScrollArea.NoFrame)

        # Trade Form
        self.trade_form = TradeForm()
        self.scroll.setWidget(self.trade_form)

        # Add scroll area to page
        self.layout.addWidget(self.scroll)