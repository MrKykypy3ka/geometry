from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QLineEdit, QListWidget, QVBoxLayout, QFileDialog
from database.scripts.db import Data
from classes.new_widgets import ScaledPixmapLabel


class ConfiguratorQWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.db = Data('database/geometry.db')
        self.load_answers()

    def init_ui(self):
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle('Геометр')
        self.resize(1280, 720)
        self.setWindowIcon(QIcon('resources/icons/ico.png'))
        self.title = QLineEdit()
        self.title.setPlaceholderText('Напишите задание')
        self.image = ScaledPixmapLabel(alignment=Qt.AlignCenter)
        self.image.setStyleSheet('border: 1px solid black;')

        self.image.setScaledContents(True)

        self.open_image_btn = QPushButton('Загрузить изображение')
        all = QLabel('Все варианты')
        self.all_answers = QListWidget()
        self.add_all_btn = QPushButton('<-')
        self.del_all_btn = QPushButton('->')
        answers = QLabel('Ответы')
        self.answers = QListWidget()
        self.answers.setWordWrap(True)
        self.add_right_btn = QPushButton('->')
        self.del_right_btn = QPushButton('<-')
        right = QLabel('Правильные варианты')
        self.right_answers = QListWidget()
        self.ok = QPushButton('Записать')
        h_l = QHBoxLayout()
        v_l1 = QVBoxLayout()
        v_l2 = QVBoxLayout()
        v_l3 = QVBoxLayout()
        v_l4 = QVBoxLayout()
        v_l5 = QVBoxLayout()
        main_l = QVBoxLayout()
        main_l.addWidget(self.title, 2)
        main_l.addWidget(self.image, 4)

        h_load_image = QHBoxLayout()
        h_load_image.addWidget(self.open_image_btn, 2)
        h_load_image.addStretch(10)

        main_l.addLayout(h_load_image, 1)

        v_l1.addWidget(all)
        v_l1.addWidget(self.all_answers)
        v_l2.addWidget(answers)
        v_l2.addWidget(self.answers)
        v_l3.addWidget(right)
        v_l3.addWidget(self.right_answers)
        v_l4.addStretch()
        v_l4.addWidget(self.add_all_btn)
        v_l4.addWidget(self.del_all_btn)
        v_l4.addStretch()
        v_l5.addStretch()
        v_l5.addWidget(self.add_right_btn)
        v_l5.addWidget(self.del_right_btn)
        v_l5.addStretch()
        h_l.addLayout(v_l1)
        h_l.addLayout(v_l4)
        h_l.addLayout(v_l2)
        h_l.addLayout(v_l5)
        h_l.addLayout(v_l3)

        main_l.addLayout(h_l, 4)

        h_ok = QHBoxLayout()
        h_ok.addStretch(10)
        h_ok.addWidget(self.ok, 2)

        main_l.addLayout(h_ok, 1)

        self.setLayout(main_l)
        self.open_image_btn.clicked.connect(self.load_image)
        self.add_all_btn.clicked.connect(self.add_all)
        self.add_right_btn.clicked.connect(self.add_right)
        self.del_all_btn.clicked.connect(self.del_all)
        self.del_right_btn.clicked.connect(self.del_right)
        self.ok.clicked.connect(self.write_data)

    def load_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home', "Images (*.png *.jpeg *.jpg)")
        if fname[0]:
            self.pixmap = QPixmap.fromImage(QImage(fname[0]))
            self.image.setPixmap(self.pixmap)

    def load_answers(self):
        self.db.get_all_answers()
        for ax in self.db.data:
            self.answers.addItem(ax[0])

    def del_all(self):
        if self.all_answers.selectedItems():
            self.answers.addItem(self.all_answers.selectedItems()[0].text())
            self.all_answers.takeItem(self.all_answers.selectedIndexes()[0].row())

    def del_right(self):
        if self.right_answers.selectedItems():
            self.answers.addItem(self.right_answers.selectedItems()[0].text())
            self.right_answers.takeItem(self.right_answers.selectedIndexes()[0].row())

    def add_all(self):
        if self.answers.selectedItems():
            self.all_answers.addItem(self.answers.selectedItems()[0].text())
            self.answers.takeItem(self.answers.selectedIndexes()[0].row())

    def add_right(self):
        if self.answers.selectedItems():
            self.right_answers.addItem(self.answers.selectedItems()[0].text())
            self.answers.takeItem(self.answers.selectedIndexes()[0].row())

    def write_data(self):
        data = []
        for i in range(1):
            self.data.add_question()