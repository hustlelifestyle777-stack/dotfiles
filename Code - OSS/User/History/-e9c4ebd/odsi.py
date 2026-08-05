from PySide6.QtWidgets import (
    QFrame,
    QPushButton,
    QHBoxLayout
)
from PySide6.QtCore import Signal

class BottomNav(QFrame):
    pageChanged = Signal(int)
    def __init__(self):
        super().__init__()

        self.setFixedSize(540, 85)

        self.setStyleSheet("""
        QFrame {
            background-color: #353535;
            border-radius: 32px;
            border: 1px solid #4d4d4d;
        }

        QPushButton {
            border: none;
            background: transparent;
            color: #bbbbbb;
            font-size: 13px;
            font-weight: bold;
        }

        QPushButton:hover {
            color: white;
        }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 12, 20, 12)
        layout.setSpacing(25)

        self.home = QPushButton("🏠\nHOME")
        self.live = QPushButton("📈\nLIVE")
        self.backtest = QPushButton("🧪\nBACKTEST")

        self.home.setObjectName("home")
        self.live.setObjectName("live")
        self.backtest.setObjectName("backtest")

        layout.addWidget(self.home)
        layout.addWidget(self.live)
        layout.addWidget(self.backtest)

        self.home.clicked.connect(lambda: self.pageChanged.emit(0))
        self.live.clicked.connect(lambda: self.pageChanged.emit(1))
        self.backtest.clicked.connect(lambda: self.pageChanged.emit(2))