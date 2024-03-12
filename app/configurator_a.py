from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QComboBox
from database.scripts.db import Data


class ConfiguratorAWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.db = Data('database/geometry.db')

    def init_ui(self):
        self.setWindowTitle('Геометр')
        self.resize(640, 0)
        self.setWindowIcon(QIcon('resources/icons/ico.png'))
        self.title = QLineEdit()
        self.title.setPlaceholderText('Напишите ответ')
        self.group_name = QLabel('К какой группе относится утверждение')
        self.group = QComboBox()
        self.ok = QPushButton('Добавить')
        main_l = QVBoxLayout()
        main_l.addStretch()
        main_l.addWidget(self.title)

        h_tatle = QHBoxLayout()
        h_tatle.addWidget(self.group_name, 2)
        h_tatle.addStretch(10)
        main_l.addLayout(h_tatle)
        main_l.addWidget(self.group)

        h_ok = QHBoxLayout()
        h_ok.addStretch(10)
        h_ok.addWidget(self.ok, 2)

        main_l.addLayout(h_ok, 1)
        main_l.addStretch()
        self.setLayout(main_l)
