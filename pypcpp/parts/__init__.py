from pypcpp.parts.common import Part
from pypcpp.parts.case import Case
from pypcpp.parts.cpu import CPU
from pypcpp.parts.motherboard import Motherboard
from pypcpp.parts.psu import PSU
from pypcpp.parts.ram import RAM
from pypcpp.parts.storage import Storage
from pypcpp.parts.videocard import VideoCard

_parts_list = [
    klass for name, klass in locals().items()
    if issubclass(type(klass), Part.__class__)
    and klass.__name__ != 'Part'
]

def list_parts():
    return _parts_list
