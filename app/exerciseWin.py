from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QMessageBox

from app.style import *
from classes.new_widgets import *
from database.scripts.db import Data


class ExerciseWin(QWidget):
    def __init__(self, task_id):
        super().__init__()
        self.init_ui()
        self.db = Data('database/geometry.db')
        self.task_id = task_id
        self.load_question()
        self.attempts = 0

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
        self.attempts += 1
        right_answers = [elem[1] for elem in self.db.data if elem[2] == 1]
        my_true_answers = 0
        my_false_answers = 0
        for answer in self.right_answers.findChildren(DraggableLabel):
            if answer.text() in right_answers:
                set_style_label_true(answer)
                my_true_answers += 1
            else:
                set_style_label_false(answer)
                my_false_answers += 1
        print(my_true_answers, my_false_answers)
        if len(right_answers) == my_true_answers and my_false_answers == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("Завершение")
            msg.setText(f"Задание выполнено!\nВы выбрали все правильные ответы.\nПопыток потрачено: {self.attempts}")
            msg.setIcon(QMessageBox.Information)
            if msg.exec_():
                self.close()

    def load_question(self):
        task = self.db.get_task(self.task_id)
        self.set_image(task[0][3])
        self.title.setText(task[0][0])
        self.answers = list()
        for answer in task:
            label = DraggableLabel(answer[1], self.all_answers)
            set_style_label(label)
            self.all_answers.layout().addWidget(label)
            self.answers.append(label)
