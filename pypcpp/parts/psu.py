from .common import Part
import constants

class PSU(Part):
	_constant = constants.PSU
	_arg = '--psu'
	
	def beautifyFields(self):
		#Only brand name
		self.fields['powersupply'] = self.fields['powersupply'].split(' ')[0]
		
	@staticmethod
	def generateFields():
		from collections import OrderedDict
		
		fields = OrderedDict()
		fields['powersupply'] = 1
		fields['series'] = 2
		fields['form'] = 3
		fields['efficiency'] = 4
		fields['watts'] = 5
		fields['modular'] = 6
		fields['price'] = 9
		
		return fields