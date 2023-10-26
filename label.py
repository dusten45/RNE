from PyQt6.QtWidgets import QLabel, QSizePolicy
from PyQt6.QtGui import QFont

class Label(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.setFont(QFont(pointSize=20))