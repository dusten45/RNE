from widgets import Widgets
from lineedit import Lineedit
from button import Button
from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox, QFileDialog, QCheckBox

class Pages(Widgets):
    def __init__(self):
        super().__init__()

        btnFilePath = Button(self.changePage(0), '')
        btnData = Button(self.changePage(1), '')
        btnInfo = Button(self.changePage(2), '')
        btnHome = Button(self.changePage(None), '')



    def changePage(self, page):
        if page == 0:
            pass

        elif page == 1:
            pass

        elif page == 2:
            pass

        else:
            pass