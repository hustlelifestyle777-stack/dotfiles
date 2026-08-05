from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class BacktestPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel("BACKTEST PAGE")
        layout.addWidget(label)