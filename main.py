from PyQt5.QtWidgets import QApplication, QWidget
from app.mainWin import MainWin
import sys


def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
