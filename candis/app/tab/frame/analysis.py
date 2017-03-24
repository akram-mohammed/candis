# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from PyQt5 import QtWidgets

class AnalysisFrame(QtWidgets.QWidget):
    def __init__(self, parent = None, name = 'analysis', icon = 'report.png'):
        self.super  = super(AnalysisFrame, self)
        self.parent = parent

        self.super.__init__(parent)

        self.name   = name
        self.icon   = icon

        self.layout = QtWidgets.QVBoxLayout()

        self.createUI()

    def createUI(self):
        self.setLayout(self.layout)
