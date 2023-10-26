# Import modules
from PyQt6.QtWidgets import QMessageBox, QGridLayout
from pages import Pages


# Define Layouts
class Layouts(Pages):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 400)
        self.setStyleSheet('background:rgb(255,255,255)')

        # Widgets Placement
        checkLayout = QGridLayout()
        checkLayout.addWidget(self.lbInfoCheck, 0, 0)
        checkLayout.addWidget(self.check_ensembl, 0, 1)

        ensemblLayout = QGridLayout()
        ensemblLayout.addWidget(self.lineedit_kind, 0, 1)
        ensemblLayout.addLayout(checkLayout, 0, 0)

        sheetnameLayout = QGridLayout()
        sheetnameLayout.addWidget(self.lineedit_datasheetname, 0, 0)
        sheetnameLayout.addWidget(self.lineedit_infosheetname, 0, 1)

        btnLayout = QGridLayout()
        btnLayout.addWidget(self.button_analyze, 0, 0)
        btnLayout.addWidget(self.button_findfile, 0, 1)

        # Main Layout
        mainLayout = QGridLayout()

        mainLayout.addWidget(self.lbFilePath, 0, 0)
        mainLayout.addWidget(self.lineedit_File_Path, 1, 0)
        mainLayout.addLayout(ensemblLayout, 2, 0)
        mainLayout.addWidget(self.lbInfoCol, 3, 0)
        mainLayout.addWidget(self.lineedit_Column, 4, 0)
        mainLayout.addWidget(self.lbSheetNames, 5, 0)
        mainLayout.addLayout(sheetnameLayout, 6, 0)
        mainLayout.addWidget(self.lbStateCheck, 7, 0)
        mainLayout.addLayout(btnLayout, 8, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle("Cancer Data Analyser")


    # Close Program
    def closeEvent(self, event):
        chk = self.messagebox.warning(self, "Exit", 'Are you sure to exit program?', QMessageBox.StandardButton.Yes| QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if chk == QMessageBox.StandardButton.Yes:
            event.accept()
        elif chk == QMessageBox.StandardButton.No:
            event.ignore()