from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QComboBox
from database.scripts.db import Data


class ConfiguratorAWin(QWidget):
    def __init__(self):
        super().__init__()
        self.db = Data('database/geometry.db')
        self.db.get_all_topic()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Геометр')
        self.resize(640, 0)
        self.setWindowIcon(QIcon('resources/icons/ico.png'))
        self.title = QLineEdit()
        self.title.setPlaceholderText('Напишите утверждение')
        self.group_name = QLabel('К какой теме относится утверждение:')
        self.group = QComboBox()
        self.group.addItems([x[1] for x in self.db.data])
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
        self.ok.clicked.connect(self.write_answer)

    def write_answer(self):
        topic_id = [elem[0] for elem in self.db.data if elem[1] == self.group.currentText()][0]
        if self.db.add_statement(topic_id=topic_id, text=self.title.text()):
            self.close()
        else:
            print('Ошибка записи данных')
