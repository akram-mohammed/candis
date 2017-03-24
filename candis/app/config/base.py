# imports - standard imports
import os
from os.path import abspath, dirname

class BaseConfig(object):
    class Path(object):
        ABSPATH_ROOT   = abspath(dirname(dirname(__file__)))
        ABSPATH_ASSETS = os.path.join(ABSPATH_ROOT, 'assets')
        ABSPATH_DATA   = os.path.join(ABSPATH_ASSETS, 'data')