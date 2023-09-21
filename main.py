from GUI import Program
from PyQt6.QtWidgets import QApplication
import sys

#Start program
def main():
    app = QApplication(sys.argv)
    pr = Program()
    pr.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
