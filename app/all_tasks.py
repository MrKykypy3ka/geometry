from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel, QComboBox
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import QSize, QByteArray
from database.scripts.db import Data
from app.exerciseWin import ExerciseWin


def create_button(text, image):
    button = QPushButton()
    button.my_text = text
    button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    button.setIcon(QIcon(QPixmap.fromImage(QImage.fromData(QByteArray(image)))))
    button.setIconSize(QSize(150, 150))
    return button


class AllTasks(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.db = Data('database/geometry.db')
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Геометр')
        # self.resize(300, 200)
        self.setGeometry(400, 50, 300, 200)
        self.setWindowIcon(QIcon('resources/icons/ico.png'))
        title = QLabel('Темы уроков:')
        self.h_layouts = list()
        self.topics = QComboBox()
        self.db.get_all_topic()
        self.topics.addItems([elem[1] for elem in self.db.data])
        self.main_vl = QVBoxLayout()
        self.main_vl.addWidget(title)
        self.main_vl.addWidget(self.topics)
        self.db.get_all_tasks()
        self.load_tasks()
        self.setLayout(self.main_vl)
        self.topics.currentTextChanged.connect(self.load_tasks)

    def show_task(self):
        self.win_e = ExerciseWin(self.sender().my_text)
        self.win_e.show()
        self.hide()

    def load_tasks(self):
        for line in self.h_layouts:
            for i in reversed(range(line.count())):
                line.itemAt(i).widget().setParent(None)
        self.db.get_all_topic()
        topics = self.db.data
        current_topic = [elem[0] for elem in topics if elem[1] == self.topics.currentText()][0]
        self.db.get_all_tasks()
        tasks = [elem for elem in self.db.data if elem[3] == current_topic]
        count_lines = [3 for _ in range(len(tasks) // 3)] + [len(tasks) % 3]
        for i in range(len(tasks) // 3 + 1):
            self.h_layouts.append(QHBoxLayout())
            for j in range(count_lines[i]):
                button = create_button(tasks[(i * 3) + j][0], tasks[(i * 3) + j][2])
                button.clicked.connect(self.show_task)
                self.h_layouts[-1].addWidget(button)
            self.main_vl.addLayout(self.h_layouts[-1])
        self.update()

