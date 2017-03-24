# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import os
import json

# imports - module imports
from candis.app.config import BaseConfig

_NAME    = 'candis'
_VERSION = '0.1.0'

class AppConfig(BaseConfig):
    class Path(BaseConfig.Path):
        pass

    NAME    = _NAME
    VERSION = _VERSION

    class Window(object):
        TITLE    = '%s v%s' % (_NAME, _VERSION)
        POSITION = (50, 50)
        SIZE     = (1024, 768)
        ICON     = os.path.join(BaseConfig.Path.ABSPATH_ASSETS, 'img/logo.png')