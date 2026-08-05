from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from ui.forms.trade_form import TradeForm


class LiveTradePage(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        container = QHBoxLayout()

        container.addStretch()

        self.trade_form = TradeForm()
        self.trade_form.setMaximumWidth(900)

        container.addWidget(self.trade_form)

        container.addStretch()

        self.layout.addLayout(container)
