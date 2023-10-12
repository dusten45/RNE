# Import modules
from PyQt6.QtWidgets import QMessageBox, QGridLayout
from widgets import Widgets

# Define Program
class Program(Widgets):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 400)

        # Widgets Placement
        checkLayout = QGridLayout()
        checkLayout.addWidget(self.label_ensembl, 0, 0)
        checkLayout.addWidget(self.check_ensembl, 0, 1)

        sheetnameLayout = QGridLayout()
        sheetnameLayout.addWidget(self.lineedit_datasheetname, 0, 0)
        sheetnameLayout.addWidget(self.lineedit_infosheetname, 0, 1)

        btnLayout = QGridLayout()
        btnLayout.addWidget(self.button_analyze, 0, 0)
        btnLayout.addWidget(self.button_findfile, 0, 1)

        # Main Layout
        mainLayout = QGridLayout()

        mainLayout.addWidget(self.label_File_Path, 0, 0)
        mainLayout.addWidget(self.lineedit_File_Path, 1, 0)
        mainLayout.addLayout(checkLayout, 2, 0)
        mainLayout.addWidget(self.lineedit_kind, 2, 1)
        mainLayout.addWidget(self.label_Column, 4, 0)
        mainLayout.addWidget(self.lineedit_Column, 5, 0)
        mainLayout.addWidget(self.label_sheetname, 6, 0)
        mainLayout.addLayout(sheetnameLayout, 7, 0)
        mainLayout.addWidget(self.label_check, 8, 0)
        mainLayout.addLayout(btnLayout, 9, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle("Cancer Data Analyser")


    # Close Program
    def closeEvent(self, event):
        chk = QMessageBox.warning(self, "Exit", 'Are you sure to exit program?', QMessageBox.StandardButton.Yes| QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if chk == QMessageBox.StandardButton.Yes:
            event.accept()
        elif chk == QMessageBox.StandardButton.No:
            event.ignore()