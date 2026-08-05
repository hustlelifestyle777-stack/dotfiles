from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtCore import Qt
from ui.home_page import HomePage
from ui.live_page import LivePage
from ui.backtest_page import BacktestPage
from ui.forms.live_trade import LiveTradePage
from widgets.bottom_nav import BottomNav

class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TRD KAIZEN")
        self.resize(1200, 800)

        layout = QVBoxLayout(self)

        self.stack = QStackedWidget()

        self.home_page = HomePage()
        self.live_page = LivePage()
        self.backtest_page = BacktestPage()
        self.trade_page = LiveTradePage()
        self.live_page.openTradePage.connect(
            lambda: self.stack.setCurrentWidget(self.trade_page)
            )

        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.live_page)
        self.stack.addWidget(self.backtest_page)
        self.stack.addWidget(self.trade_page)

        layout.addWidget(self.stack)
        self.bottom_nav = BottomNav()
        layout.addWidget(
        self.bottom_nav,
        alignment=Qt.AlignCenter
        )
        self.bottom_nav.pageChanged.connect(self.stack.setCurrentIndex)