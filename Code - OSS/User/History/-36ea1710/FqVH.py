from PySide6.QtWidgets import QDialog, QVBoxLayout

from ui.forms.trade_form import TradeForm


class LiveTradeDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Live Trade")
        self.resize(700, 900)

        layout = QVBoxLayout(self)

        self.trade_form = TradeForm()
        layout.addWidget(self.trade_form)