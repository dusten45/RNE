# Import modules
from analyze import Run
from lineedit import Lineedit
from button import Button
from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox, QFileDialog, QCheckBox
import os, traceback

# Define Widgets
class Widgets(QWidget):
    def __init__(self):
        super().__init__()
        self.check : bool
        self.messagebox = QMessageBox()

        self.lbFilePath = QLabel("File Path : ")
        self.lbInfoCol = QLabel("Column Number of Gene IDs in Info Sheet : ")
        self.lbInfoCheck = QLabel("If there is gene length : ")
        self.lbSheetNames = QLabel("Sheet Names : ")
        self.lbStateCheck = QLabel("State : Not Ready")

        self.leFilePath = Lineedit('C:/example_file/example.xlsx', False, self.textChanged)
        self.leInfoKind = Lineedit('ensembl : 0 / symbol : 1', True, self.textChanged)
        self.leInfoCol = Lineedit('', True, self.textChanged)
        self.leDataSheetName = Lineedit('Name of the data sheet', False, self.textChanged)
        self.leInfoSheetName = Lineedit('Name of the info sheet (gene length, symbol, etc.)', False, self.textChanged)

        self.chkboxInfoCheck = QCheckBox()

        self.btnAnalyze = Button(self.Analyze, 'Analyze.bmp')
        self.btnFindFile = Button(self.Findfile, 'Find File.bmp')


    # Callback Analyze Button
    def Analyze(self):
        try:
            if self.check == False:
                QMessageBox.about(self, "Error", "Fill Every Box")
            elif os.path.splitext(self.leFilePath.text())[1] != ".xlsx":
                QMessageBox.about(self, "Error", ".xlsx File Only")
            else:
                if self.chkboxInfoCheck.isChecked():
                    Run(self.leFilePath.text(), self.leDataSheetName.text(), self.leInfoSheetName.text(), self.chkboxInfoCheck.isChecked(), int(self.leInfoCol.text()), 0)
                else:
                    Run(self.leFilePath.text(), self.leDataSheetName.text(), '', self.chkboxInfoCheck.isChecked(), 0, int(self.leInfoKind.text()))
                QMessageBox.about(self, 'Done!', 'Check \'result.csv\' file.')
        except:
            QMessageBox.about(self, 'Error', traceback.format_exc())


    # Callback Finding File Button
    def Findfile(self):   
        try:
            frame = QFileDialog.getOpenFileName(self, "Open File", './')
            if frame[0].endswith(".xlsx"):
                self.leFilePath.setText(frame[0])
            elif frame[0]:
                QMessageBox.about(self, "Error", ".xlsx File Only")
            else:
                QMessageBox.about(self, "Error", 'Failed to Open File')
        except:
            QMessageBox.about(self, 'Error', 'Failed to Open explorer.exe')


    # Callback Lineedit
    def textChanged(self):
        self.check = False
        if self.leFilePath.text() != "":
            if self.leDataSheetName.text() != "":
                if self.chkboxInfoCheck.isChecked():
                    if self.leInfoSheetName.text() != '':
                        if self.leInfoCol.text() != "":
                            self.check = True

                elif self.leInfoKind.text() != '':
                    self.check = True

        if self.check:
            self.lbStateCheck.setText("State : Ready")
        else:
            self.lbStateCheck.setText("State : Not Ready")