from .case import Case
from .cpu import CPU
from .motherboard import Motherboard
from .psu import PSU
from .ram import RAM
from .storage import Storage
from .videocard import VideoCard

_parts_list = [
	klass for name, klass in locals().items()
	if isinstance(klass, type) and klass.__bases__[0].__name__ == 'Part'
]

def list_parts():
	return _parts_list
