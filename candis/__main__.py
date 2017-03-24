# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import sys

# imports - module imports
from candis.app import Window
from candis import app

if __name__ == '__main__':
    window = Window()
    window.show()

    sys.exit(app.exec_())
