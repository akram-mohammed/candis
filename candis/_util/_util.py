# imports - standard imports
import collections

def _assign_if_none(obj, value):
    if obj is None:
        obj = value

    return obj

def autodict():
	dict_ = collections.defaultdict(autodict)

	return dict_
