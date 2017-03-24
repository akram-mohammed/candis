# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import os

# imports - third-party imports
from PyQt5 import QtGui, QtWidgets

# imports - module imports
from candis._util import _assign_if_none
from candis.app.config.app import AppConfig
from candis.app._util import _get_icon_path

def _get_tab_display_text(frame):
    name = frame.name.capitalize()

    return name

class TabLayout(QtWidgets.QWidget):
    def __init__(self, parent, frame_widgets = None):
        self.super  = super(TabLayout, self)
        self.parent = parent

        self.super.__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.tab    = QtWidgets.QTabWidget()
        self.frames = [widget(parent) for widget in frame_widgets]

        self.createUI()

    def createUI(self):
        for i, frame in enumerate(self.frames):
            text = _get_tab_display_text(frame)
            self.tab.addTab(frame, text)

            path = _get_icon_path(frame.icon)
            icon = QtGui.QIcon(path)
            self.tab.setTabIcon(i, icon)

        self.layout.addWidget(self.tab)
        self.setLayout(self.layout)
