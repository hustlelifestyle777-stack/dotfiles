from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QPushButton,
    QWidget
)
from PySide6.QtCore import Signal


class BacktestInstrumentCard(QFrame):
    newBacktestTrade = Signal()
    def __init__(self, name, mode="home"):
        super().__init__()

        self.mode = mode
        self.expanded = False

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(4)

        self.main_button = QPushButton(f"▶ {name}")
        self.main_button.setFixedSize(340, 42)
        self.main_button.setStyleSheet("""
        QPushButton {
            border-radius: 21px;
            padding: 8px;
            background-color: #3b3b3b;
            border: 1px solid #666666;
            color: white;
            text-align: left;
}
""")
        self.main_button.clicked.connect(self.toggle)

        self.layout.addWidget(self.main_button)

        self.menu = QWidget()
        self.menu_layout = QVBoxLayout(self.menu)
        self.menu_layout.setContentsMargins(20, 0, 20, 10)

        self.new_backtest_btn = QPushButton("➕ New Backtest")
        self.new_backtest_btn.clicked.connect(self.open_backtest_trade)
        self.backtest_history_btn = QPushButton("📈 Backtests (90)")
        

        self.new_backtest_btn.setFixedSize(300, 34)
        self.backtest_history_btn.setFixedSize(300, 34)
        style = """
        QPushButton {
            border-radius: 17px;
            background-color: #4a4a4a;
            border: 1px solid #666666;
            color: white;
            text-align: left;
            padding-left: 12px;
}
"""

        self.new_backtest_btn.setStyleSheet(style)
        self.backtest_history_btn.setStyleSheet(style)

        self.menu_layout.addWidget(self.new_backtest_btn)
        self.menu_layout.addWidget(self.backtest_history_btn)

        self.menu.hide()

        self.layout.addWidget(self.menu)

    def toggle(self):
        self.expanded = not self.expanded

        if self.expanded:
            self.main_button.setText(
                self.main_button.text().replace("▶", "▼")
            )
            self.menu.show()
        else:
            self.main_button.setText(
                self.main_button.text().replace("▼", "▶")
            )
            self.menu.hide()

    def open_backtest_trade(self):
        self.newBacktestTrade.emit()
        
        
