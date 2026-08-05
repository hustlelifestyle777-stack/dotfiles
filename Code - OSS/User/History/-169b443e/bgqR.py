from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QTimeEdit,
    QSpinBox,
    QFormLayout,
    QTextEdit
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

        # Stop Loss
        execution_layout.addWidget(QLabel("Stop Loss (Points)"))
        self.stop_loss = QLineEdit()
        execution_layout.addWidget(self.stop_loss)

        # Target
        execution_layout.addWidget(QLabel("Target (Points)"))
        self.target = QLineEdit()
        execution_layout.addWidget(self.target)

        # Risk : Reward (Auto)
        execution_layout.addWidget(QLabel("Risk : Reward"))
        self.risk_reward = QLineEdit()
        self.risk_reward.setReadOnly(True)
        execution_layout.addWidget(self.risk_reward)

        # Capital Used
        execution_layout.addWidget(QLabel("Capital Used"))
        self.capital_used = QLineEdit()
        execution_layout.addWidget(self.capital_used)

        # Entry Premium
        execution_layout.addWidget(QLabel("Entry Premium"))
        self.entry_premium = QLineEdit()
        execution_layout.addWidget(self.entry_premium)

        self.stop_loss.textChanged.connect(self.calculate_rr)
        self.target.textChanged.connect(self.calculate_rr)

        self.entry_price.textChanged.connect(self.calculate_result)
        self.exit_price.textChanged.connect(self.calculate_result)

        execution_box.setLayout(execution_layout)
        layout.addWidget(execution_box)

        # =====================================
        # SECTION 5 -- Trade Outcome
        # =====================================

        outcome_box = QGroupBox("5. Trade Outcome")
        outcome_layout = QVBoxLayout()

        # Exit Reason
        outcome_layout.addWidget(QLabel("Exit Reason"))
        self.exit_reason = QLineEdit()
        outcome_layout.addWidget(self.exit_reason)

        # P/L Points
        outcome_layout.addWidget(QLabel("P/L (Points)"))
        self.pl_points = QLineEdit()
        self.pl_points.setReadOnly(True)
        outcome_layout.addWidget(self.pl_points)

        # P/L Amount
        outcome_layout.addWidget(QLabel("P/L (₹)"))
        self.pl_amount = QLineEdit()
        self.pl_amount.setReadOnly(True)
        outcome_layout.addWidget(self.pl_amount)

        # Result
        outcome_layout.addWidget(QLabel("Result"))
        self.result = QLineEdit()
        self.result.setReadOnly(True)
        outcome_layout.addWidget(self.result)

        # Trade Quality
        outcome_layout.addWidget(QLabel("Trade Quality"))
        self.trade_quality = QComboBox()
        self.trade_quality.addItems(["A+", "A", "B", "C", "F"])
        outcome_layout.addWidget(self.trade_quality)

        outcome_box.setLayout(outcome_layout)
        layout.addWidget(outcome_box)

        # -----------------------------
        # Section 6 - Trade Review
        # -----------------------------
        review_box = QGroupBox("6. Trade Review")
        review_layout = QFormLayout()

        # Mistakes Made
        self.mistakes = QTextEdit()
        self.mistakes.setFixedHeight(60)
        review_layout.addRow("Mistakes Made", self.mistakes)

        # What Went Well
        self.what_went_well = QTextEdit()
        self.what_went_well.setFixedHeight(60)
        review_layout.addRow("What Went Well", self.what_went_well)

        # Improvements
        self.improvements = QTextEdit()
        self.improvements.setFixedHeight(60)
        review_layout.addRow("Improvements", self.improvements)

        # Key Lesson
        self.key_lesson = QTextEdit()
        self.key_lesson.setFixedHeight(60)
        review_layout.addRow("Key Lesson", self.key_lesson)

        review_box.setLayout(review_layout)
        layout.addWidget(review_box)

        # -----------------------------
        # Section 7 - Psychology
        # -----------------------------
        psychology_box = QGroupBox("7. Psychology")
        psychology_layout = QFormLayout()

        # Emotion Before Trade
        self.emotion_before = QComboBox()
        self.emotion_before.addItems([
            "Calm",
            "Confident",
            "Fearful",
            "Greedy",
            "FOMO",
            "Frustrated",
            "Neutral"
        ])
        psychology_layout.addRow("Emotion Before", self.emotion_before)

        # Emotion During Trade
        self.emotion_during = QComboBox()
        self.emotion_during.addItems([
            "Calm",
            "Confident",
            "Fearful",
            "Greedy",
            "FOMO",
            "Frustrated",
            "Neutral"
        ])
        psychology_layout.addRow("Emotion During", self.emotion_during)

        # Emotion After Trade
        self.emotion_after = QComboBox()
        self.emotion_after.addItems([
            "Satisfied",
            "Happy",
            "Disappointed",
            "Angry",
            "Relieved",
            "Neutral"
        ])
        psychology_layout.addRow("Emotion After", self.emotion_after)

        # Confidence (1-10)
        self.confidence = QSpinBox()
        self.confidence.setRange(1, 10)
        psychology_layout.addRow("Confidence", self.confidence)

        # Discipline (1-10)
        self.discipline = QSpinBox()
        self.discipline.setRange(1, 10)
        psychology_layout.addRow("Discipline", self.discipline)

        psychology_box.setLayout(psychology_layout)
        layout.addWidget(psychology_box)

        # -----------------------------
        # Section 8 - Journal
        # -----------------------------
        journal_box = QGroupBox("8. Journal")
        journal_layout = QVBoxLayout()

        self.journal = QTextEdit()
        self.journal.setPlaceholderText(
            "Write your complete trade journal here..."
        )
        self.journal.setFixedHeight(220)

        journal_layout.addWidget(self.journal)

        journal_box.setLayout(journal_layout)
        layout.addWidget(journal_box)

        # -----------------------------
        # Section 9 - Attachments
        # -----------------------------
        attachments_box = QGroupBox("9. Attachments")
        attachments_layout = QFormLayout()




    def calculate_rr(self):
        try:
            sl = float(self.stop_loss.text())
            target = float(self.target.text())

            if sl > 0:
                rr = target / sl
                self.risk_reward.setText(f"1 : {rr:.2f}")
            else:
                self.risk_reward.clear()

        except ValueError:
            self.risk_reward.clear()

    def calculate_result(self):
        pass

