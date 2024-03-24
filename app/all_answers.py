from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy
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


class AllAnswers(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.db = Data('database/geometry.db')
        self.db.get_all_tasks()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Геометр')
        self.resize(300, 200)
        self.setWindowIcon(QIcon('resources/icons/ico.png'))
        main_vl = QVBoxLayout()
        h_layouts = list()
        count_lines = [3 for _ in range(len(self.db.data)//3)] + [len(self.db.data) % 3]
        for i in range(len(self.db.data)//3 + 1):
            h_layouts.append(QHBoxLayout())
            for j in range(count_lines[i]):
                button = create_button(self.db.data[(i * 3) + j][0], self.db.data[(i * 3) + j][2])
                button.clicked.connect(self.show_task)
                h_layouts[-1].addWidget(button)
            main_vl.addLayout(h_layouts[-1])
        self.setLayout(main_vl)

    def show_task(self):
        self.win_e = ExerciseWin(self.sender().my_text)
        self.win_e.show()
        self.hide()
