# imports - compatibility imports
from __future__ import absolute_import

# imports - module imports
from candis._util import _assign_if_none

def test__assign_if_none():
    assert _assign_if_none(None, 1) == 1
    assert _assign_if_none(1,'foo') == 1
