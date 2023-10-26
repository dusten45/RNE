# Import modules
from analyze import Run
from lineedit import Lineedit
from button import Button
from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox, QFileDialog, QCheckBox, QRadioButton
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
        self.leInfoFilePath = Lineedit('Info File Path', False, self.textChanged)
        self.leInfoCol = Lineedit('', True, self.textChanged)
        self.leDataSheetName = Lineedit('Name of the data sheet', False, self.textChanged)
        self.leInfoSheetName = Lineedit('Name of the info sheet (gene length, symbol, etc.)', False, self.textChanged)

        self.chkboxInfo = QCheckBox()
        self.chkboxInfo.stateChanged.connect(self.stateChanged)
        self.chkboxFilePath = QCheckBox()
        self.chkboxFilePath.stateChanged.connect(self.stateChanged)

        self.btnAnalyze = Button(self.Analyze, 'Analyze.bmp')
        self.btnFindFile = Button(self.Findfile, 'Find File.bmp')

        self.rbtnInfoSymb = QRadioButton('Symbol')
        self.rbtnInfoEnsm = QRadioButton('Ensembl ID')


    # Callback Analyze Button
    def Analyze(self):
        try:
            if self.check == False:
                QMessageBox.about(self, "Error", "Fill Every Box")
            elif os.path.splitext(self.leFilePath.text())[1] != ".xlsx":
                QMessageBox.about(self, "Error", ".xlsx File Only")
            else:
                if self.chkboxInfo.isChecked():
                    Run(self.leFilePath.text(), self.leDataSheetName.text(), self.leInfoSheetName.text(), self.chkboxInfo.isChecked(), int(self.leInfoCol.text()), 0, self.leInfoFilePath.text())
                else:
                    Run(self.leFilePath.text(), self.leDataSheetName.text(), '', self.chkboxInfo.isChecked(), 0, int(self.rbtnInfoSymb.isChecked()), self.leInfoFilePath.text())
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
                if self.chkboxInfo.isChecked():
                    if self.leInfoSheetName.text() != '':
                        if self.leInfoCol.text() != "":
                            if self.chkboxFilePath.isChecked():
                                if self.leInfoFilePath != "":
                                    self.check = True

                            else:
                                self.check = True

                elif self.leInfoKind.text() != '':
                    if self.chkboxFilePath.isChecked():
                        if self.leInfoFilePath != "":
                            self.check = True

                    else:
                        self.check = True


        if self.check:
            self.lbStateCheck.setText("State : Ready")
        else:
            self.lbStateCheck.setText("State : Not Ready")

        
    def stateChanged(self):
        if self.chkboxFilePath.isChecked():
            self.leInfoFilePath.setText('')
            self.leInfoFilePath.setVisible(True)
        else:
            self.leInfoFilePath.setVisible(False)
            self.leInfoFilePath.setText(self.leFilePath)

        if self.chkboxInfo.isChecked():
            self.rbtnInfoEnsm.setVisible(True)
            self.rbtnInfoSymb.setVisible(True)
            self.leInfoSheetName.setVisible(False)
            self.leInfoCol.setVisible(False)
        else:
            self.rbtnInfoSymb.setVisible(False)
            self.rbtnInfoEnsm.setVisible(False)
            self.leInfoSheetName.setVisible(True)
            self.leInfoCol.setVisible(True)