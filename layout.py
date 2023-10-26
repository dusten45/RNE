# Import modules
from PyQt6.QtWidgets import QMessageBox, QGridLayout
from widgets import Widgets


# Define Layouts
class Layouts(Widgets):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 400)
        self.setStyleSheet('background:rgb(255,255,255)')

        self.pgFilePath = QGridLayout()
        self.pgFilePath.addWidget(self.chkboxFilePath, 0, 0)
        self.pgFilePath.addWidget(self.lbFilePath, 1, 0)
        self.pgFilePath.addWidget(self.leFilePath, 2, 0)
        self.pgFilePath.addWidget(self.leInfoFilePath, 3, 0)

        self.pgData = QGridLayout()
        self.pgData.addWidget(self.lbSheetNames, 0, 0)
        self.pgData.addWidget(self.leDataSheetName, 1, 0)

        self.pgInfo = QGridLayout()
        self.pgInfo.addWidget(self.lbInfoCheck, 0, 0)
        self.pgInfo.addWidget(self.rbtnInfoSymb, 1, 0)
        self.pgInfo.addWidget(self.rbtnInfoSymb, 2, 0)
        layout = QGridLayout()
        layout.addWidget(self.leInfoCol, 0, 1)
        layout.addWidget(self.leInfoSheetName, 0, 0)
        self.pgInfo.addLayout(layout, 3, 0)

        self.pgHome = QGridLayout()

        self.setWindowTitle("Cancer Data Analyser")


    # Close Program
    def closeEvent(self, event):
        chk = self.messagebox.warning(self, "Exit", 'Are you sure to exit program?', QMessageBox.StandardButton.Yes| QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if chk == QMessageBox.StandardButton.Yes:
            event.accept()
        elif chk == QMessageBox.StandardButton.No:
            event.ignore()