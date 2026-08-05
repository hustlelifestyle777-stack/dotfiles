from PySide6.QtWidgets import QWidget, QVBoxLayout

from ui.forms.trade_form import TradeForm


class BacktestTradePage(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.trade_form = TradeForm()
        self.layout.addWidget(self.trade_form)