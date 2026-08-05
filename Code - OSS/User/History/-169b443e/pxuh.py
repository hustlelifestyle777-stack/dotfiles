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
        layout.addStretch()
