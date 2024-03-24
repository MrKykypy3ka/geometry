from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QPainter
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QGroupBox, QApplication
from app.style import set_style_label


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
        self.hide()
        result = drag.exec_(Qt.CopyAction | Qt.MoveAction)
        if result != Qt.MoveAction:
            self.show()


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
            set_style_label(new_label)
            self.layout().addWidget(new_label)
            new_label.show()
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()


class ScaledPixmapLabel(QLabel):
    scaled = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setMinimumSize(1, 1)

    def resizeEvent(self, event):
        if self.pixmap() and not self.pixmap().isNull():
            self.scaled = self.pixmap().scaled(
                self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def paintEvent(self, event):
        if self.pixmap() and not self.pixmap().isNull():
            if not self.scaled:
                self.scaled = self.pixmap().scaled(
                    self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            available = self.rect()
            rect = self.scaled.rect()
            rect.moveCenter(available.center())
            align = self.alignment()
            if align & Qt.AlignLeft:
                rect.moveLeft(available.left())
            elif align & Qt.AlignRight:
                rect.moveRight(available.right())
            if align & Qt.AlignTop:
                rect.moveTop(available.top())
            elif align & Qt.AlignBottom:
                rect.moveBottom(available.bottom())
            qp = QPainter(self)
            qp.drawPixmap(rect, self.scaled)
