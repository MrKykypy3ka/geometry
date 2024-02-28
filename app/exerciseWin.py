from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox
from PyQt5.QtGui import QIcon, QPixmap, QImage, QFont


class ExerciseWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_question()

    def init_ui(self):
        self.setWindowTitle('Геометр')
        self.resize(1280, 720)
        self.setWindowIcon(QIcon('resources/icons/ico.png'))
        main_l = QHBoxLayout()
        v_l1 = QVBoxLayout()
        v_l2 = QVBoxLayout()
        self.title = QLabel('Вопрос')
        self.image = QLabel()
        self.image.setStyleSheet('border: 1px solid black;')
        self.right_answers = QGroupBox('Правильные ответы')
        self.all_answers = QGroupBox('Варианты ответов')
        self.ok = QPushButton('Проверить')
        v_l1.addWidget(self.title, 1)
        v_l1.addWidget(self.image, 7, alignment=Qt.AlignCenter)
        v_l1.addWidget(self.right_answers, 3)
        v_l2.addWidget(self.all_answers, 6)
        v_l2.addWidget(self.ok, 1)
        main_l.addLayout(v_l1, 4)
        main_l.addLayout(v_l2, 2)
        self.setLayout(main_l)
        self.ok.clicked.connect(self.check_answer)
        self.set_style(self.title, self.right_answers, self.all_answers, self.ok)

    def set_image(self):
        self.picture = QImage('resources/images/1.png')
        self.pixmap = QPixmap.fromImage(self.picture)
        self.image.setPixmap(self.pixmap)

    def check_answer(self):
        pass

    def load_question(self):
        self.set_image()
        self.title.setText('Тут долне быть какой нибудь вопрос про сечение на рисунке')

    def set_style(self, *args):
        for widget in args:
            widget.setFont(QFont('Impact', 14))