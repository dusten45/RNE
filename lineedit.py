from PyQt6.QtWidgets import QLineEdit, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator

#Define lineedit
class Lineedit(QLineEdit):
    def __init__(self, text, i_vali, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setPlaceholderText(text)
        self.textChanged.connect(callback)

        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setStyleSheet("background-color: #FFFFFF;"
                            "border-style: solid;"
                            "border-width: 1px;"
                            "border-color: #000000;"
                            "color: black;")
        if i_vali:
            self.setValidator(QIntValidator())


    def sizeHint(self):
        size = super(Lineedit, self).sizeHint()
        size.setHeight(size.height() + 5)
        size.setWidth(max(size.width(), size.height()))
        return size