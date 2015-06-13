import constants
from collections import OrderedDict

class Part:
	def __init__(self, cns):
		self.fields = OrderedDict()
		self.cns = cns
		
	@classmethod
	def isValidConstant(cls, cns):
		return cns == cls._constant
	
	def __repr__(self):
		ret = []
		for k, v in self.fields.items():
			ret.append(v)
		
		return ' '.join(ret)
	
	def __str__(self):
		return repr(self)
		
	def beautifyFields(self):
		pass
		