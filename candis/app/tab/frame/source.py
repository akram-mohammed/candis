# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from PyQt5 import QtGui, QtWidgets, QtCore

# imports - module imports
from candis._util import _assign_if_none

class ButtonLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent = None, buttonText = None):
        self.super      = super(ButtonLineEdit, self)
        self.parent     = parent
        self.super.__init__(parent)

        self.buttonText = _assign_if_none(buttonText, '')
        self.layout     = QtWidgets.QHBoxLayout()

        self.createUI()

    def createUI(self):
        self.button  = QtWidgets.QPushButton(self.buttonText, self)
        self.button.setCursor(QtCore.Qt.ArrowCursor)
        self.clicked = self.button.clicked

        self.layout.addWidget(self.button)
        self.layout.setAlignment(QtCore.Qt.AlignRight)
        self.layout.setContentsMargins(QtCore.QMargins(0, 0, 0, 0))

        self.setLayout(self.layout)

class SourceFrame(QtWidgets.QWidget):
    def __init__(self, parent = None, name = 'source', icon = 'database.png'):
        self.super  = super(SourceFrame, self)
        self.parent = parent

        self.super.__init__(parent)

        self.name   = name
        self.icon   = icon

        self.layout = QtWidgets.QVBoxLayout()

        self.createUI()

    def createUI(self):
        self.input      = ButtonLineEdit(self, buttonText = 'Browse')
        self.input.clicked.connect(self.openFile)
        self.input.setPlaceholderText('Search or Upload a dataset')

        self.table      = QtWidgets.QTableView()

        self.layout.addWidget(self.input)
        self.layout.addWidget(self.table)
        self.layout.setAlignment(QtCore.Qt.AlignTop)

        self.setLayout(self.layout)

    def openFile(self):
        filename, filter_ = QtWidgets.QFileDialog.getOpenFileName(self, filter = "(CEL (*.cel)")

        if filename is not None:
            self.input.setText(filename)