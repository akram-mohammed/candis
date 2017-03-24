# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from PyQt5 import QtWidgets

class PredictFrame(QtWidgets.QWidget):
    def __init__(self, parent = None, name = 'predict', icon = 'crystalball.png'):
        self.super  = super(PredictFrame, self)
        self.parent = parent

        self.super.__init__(parent)

        self.name   = name
        self.icon   = icon

        self.layout = QtWidgets.QVBoxLayout()

        self.createUI()

    def createUI(self):
        self.setLayout(self.layout)
