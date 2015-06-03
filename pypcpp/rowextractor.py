from bs4 import BeautifulSoup
from .part import Part, CPU, VideoCard
from collections import OrderedDict
import constants, tools

class RowExtractor:
	def __init__(self, type, rows):
		self.type = type
		self.rows = rows
		
	def extract(self):
		result = []
		
		for a in self.rows:
			rowresult = self.__workRow(a)
			if rowresult is not None:
				result.append(rowresult)
				
		return result
			
	def __workRow(self, row):
		tds = row.findAll('td')
		
		part = self.type.newPart()
		
		for c, n in self.type.fields.items():
			if not tds[n].a:
				part.fields[c] = tds[n].text
			else:
				part.fields[c] = tds[n].a.text
				
		part.beautifyFields()
		
		return part if part.fields['price'] else None #Only return Part if price is available
			