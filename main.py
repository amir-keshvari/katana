# katana club member managment system
# use python3.8
# use PySide2
import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('KATANA')
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWindow()
    widget.show()
    sys.exit(app.exec_())