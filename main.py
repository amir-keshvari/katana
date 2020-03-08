# katana club member managment system
# use python3.8
# use PySide2
import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1280, 768)
        self.setWindowTitle('Game Club Managment System')
        
        self.lbl_logo = QtWidgets.QLabel('K A T A N A')
        self.lbl_logo.setAlignment(QtCore.Qt.AlignCenter)
        #self.content_layout = QtWidgets.QHBoxLayout()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.lbl_logo)
        #self.main_layout.addWidget(self.content_layout)
        self.setLayout(self.main_layout)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWindow()
    widget.show()
    sys.exit(app.exec_())
