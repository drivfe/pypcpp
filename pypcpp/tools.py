import os
from configparser import SafeConfigParser
import pypcpp.parts as parts

class PartType:
	def __init__(self, name):
		self.name = name
		self.pclass = self.__gen_part()
		self.fields = self.pclass.generateFields()
		self.fetch = self.pclass._fetch
		
	def __gen_part(self):
		for p in parts.list_parts():
			if p.isName(self.name):
				return p

	#returns a8, d8, depending on the column and order
	#will default to price in ascending order
	def sortString(self, sortby, order):
		return '{}{}'.format(order, self.fields.get(sortby, 'price'))

	def newPart(self):
		return self.pclass()

	@staticmethod
	def typeFromArgs(arg):
		typestring = None
		for p in parts.list_parts():
			if arg[p._arg] == True:
				typestring = p.name()
		
		return PartType(typestring)
		
def getLoginInfo():	
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
	return os.path.dirname(os.path.abspath(__file__))