from .common import Part
import constants

class CPU(Part):
	_constant = constants.CPU
	_arg = '--cpu'
	
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