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
       # widgets
        self.lbl_logo = QtWidgets.QLabel('K A T A N A')
        self.lbl_logo.setAlignment(QtCore.Qt.AlignCenter)
        # reg form widget
        self.txt_name = QtWidgets.QLineEdit()
        self.txt_name.setPlaceholderText('Client Name')
        # ComboBox consols
        self.combo_consols = QtWidgets.QComboBox()
        self.combo_consols.addItem('PS1')
        self.combo_consols.addItem('PS2')
        self.combo_consols.addItem('PS3')
        self.combo_consols.addItem('PS4')
        self.combo_consols.addItem('PS5')
        self.combo_consols.addItem('PS6')
        self.combo_consols.addItem('PS7')
        self.combo_consols.addItem('PS8')
        self.txt_credit = QtWidgets.QLineEdit()
        self.txt_credit.setPlaceholderText('Credit')
        self.txt_hour = QtWidgets.QLineEdit()
        self.txt_hour.setPlaceholderText('Hour')
        self.txt_min = QtWidgets.QLineEdit()
        self.txt_min.setPlaceholderText('Minute')
        self.btn_submit = QtWidgets.QPushButton('Register')
        self.regForm_groupBox = QtWidgets.QGroupBox('Register Form')
       # layouts
        # Register Form
        self.regForm_layout = QtWidgets.QHBoxLayout()
        self.regForm_groupBox.setLayout(self.regForm_layout)
        self.regForm_layout.addWidget(self.txt_name)
        self.regForm_layout.addWidget(self.combo_consols)
        self.regForm_layout.addWidget(self.txt_credit)
        self.regForm_layout.addWidget(self.txt_hour)
        self.regForm_layout.addWidget(self.txt_min)
        self.regForm_layout.addWidget(self.btn_submit)
        # main layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.lbl_logo)
        self.main_layout.addWidget(self.regForm_groupBox)
        self.setLayout(self.main_layout)
        self.regForm_groupBox.setLayout(self.regForm_layout)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWindow()
    widget.show()
    sys.exit(app.exec_())
