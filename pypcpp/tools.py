from collections import OrderedDict
import constants

def typeFields(type):
		fields = OrderedDict()
		
		if type == constants.VIDEOCARD:
			fields['videocard'] = 1
			fields['series'] = 2
			fields['chipset'] = 3
			fields['memory'] = 4
			fields['coreclock'] = 5
			fields['price'] = 8
		
		if type == constants.CPU:
			fields['cpu'] = 1
			fields['speed'] = 2
			fields['cores'] = 3
			fields['tdp'] = 4
			fields['price'] = 7
			
		if type == constants.RAM:
			fields['ram'] = 1
			fields['speed'] = 2
			#fields['type'] = 3
			fields['modules'] = 5
			#fields['size'] = 6
			fields['price/gb'] = 7
			fields['price'] = 10
			
		if type == constants.MOTHERBOARD:
			fields['motherboard'] = 1
			fields['socket/cpu'] = 2
			fields['formfactor'] = 3
			fields['ramslots'] = 4
			#fields['maxram'] = 5
			fields['price'] = 8
			
		if type == constants.CASE:
			fields['case'] = 1
			fields['type'] = 2
			#fields['psu'] = 5
			fields['price'] = 8
			
		return fields
		
#returns a8, d8, depending on the column and order
#will default to price in ascending order
def sortFromColumnName(type, name, descending):
	return '{}{}'.format('d' if descending else 'a', typeFields(type).get(name, 'price'))

def typeFromArgs(arg):
	if arg['--videocard'] == True:
		return constants.VIDEOCARD
	elif arg['--cpu'] == True:
		return constants.CPU
	elif arg['--ram'] == True:
		return constants.RAM
	elif arg['--motherboard'] == True:
		return constants.MOTHERBOARD
	elif arg['--tower'] == True:
		return constants.CASE
		
def getLoginInfo():
	from configparser import SafeConfigParser
	import os
	
	parser = SafeConfigParser()
	parser.read('{}\pypcpp.conf'.format(configFilePath()))
	result = {  'username': parser.get('Login Info', 'username'),
				'password': parser.get('Login Info', 'password') }
	return result
	
def writeLoginInfo(username, password):
	from configparser import SafeConfigParser
	import os
	
	parser = SafeConfigParser()
	parser.add_section('Login Info')
	if username:
		parser.set('Login Info', 'username', username)
	if password:
		parser.set('Login Info', 'password', password)
		
	cfg = '{}\pypcpp.conf'.format(configFilePath())
	with open(cfg, 'w') as fh:
		parser.write(fh)
		
def configFilePath():
	import os
	return os.path.dirname(os.path.abspath(__file__))