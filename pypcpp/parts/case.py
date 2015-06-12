from .common import Part
import constants

class Case(Part):
	_constant = constants.TOWER
	
	@staticmethod
	def generateFields():
		from collections import OrderedDict
		
		fields = OrderedDict()
		fields['case'] = 1
		fields['type'] = 2
		#fields['psu'] = 5
		fields['price'] = 8
		
		return fields