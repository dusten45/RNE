#Import modules
from analyze import Run
from lineedit import Lineedit
from button import Button
from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox, QGridLayout, QFileDialog
import os, traceback

#Define Program
class Program(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 400)

        self.check = False

        # Display Window
        self.label_File_Path = QLabel("File Path : ")

        self.lineedit_File_Path = Lineedit('C:/example_file/example.xlsx', False, self.textChanged)

        self.label_Column = QLabel("Column Number of Gene IDs in Info Sheet : ")
        
        self.lineedit_Column = Lineedit('', True, self.textChanged)

        self.label_ensembl = QLabel("If there is Ensembl Id : ")

        self.lineedit_ensembl = Lineedit('True : 1 / False : 0', True, self.textChanged)

        self.label_sheetname = QLabel("Sheet Names : ")

        self.lineedit_datasheetname = Lineedit('Name of the data sheet', False, self.textChanged)
        
        self.lineedit_infosheetname = Lineedit('Name of the info sheet (gene length, symbol, etc.)', False, self.textChanged)
        self.label_check = QLabel("State : Not Ready")

        sheetnameLayout = QGridLayout()

        sheetnameLayout.addWidget(self.lineedit_datasheetname, 0, 0)
        sheetnameLayout.addWidget(self.lineedit_infosheetname, 0, 1)
        
        # Button Creation and Placement
        btnLayout = QGridLayout()

        self.button_analyze = Button("Analyze", self.buttonClicked)
        self.button_analyze.setDisabled(True)
        self.button_findfile = Button("Find File", self.buttonClicked)

        btnLayout.addWidget(self.button_analyze, 0, 0)
        btnLayout.addWidget(self.button_findfile, 0, 1)

        # Layout
        mainLayout = QGridLayout()

        mainLayout.addWidget(self.label_File_Path, 0, 0)
        mainLayout.addWidget(self.lineedit_File_Path, 1, 0)
        mainLayout.addWidget(self.label_ensembl, 2, 0)
        mainLayout.addWidget(self.lineedit_ensembl, 3, 0)
        mainLayout.addWidget(self.label_Column, 4, 0)
        mainLayout.addWidget(self.lineedit_Column, 5, 0)
        mainLayout.addWidget(self.label_sheetname, 6, 0)
        mainLayout.addLayout(sheetnameLayout, 7, 0)
        mainLayout.addWidget(self.label_check, 8, 0)
        mainLayout.addLayout(btnLayout, 9, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle("Cancer Data Analyser")


    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        ensembl_exist = False

        if self.lineedit_ensembl == 1:
            ensembl_exist = True

        if key == 'Analyze':
            try:
                if self.check == False:
                    QMessageBox.about(self, "Error", "Fill Every Box")
                elif os.path.splitext(self.lineedit_File_Path.text())[1] != ".xlsx":
                    QMessageBox.about(self, "Error", ".xlsx File Only")
                else:
                    Run(self.lineedit_File_Path.text(), self.lineedit_datasheetname.text(), self.lineedit_infosheetname.text(), ensembl_exist, self.lineedit_Column.text())
                    QMessageBox.about(self, 'Done!', 'Check \'result.csv\' file.')
            except:
                QMessageBox.about(self, 'Error', traceback.format_exc())
                print(traceback.format_exc())
            
        elif key == "Find File":
            try:
                frame = QFileDialog.getOpenFileName(self, "Open File", './')
                if frame[0].endswith(".xlsx"):
                    self.lineedit_File_Path.setText(frame[0])
                elif frame[0]:
                    QMessageBox.about(self, "Error", ".xlsx File Only")
                else:
                    QMessageBox.about(self, "Error", 'Failed to Open File')
            except:
                QMessageBox.about(self, 'Error', 'Failed to Open explorer.exe')



    def closeEvent(self, event):
        chk = QMessageBox.warning(self, "Exit", 'Are you sure to exit program?', QMessageBox.StandardButton.Yes| QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if chk == QMessageBox.StandardButton.Yes:
            event.accept()
        elif chk == QMessageBox.StandardButton.No:
            event.ignore()


    def textChanged(self):
        self.check = False
        if self.lineedit_Column.text() != "":
            if self.lineedit_datasheetname.text() != "":
                if self.lineedit_File_Path.text() != "":
                    if self.lineedit_infosheetname.text() != '':
                        self.check = True

        if self.check:
            self.label_check.setText("State : Ready")
            self.button_analyze.setDisabled(False)
        else:
            self.label_check.setText("State : Not Ready")
            self.button_analyze.setDisabled(True)