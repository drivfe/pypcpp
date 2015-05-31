from bs4 import BeautifulSoup
from .rowextractor import RowExtractor
from pprint import pprint
from prettytable import PrettyTable
import prettytable
import tools
import requests, os

class Search:
	def __init__(self, search, options={}):
		self.search = search
		self.results = []
		self.opts = options
		self.type = self.opts['type']
		self.session = requests.Session()
	
	def run(self):
		print("Searching '{}' of type '{}'".format(self.search, self.type))

		URL = "http://pcpartpicker.com/parts/{}/fetch/".format(self.type)
	
		payload = { 'mode': 'list',
					'xslug': '',
					'search': self.search,
					'page': self.opts.get('page', 1),
					'sort': self.opts.get('sort') }
					# a8 = column 8 sort ascending
					
		if self.opts['login']:
			self.login()
		
		if True:
			r = self.session.get(URL, params=payload)
			with open('pypcpp\cachejson.html', 'w+') as fh:
				fh.write(r.json()['result']['html']);

		soup = BeautifulSoup(open('pypcpp\cachejson.html'))
		rows = soup.findAll('tr')
		
		extracted = RowExtractor(self.type, rows).extract()
		
		self.outputTable(extracted)
		
	def outputTable(self, extr):
		tbl = PrettyTable(list(tools.typeFields(self.type)))
		tbl.align = 'l'
		tbl.border = False
		tbl.header_style = 'upper'
		
		for r in extr:
			tbl.add_row(shrinkText(r.fields.values(), 17))
		
		print(tbl)

	def login(self):
		LOGIN_URL = "https://pcpartpicker.com/accounts/login/"
		self.session.headers.update({'referer':LOGIN_URL})
		self.session.headers.update({'User-Agent':'Bot testing'})

		r = self.session.get(LOGIN_URL)
		tokensoup = BeautifulSoup(r.text)
		token = tokensoup.find('input', attrs={'name':'csrfmiddlewaretoken'})['value']

		data = {'checkbox':'on', 'csrfmiddlewaretoken':token, 'next':''}
		data.update(tools.getLoginInfo())
		
		r = self.session.post(LOGIN_URL, data=data)
		
def shrinkText(values, limit):
	MAX_LENGTH = 100
	newList = values
	shrink = lambda text: text if len(text) < limit else text[:limit]+'...'
	
	length = sum([len(a) for a in values])
	if length > MAX_LENGTH:
		newList = [shrink(s) for s in values]
		
	return newList
	