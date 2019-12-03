from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
import text_operation


class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.left = 550
        self.top = 150
        self.width = 1000
        self.height = 530
        self.title = "Translate text"
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_up_part()
        self.create_down_part()
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.up_group)
        self.layout.addWidget(self.translate_textbox)
        self.setLayout(self.layout)

        self.show()

    def create_up_part(self):

        self.up_group = QGroupBox()
        self.up_group.setStyleSheet("background:gray")
        up_layout = QHBoxLayout()

        self.textbox = QLineEdit(self)
        self.textbox.resize(280, 40)

        self.select_button = QPushButton('Select pdf file')
        self.select_button.setStyleSheet(
            'background:rgb(91, 155, 213); color:white; font-size: 20px; font-weight: bold')
        self.select_button.clicked.connect(self.upload_pdf_file)
        up_layout.addWidget(self.textbox)
        up_layout.addWidget(self.select_button)

        self.up_group.setLayout(up_layout)

    def create_down_part(self):
        self.translate_textbox = QTextEdit(self)
        self.translate_textbox.setMinimumSize(580,500)

    def upload_pdf_file(self):
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)
        file_path = text_operation.get_file_path()
        self.textbox.setText(file_path)
        text_after_translate = text_operation.translate_text(file_path)
        self.translate_textbox.setFont(font)
        self.translate_textbox.setText(text_after_translate)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())