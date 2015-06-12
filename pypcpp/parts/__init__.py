from .case import Case
from .cpu import CPU
from .motherboard import Motherboard
from .psu import PSU
from .ram import RAM
from .storage import Storage
from .videocard import VideoCard

_parts_list = [
	Case,
	CPU,
	Motherboard,
	PSU,
	RAM,
	Storage,
	VideoCard
]

def list_parts():
	return _parts_list