from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from app.configurator_q import ConfiguratorQWin
from app.configurator_a import ConfiguratorAWin


class RedactorWin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Геометр')
        self.resize(300, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('resources/icons/ico.png'))
        self.answers_btn = QPushButton('Добавить ответы')
        self.questions_btn = QPushButton('Добавить вопросы')
        main_vl = QVBoxLayout()
        main_vl.addStretch()
        main_vl.addWidget(self.answers_btn)
        main_vl.addWidget(self.questions_btn)
        main_vl.addStretch()
        self.setLayout(main_vl)
        self.answers_btn.clicked.connect(self.show_answers)
        self.questions_btn.clicked.connect(self.show_questions)

    def show_answers(self):
        self.win_a = ConfiguratorAWin()
        self.win_a.show()
        self.hide()

    def show_questions(self):
        self.win_q = ConfiguratorQWin()
        self.win_q.show()
        self.hide()
