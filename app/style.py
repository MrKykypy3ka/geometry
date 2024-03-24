from PyQt5.QtGui import QFont


def set_style_form(*args):
    for widget in args:
        widget.setFont(QFont('Impact', 14))


def set_style_label(label):
    label.setWordWrap(True)
    label.setFont(QFont('Arial', 12))
    label.setStyleSheet('border: 1px solid black;')


def set_style_label_true(label):
    label.setWordWrap(True)
    label.setFont(QFont('Arial', 12))
    label.setStyleSheet('border: 2px solid green;')


def set_style_label_false(label):
    label.setWordWrap(True)
    label.setFont(QFont('Arial', 12))
    label.setStyleSheet('border: 2px solid red;')