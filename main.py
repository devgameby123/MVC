from view import MainWindow
from controller import Controller
from model import MOMLModel
from PySide6 import QtWidgets

import sys

#App
app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")

#Instance
window = MainWindow()
model = MOMLModel()
control = Controller(model,window)

#event loop
app.exec()