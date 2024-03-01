import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGroupBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class DraggableLabel(QLabel):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.setAttribute(Qt.WA_DeleteOnClose)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(self.text())
        drag.setMimeData(mime_data)
        pixmap = self.grab()
        drag.setPixmap(pixmap)
        self.close()  # we close the label to drag a 'copy' of it
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

class DroppableGroupBox(QGroupBox):

    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setAcceptDrops(True)
        layout = QVBoxLayout()
        self.setLayout(layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            text = event.mimeData().text()
            new_label = DraggableLabel(text, self)
            self.layout().addWidget(new_label)
            new_label.show()
            event.accept()
        else:
            event.ignore()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        group_box1 = DroppableGroupBox("Group Box 1")
        label1 = DraggableLabel("Label 1", group_box1)
        group_box1.layout().addWidget(label1)

        group_box2 = DroppableGroupBox("Group Box 2")
        label2 = DraggableLabel("Label 2", group_box2)
        group_box2.layout().addWidget(label2)

        layout.addWidget(group_box1)
        layout.addWidget(group_box2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
