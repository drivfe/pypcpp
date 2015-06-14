from .common import Part

class CPU(Part):
	_arg = '--cpu'
	_fetch = 'cpu'
	
	@staticmethod
	def generateFields():
		from collections import OrderedDict
		
		fields = OrderedDict()
		fields['cpu'] = 1
		fields['speed'] = 2
		fields['cores'] = 3
		fields['tdp'] = 4
		fields['price'] = 7
		
		return fields