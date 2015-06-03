from collections import OrderedDict
import constants

class Part:
	def __init__(self, type):
		self.fields = OrderedDict()
		self.type = type
		
	def __repr__(self):
		ret = []
		for k, v in self.fields.items():
			ret.append(v)
		
		return ' '.join(ret)
	
	def __str__(self):
		return repr(self)
		
	def beautifyFields(self):
		pass

class CPU(Part):
	pass

class VideoCard(Part):
	def beautifyFields(self):
		#Only brand name of the Videocard
		self.fields['videocard'] = self.fields['videocard'].split(' ')[0]
		
		#Remove 'Radeon' and 'Geforce' from chipset
		self.fields['chipset'] = self.fields['chipset'].replace('Radeon ', '').replace('GeForce ', '')
		
		#Remove 'black edition' from series (string too long)
		self.fields['series'] = self.fields['series'].replace('Black Edition ', '')
		
class RAM(Part):
	pass
	
class Motherboard(Part):
	pass
	
class Case(Part):
	pass

class Storage(Part):
	def beautifyFields(self):
		#Only brand, Western Digital fails
		self.fields['storage'] = self.fields['storage'].split(' ')[0]
		if 'Western' in self.fields['storage']:
			self.fields['storage'] = 'Western Digital'
	
class PSU(Part):
	def beautifyFields(self):
		#Only brand name
		self.fields['powersupply'] = self.fields['powersupply'].split(' ')[0]