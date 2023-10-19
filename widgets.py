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

        self.label_File_Path = QLabel("File Path : ")
        self.label_Column = QLabel("Column Number of Gene IDs in Info Sheet : ")
        self.label_ensembl = QLabel("If there is Ensembl Id : ")
        self.label_sheetname = QLabel("Sheet Names : ")
        self.label_check = QLabel("State : Not Ready")

        self.lineedit_File_Path = Lineedit('C:/example_file/example.xlsx', False, self.textChanged)
        self.lineedit_kind = Lineedit('ensembl : 0 / symbol : 1', True, self.textChanged)
        self.lineedit_Column = Lineedit('', True, self.textChanged)
        self.lineedit_datasheetname = Lineedit('Name of the data sheet', False, self.textChanged)
        self.lineedit_infosheetname = Lineedit('Name of the info sheet (gene length, symbol, etc.)', False, self.textChanged)

        self.check_ensembl = QCheckBox()

        self.button_analyze = Button("Analyze", self.buttonClicked)
        self.button_findfile = Button("Find File", self.buttonClicked)


    # Callback Button
    def buttonClicked(self):
        button = self.sender()
        key = button.text() # type: ignore

        if key == 'Analyze':
            try:
                if self.check == False:
                    QMessageBox.about(self, "Error", "Fill Every Box")
                elif os.path.splitext(self.lineedit_File_Path.text())[1] != ".xlsx":
                    QMessageBox.about(self, "Error", ".xlsx File Only")
                else:
                    if self.check_ensembl.isChecked():
                        Run(self.lineedit_File_Path.text(), self.lineedit_datasheetname.text(), self.lineedit_infosheetname.text(), self.check_ensembl.isChecked(), int(self.lineedit_Column.text()), 0)
                    else:
                        Run(self.lineedit_File_Path.text(), self.lineedit_datasheetname.text(), '', self.check_ensembl.isChecked(), 0, int(self.lineedit_kind.text()))
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


    # Callback Lineedit
    def textChanged(self):
        self.check = False
        if self.lineedit_File_Path.text() != "":
            if self.lineedit_datasheetname.text() != "":
                if self.check_ensembl.isChecked():
                    if self.lineedit_infosheetname.text() != '':
                        if self.lineedit_Column.text() != "":
                            self.check = True

                elif self.lineedit_kind.text() != '':
                    self.check = True

        if self.check:
            self.label_check.setText("State : Ready")
        else:
            self.label_check.setText("State : Not Ready")