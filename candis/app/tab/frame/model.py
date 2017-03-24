# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from PyQt5 import QtGui, QtWidgets, QtCore

# imports - module imports
from candis._util import autodict
from candis.app._util import _get_icon_path

class ModelFrame(QtWidgets.QWidget):
    class Dialog(QtWidgets.QDialog):
        def __init__(self, parent = None, position = (50, 50), size = (640, 480), caption = 'Experiment', icon = 'lab.png'):
            self.super     = super(ModelFrame.Dialog, self)
            self.parent    = parent
            self.super.__init__(parent)

            self.position  = position
            self.size      = size
            self.caption   = caption
            self.icon      = icon
            self.layout    = QtWidgets.QGridLayout()

            self.createUI()

        def createUI(self):
            x, y           = self.position
            w, h           = self.size
            self.setGeometry(x, y, w, h)
            self.setWindowTitle(self.caption)

            path           = _get_icon_path(self.icon)
            self.setWindowIcon(QtGui.QIcon(path))            
            
            # self.form            = autodict()
            # self.input           = autodict()

            # self.form['general'] = QtWidgets.QFormLayout()

            # self.input['name']   = QtWidgets.QLineEdit()
            # self.input['descr']  = QtWidgets.QTextEdit()
            # self.input['descr'].setMaximumHeight(50)

            # self.form['general'].addRow('Name',        self.input['name'])
            # self.form['general'].addRow('Description', self.input['descr'])

            # self.form['learn']   = QtWidgets.QFormLayout()
            
            # self.input['algo']   = QtWidgets.QComboBox()
            # self.input['algo'].addItem('Random Forests')
            # self.input['algo'].addItem('Decision Trees')

            # self.form['learn'].addRow('Classifier', self.input['algo'])

            # self.layout.addLayout(self.form['general'], 0, 0)
            # self.layout.addLayout(self.form['learn']  , 1, 0)

            self.setLayout(self.layout)

    def __init__(self, parent = None, name = 'model', icon = 'network.png'):
        self.super  = super(ModelFrame, self)
        self.parent = parent

        self.super.__init__(parent)

        self.name   = name
        self.icon   = icon

        self.layout = QtWidgets.QVBoxLayout()

        self.createUI()

    def createUI(self):
        self.button        = autodict()
        self.button['new'] = QtWidgets.QPushButton('New', self)
        self.button['new'].clicked.connect(self.openDialog)
        self.table         = QtWidgets.QTableView()

        self.layout.addWidget(self.button['new'])
        self.layout.addWidget(self.table)
        self.layout.setAlignment(QtCore.Qt.AlignTop)

        self.setLayout(self.layout)

    def openDialog(self):
        dialog = ModelFrame.Dialog()
        dialog.show()