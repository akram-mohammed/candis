# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party imports
from PyQt5 import QtGui, QtWidgets

# imports - module imports
from candis.app.config.app import AppConfig
from candis.app.tab import TabLayout
from candis.app.tab.frame import (
    SourceFrame,
    PreviewFrame,
    PreprocessFrame,
    ModelFrame,
    AnalysisFrame,
    PredictFrame
)

_FRAME_WIDGETS = \
[
    SourceFrame,
    PreviewFrame,
    PreprocessFrame,
    ModelFrame,
    AnalysisFrame,
    PredictFrame
]

class Window(QtWidgets.QMainWindow):
    def __init__(self,
                 title    = AppConfig.Window.TITLE,
                 position = AppConfig.Window.POSITION,
                 size     = AppConfig.Window.SIZE,
                 icon     = AppConfig.Window.ICON):
        self.super    = super(Window, self)

        self.title    = title
        self.position = position
        self.size     = size
        self.icon     = icon

        self.super.__init__()

        self.createUI()

    def createUI(self):
        x, y = self.position
        w, h = self.size
        self.setGeometry(x, y, w, h)

        self.setWindowTitle(self.title)

        icon = QtGui.QIcon(self.icon)
        self.setWindowIcon(icon)

        self.tabLayout = TabLayout(self, frame_widgets = _FRAME_WIDGETS)
        self.setCentralWidget(self.tabLayout)
