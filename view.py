from PySide6 import QtWidgets,QtCore
from PySide6.QtUiTools import QUiLoader

import os
#กำหนด Path ที่ทำงานอยู่
basePath = os.path.dirname(__file__)
loader = QUiLoader()

class MainWindow(QtCore.QObject):
    def __init__(self):
        super().__init__()
        #โหลด File MainWindow.ui เพื่อสร้าง desktop gui
        self.ui = loader.load(os.path.join(basePath,"MainWindow.ui"))
        #กำหนด Widgets ทั้งหมดให้เป็นตัวแปร
        self.bttag1 = self.ui.findChild(QtWidgets.QPushButton,"bt_tag1")
        self.bttag2 = self.ui.findChild(QtWidgets.QPushButton,"bt_tag2")
        self.textout1 = self.ui.findChild(QtWidgets.QTextBrowser,"output_tag1")
        self.textout2 = self.ui.findChild(QtWidgets.QTextBrowser,"output_tag2")
        self.textinput = self.ui.findChild(QtWidgets.QPlainTextEdit,"textInput")
        self.ui.show()  
        
