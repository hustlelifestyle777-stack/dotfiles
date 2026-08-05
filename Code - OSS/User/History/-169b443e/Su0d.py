from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QTimeEdit,
    QSpinBox
)
from PySide6.QtCore import QDate, QTime


class TradeForm(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.setMinimumWidth(800)
        layout.setContentsMargins(30, 25, 30, 25)
        layout.setSpacing(15)

        # ====================================
        # SECTION 1 - Trade Information
        # ====================================

        trade_box = QGroupBox("1. Trade Information")
        trade_layout = QVBoxLayout()

        # Date
        trade_layout.addWidget(QLabel("Date"))
        self.date = QDateEdit()
        self.date.setDate(QDate.currentDate())
        trade_layout.addWidget(self.date)

        # Day
        trade_layout.addWidget(QLabel("Day"))
        self.day = QLineEdit()
        self.day.setReadOnly(True)
        self.day.setText(QDate.currentDate().toString("dddd"))
        trade_layout.addWidget(self.day)

        # Entry Time
        trade_layout.addWidget(QLabel("Entry Time"))
        self.entry_time = QTimeEdit()
        self.entry_time.setTime(QTime.currentTime())
        trade_layout.addWidget(self.entry_time)

        # Exit Time
        trade_layout.addWidget(QLabel("Exit Time"))
        self.exit_time = QTimeEdit()
        trade_layout.addWidget(self.exit_time)

        # Instrument
        trade_layout.addWidget(QLabel("Instrument"))
        self.instrument = QLineEdit()
        trade_layout.addWidget(self.instrument)

        # Direction
        trade_layout.addWidget(QLabel("Direction"))
        self.direction = QComboBox()
        self.direction.addItems(["CE", "PE"])
        trade_layout.addWidget(self.direction)

        # Entry Price
        trade_layout.addWidget(QLabel("Entry Price"))
        self.entry_price = QLineEdit()
        trade_layout.addWidget(self.entry_price)

        # Exit Price
        trade_layout.addWidget(QLabel("Exit Price"))
        self.exit_price = QLineEdit()
        trade_layout.addWidget(self.exit_price)

        # Quantity
        trade_layout.addWidget(QLabel("Quantity"))
        self.quantity = QSpinBox()
        self.quantity.setRange(1, 1000000)
        trade_layout.addWidget(self.quantity)

        # Strike Price
        trade_layout.addWidget(QLabel("Strike Price"))
        self.strike_price = QLineEdit()
        trade_layout.addWidget(self.strike_price)

        # Expiry Date
        trade_layout.addWidget(QLabel("Expiry Date"))
        self.expiry_date = QDateEdit()
        self.expiry_date.setCalendarPopup(True)
        self.expiry_date.setDate(QDate.currentDate())
        trade_layout.addWidget(self.expiry_date)

        trade_box.setLayout(trade_layout)

        layout.addWidget(trade_box)
                # ==========================================
        # SECTION 2 - Market Context
        # ==========================================

        market_box = QGroupBox("2. Market Context")
        market_layout = QVBoxLayout()

        # Previous Day Close
        market_layout.addWidget(QLabel("Previous Day Close"))
        self.previous_close = QLineEdit()
        market_layout.addWidget(self.previous_close)

        # Premarket Settlement
        market_layout.addWidget(QLabel("Premarket Settlement"))
        self.premarket_settlement = QLineEdit()
        market_layout.addWidget(self.premarket_settlement)

        # Gap
        market_layout.addWidget(QLabel("Gap"))
        self.gap = QComboBox()
        self.gap.addItems(["Gap Up", "Gap Down", "Flat"])
        market_layout.addWidget(self.gap)

        # Expiry Day
        market_layout.addWidget(QLabel("Expiry Day"))
        self.expiry_day = QComboBox()
        self.expiry_day.addItems(["Yes", "No"])
        market_layout.addWidget(self.expiry_day)

        # VIX
        market_layout.addWidget(QLabel("VIX"))
        self.vix = QLineEdit()
        market_layout.addWidget(self.vix)

        # Seller Dominated
        market_layout.addWidget(QLabel("Seller Dominated"))
        self.seller_dominated = QComboBox()
        self.seller_dominated.addItems(["Yes", "No"])
        market_layout.addWidget(self.seller_dominated)

        market_box.setLayout(market_layout)

        layout.addWidget(market_box)
        
                # =====================================
        # SECTION 3 -- Trade Setup
        # =====================================

        setup_box = QGroupBox("3. Trade Setup")
        setup_layout = QVBoxLayout()

        # Strategy
        setup_layout.addWidget(QLabel("Strategy"))
        self.strategy = QLineEdit()
        setup_layout.addWidget(self.strategy)

        # Timeframe
        setup_layout.addWidget(QLabel("Timeframe"))
        self.timeframe = QLineEdit()
        setup_layout.addWidget(self.timeframe)

        # Entry Confirmation
        setup_layout.addWidget(QLabel("Entry Confirmation"))
        self.confirmation = QLineEdit()
        setup_layout.addWidget(self.confirmation)

        # Reason for Entry
        setup_layout.addWidget(QLabel("Reason for Entry"))
        self.reason = QLineEdit()
        setup_layout.addWidget(self.reason)

        setup_box.setLayout(setup_layout)
        layout.addWidget(setup_box)

                # =====================================
        # SECTION 4 -- Trade Execution
        # =====================================

        execution_box = QGroupBox("4. Trade Execution")
        execution_layout = QVBoxLayout()

        # Entry Trigger
        execution_layout.addWidget(QLabel("Entry Trigger"))
        self.entry_trigger = QLineEdit()
        execution_layout.addWidget(self.entry_trigger)

        # Stop Loss
        execution_layout.addWidget(QLabel("Stop Loss"))
        self.stop_loss = QLineEdit()
        execution_layout.addWidget(self.stop_loss)

        # Target
        execution_layout.addWidget(QLabel("Target"))
        self.target = QLineEdit()
        execution_layout.addWidget(self.target)

        # Risk : Reward
        execution_layout.addWidget(QLabel("Risk : Reward"))
        self.risk_reward = QLineEdit()
        execution_layout.addWidget(self.risk_reward)

        # Capital Used
        execution_layout.addWidget(QLabel("Capital Used"))
        self.capital_used = QLineEdit()
        execution_layout.addWidget(self.capital_used)

        # Premium Paid
        execution_layout.addWidget(QLabel("Premium Paid"))
        self.premium_paid = QLineEdit()
        execution_layout.addWidget(self.premium_paid)

        execution_box.setLayout(execution_layout)
        layout.addWidget(execution_box)

        layout.addStretch()
