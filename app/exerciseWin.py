from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

from app.style import set_style_form
from classes.new_widgets import *
from database.scripts.db import Data


class ExerciseWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.db = Data('database/geometry.db')
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
        self.right_answers = DroppableGroupBox('Правильные ответы')
        self.all_answers = DroppableGroupBox('Варианты ответов')
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
        set_style_form(self.title, self.right_answers, self.all_answers, self.ok)

    def set_image(self, image):
        self.pixmap = QPixmap.fromImage(QImage.fromData(QByteArray(image)))
        self.image.setPixmap(self.pixmap)

    def check_answer(self):
        pass

    def load_question(self):
        task = self.db.get_task(1)
        self.set_image(task[0][3])
        self.title.setText(task[0][0])
        self.answers = list()
        for answer in task:
            label = DraggableLabel(answer[1], self.all_answers)
            set_style_label(label)
            self.all_answers.layout().addWidget(label)
            self.answers.append(label)
