from PyQt6.QtWidgets import QToolButton, QSizePolicy
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

#Define button
class Button(QToolButton):
    def __init__(self, callback, filename):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.clicked.connect(callback)
        if filename != '':
            self.setImage(filename)

    
    def setImage(self, filename):
        self.setStyleSheet('border:none')
        icon = QIcon()
        icon.addFile(f'./image/{filename}')
        self.setIcon(icon)
        self.setIconSize(QSize(350, 150))


    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 30)
        size.setWidth(max(size.width(), size.height()))
        return size