from .common import Part

class Motherboard(Part):
	_arg = '--motherboard'
	_fetch = 'motherboard'
	
	@staticmethod
	def generateFields():
		from collections import OrderedDict
		
		fields = OrderedDict()
		fields['motherboard'] = 1
		fields['socket/cpu'] = 2
		fields['formfactor'] = 3
		fields['ramslots'] = 4
		#fields['maxram'] = 5
		fields['price'] = 8
		
		return fields