from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
from PyQt5.QtGui import QIcon
from app.exerciseWin import ExerciseWin


class TasksWin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Геометр')
        self.resize(300, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('resources/icons/ico.png'))
        self.choice_btn = QPushButton('Выбрать урок')
        self.blitz_btn = QPushButton('Блиц')
        main_vl = QVBoxLayout()
        main_vl.addStretch()
        main_vl.addWidget(self.choice_btn)
        main_vl.addWidget(self.blitz_btn)
        main_vl.addStretch()
        self.setLayout(main_vl)
        self.choice_btn.clicked.connect(self.show_choice)
        self.blitz_btn.clicked.connect(self.show_blitz)

    def show_blitz(self):
        self.win = ExerciseWin()
        self.win.show()

    def show_choice(self):
        pass

    def closeEvent(self, event):
        QApplication.quit()