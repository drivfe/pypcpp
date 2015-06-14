from .common import Part

class Case(Part):
	_arg = '--tower'
	_fetch = 'case'
	
	@staticmethod
	def generateFields():
		from collections import OrderedDict
		
		fields = OrderedDict()
		fields['case'] = 1
		fields['type'] = 2
		#fields['psu'] = 5
		fields['price'] = 8
		
		return fields