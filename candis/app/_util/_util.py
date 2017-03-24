# imports - compatibility imports
from __future__ import absolute_import

# imports - standard imports
import os

# imports - module imports
from candis.app.config.app import AppConfig

def _get_icon_path(filename):
    path = os.path.join(AppConfig.Path.ABSPATH_ASSETS, 'img/icons', filename)

    return path