from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QPushButton,
    QWidget
)


class InstrumentCard(QFrame):
    def __init__(self, name, mode="home"):
        super().__init__()
        
        self.mode = mode
        self.expanded = False

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

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

        layout.addWidget(self.main_button)

        self.menu = QWidget()
        menu_layout = QVBoxLayout(self.menu)
        menu_layout.setContentsMargins(20, 0, 20, 10)

        self.live_btn = QPushButton("📈 Live Trades (90)")
        self.backtest_btn = QPushButton("📊 Backtests (190)")

        self.live_btn.setFixedSize(300, 34)
        self.backtest_btn.setFixedSize(300, 34)
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

        self.live_btn.setStyleSheet(style)
        self.backtest_btn.setStyleSheet(style)

        menu_layout.addWidget(self.live_btn)
        menu_layout.addWidget(self.backtest_btn)

        self.menu.hide()

        layout.addWidget(self.menu)

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
