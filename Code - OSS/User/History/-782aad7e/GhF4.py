from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget
from PySide6.QtCore import Qt
from ui.home_page import HomePage
from ui.live_page import LivePage
from ui.backtest_page import BacktestPage
from ui.forms.live_trade import LiveTradePage
from ui.forms.backtest import BacktestTradePage
from widgets.bottom_nav import BottomNav
from ui.scroll_page import ScrollPage

class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TRD KAIZEN")
        self.resize(1200, 800)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 24)
        layout.setSpacing(0)

        self.stack = QStackedWidget()

        self.home_page = HomePage()
        self.live_page = LivePage()
        self.backtest_page = BacktestPage()
        self.trade_page = LiveTradePage()
        self.backtest_trade_page = BacktestTradePage()

        self.home_scroll = ScrollPage(self.home_page)
        self.live_scroll = ScrollPage(self.live_page)
        self.backtest_scroll = ScrollPage(self.backtest_page)
        self.trade_scroll = ScrollPage(self.trade_page)
        self.backtest_trade_scroll = ScrollPage(self.backtest_trade_page)

        self.live_page.openTradePage.connect(
            lambda: self.stack.setCurrentWidget(self.trade_scroll)
        )

        self.backtest_page.openBacktestPage.connect(
            lambda: self.stack.setCurrentWidget(self.backtest_trade_scroll)
        )

        self.stack.addWidget(self.home_scroll)
        self.stack.addWidget(self.live_scroll)
        self.stack.addWidget(self.backtest_scroll)
        self.stack.addWidget(self.trade_scroll)
        self.stack.addWidget(self.backtest_trade_scroll)

        layout.addWidget(self.stack, 1)
        self.bottom_nav = BottomNav()
        layout.addWidget(
        self.bottom_nav,
        alignment=Qt.AlignCenter
        )
        self.bottom_nav.pageChanged.connect(self.stack.setCurrentIndex)