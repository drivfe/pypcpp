from .common import Part
import constants

class Storage(Part):
	_constant = constants.STORAGE

	def beautifyFields(self):
		#Only brand, Western Digital fails
		self.fields['storage'] = self.fields['storage'].split(' ')[0]
		if 'Western' in self.fields['storage']:
			self.fields['storage'] = 'Western Digital'

	@staticmethod
	def generateFields():
		from collections import OrderedDict
		
		fields = OrderedDict()
		fields['storage'] = 1
		fields['series'] = 2
		fields['type'] = 4
		fields['capacity'] = 5
		fields['cache'] = 6
		#fields['price/gb'] = 7
		fields['price'] = 10
		
		return fields