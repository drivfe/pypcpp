from collections import OrderedDict
import constants
import part
	
class PartType:
	def __init__(self, name):
		self.name = name
		self.fields = self.__generateFields()
		
	#returns a8, d8, depending on the column and order
	#will default to price in ascending order
	def sortString(self, sortby, order):
		return '{}{}'.format(order, self.fields.get(sortby, 'price'))

	def newPart(self):
		partClasses = {
			constants.VIDEOCARD:part.VideoCard,
			constants.CPU:part.CPU,
			constants.RAM:part.RAM,
			constants.MOTHERBOARD:part.Motherboard,
			constants.CASE:part.Case,
			constants.PSU:part.PSU,
			constants.STORAGE:part.Storage
		}
	
		return partClasses[self.name](self.name)
		
	def __generateFields(self):
		flds = OrderedDict()
		
		if self.name == constants.VIDEOCARD:
			flds['videocard'] = 1
			flds['series'] = 2
			flds['chipset'] = 3
			flds['memory'] = 4
			flds['coreclock'] = 5
			flds['price'] = 8
		
		if self.name == constants.CPU:
			flds['cpu'] = 1
			flds['speed'] = 2
			flds['cores'] = 3
			flds['tdp'] = 4
			flds['price'] = 7
			
		if self.name == constants.RAM:
			flds['ram'] = 1
			flds['speed'] = 2
			#flds['type'] = 3
			flds['modules'] = 5
			#flds['size'] = 6
			flds['price/gb'] = 7
			flds['price'] = 10
			
		if self.name == constants.MOTHERBOARD:
			flds['motherboard'] = 1
			flds['socket/cpu'] = 2
			flds['formfactor'] = 3
			flds['ramslots'] = 4
			#flds['maxram'] = 5
			flds['price'] = 8
			
		if self.name == constants.CASE:
			flds['case'] = 1
			flds['type'] = 2
			#flds['psu'] = 5
			flds['price'] = 8
		
		if self.name == constants.PSU:
			flds['powersupply'] = 1
			flds['series'] = 2
			flds['form'] = 3
			flds['efficiency'] = 4
			flds['watts'] = 5
			flds['modular'] = 6
			flds['price'] = 9
		
		if self.name == constants.STORAGE:
			flds['storage'] = 1
			flds['series'] = 2
			flds['type'] = 4
			flds['capacity'] = 5
			flds['cache'] = 6
			#flds['price/gb'] = 7
			flds['price'] = 10
		
		return flds
		
	@staticmethod
	def typeFromArgs(arg):
		typestring = None
		
		if arg['--videocard'] == True:
			typestring = constants.VIDEOCARD
		elif arg['--cpu'] == True:
			typestring = constants.CPU
		elif arg['--ram'] == True:
			typestring = constants.RAM
		elif arg['--motherboard'] == True:
			typestring = constants.MOTHERBOARD
		elif arg['--tower'] == True:
			typestring = constants.CASE
		elif arg['--psu'] == True:
			typestring = constants.PSU
		elif arg['--storage'] == True:
			typestring = constants.STORAGE
		
		return PartType(typestring)
		
def getLoginInfo():
	from configparser import SafeConfigParser
	import os
	
	FILEPATH = '{}\pypcpp.conf'.format(currentDir())
	if not os.path.isfile(FILEPATH):
		open(FILEPATH, 'a').close()
		writeLoginInfo('', '', True)
	
	parser = SafeConfigParser()
	parser.read(FILEPATH)
	result = {
		'username': parser.get('Login Info', 'username'),
		'password': parser.get('Login Info', 'password')
	}
	return result
	
def writeLoginInfo(username, password, acceptNone=False):
	from configparser import SafeConfigParser
	import os
	
	parser = SafeConfigParser()
	parser.add_section('Login Info')
	if username or acceptNone:
		parser.set('Login Info', 'username', username)
	if password or acceptNone:
		parser.set('Login Info', 'password', password)
		
	cfg = '{}\pypcpp.conf'.format(currentDir())
	with open(cfg, 'w') as fh:
		parser.write(fh)	
		
def currentDir():
	import os
	return os.path.dirname(os.path.abspath(__file__))