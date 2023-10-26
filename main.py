from pages import Pages
from PyQt6.QtWidgets import QApplication
import sys

#Start program
def main():
    app = QApplication(sys.argv)
    pr = Pages()
    pr.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
