# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from PyQt5 import QtWidgets

class ModelTab(QtWidgets.QWidget):
    def __init__(self, parent, name = 'model', icon = 'network.png'):
        self.super  = super(SourceTab, self)
        self.parent = parent

        self.super.__init__(parent)

        self.name   = name
        self.icon   = icon

        self.layout = QtWidgets.QVBoxLayout(parent)

        self.createUI()

    def createUI(self):
        self.setLayout(self.layout)
