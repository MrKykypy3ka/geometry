from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from app.tasksWin import TasksWin
from app.redactorsWin import RedactorWin


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Геометр')
        self.resize(300, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('resources/icons/ico.png'))
        wid = QWidget()
        self.setCentralWidget(wid)
        self.lessons_btn = QPushButton('Уроки')
        self.configurator_btn = QPushButton('Конфигуратор')
        self.settings_btn = QPushButton('Настройки')
        main_vl = QVBoxLayout()
        main_vl.addStretch()
        main_vl.addWidget(self.lessons_btn)
        main_vl.addWidget(self.configurator_btn)
        main_vl.addWidget(self.settings_btn)
        main_vl.addStretch()
        wid.setLayout(main_vl)
        self.lessons_btn.clicked.connect(self.show_lessons)
        self.configurator_btn.clicked.connect(self.show_configurator)
        self.settings_btn.clicked.connect(self.show_settings)

    def show_lessons(self):
        self.win_t = TasksWin()
        self.win_t.show()

    def show_configurator(self):
        self.win_с = RedactorWin()
        self.win_с.show()

    def show_settings(self):
        pass

    def closeEvent(self, event):
        QApplication.quit()