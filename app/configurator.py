from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QLineEdit, QListWidget, QComboBox
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
        self.title = QLineEdit()
        self.title.setPlaceholderText('Напишите задание')
        self.image = QLabel()
        self.button = QPushButton('Загрузить изображение')
        self.answers = QComboBox()
        all = QLabel('Все варианты')
        right = QLabel('Правильные варианты')
        self.all_answers = QListWidget('Все ответы')
        self.add_all = QPushButton('<-')
        self.answers = QListWidget()
        self.add_right = QPushButton('->')
        self.right_answers = QListWidget('Правильные ответов')

        self.ok = QPushButton('Записать')