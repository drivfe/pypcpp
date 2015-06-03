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
		print("Searching '{}' of type '{}'".format(self.search, self.type.name))

		URL = "http://pcpartpicker.com/parts/{}/fetch/".format(self.type.name)
	
		payload = {
			'mode': 'list',
			'xslug': '',
			'search': self.search,
			'page': self.opts.get('page', 1),
			'sort': self.type.sortString(
				self.opts['sortby'],
				self.opts['order']
				)
		}
		
		if self.opts['login']:
			self.login()
		
		#cachejson is just for debugging
		if True:
			r = self.session.get(URL, params=payload)
			with open('pypcpp\cachejson.html', 'w+') as fh:
				fh.write(r.json()['result']['html']);

		soup = BeautifulSoup(open('pypcpp\cachejson.html'))
		rows = soup.findAll('tr')
		
		extracted = RowExtractor(self.type, rows).extract()
		
		self.outputTable(extracted)
		
	def outputTable(self, extr):
		tbl = PrettyTable(list(self.type.fields))
		tbl.align = 'l'
		tbl.border = False
		tbl.header_style = 'upper'
		
		for r in extr:
			tbl.add_row(shrinkText(r.fields.values()))
		
		print(tbl)

	def login(self):
		LOGIN_URL = "https://pcpartpicker.com/accounts/login/"
		self.session.headers.update({'referer':LOGIN_URL})
		self.session.headers.update({'User-Agent':'Bot testing'})

		r = self.session.get(LOGIN_URL)
		tokensoup = BeautifulSoup(r.text)
		token = tokensoup.find('input', attrs={'name':'csrfmiddlewaretoken'})['value']

		data = {
			'checkbox':'on',
			'csrfmiddlewaretoken':token,
			'next':''
		}
		data.update(tools.getLoginInfo())
		
		r = self.session.post(LOGIN_URL, data=data)
		
def shrinkText(values):
	MAX_LENGTH = 100
	newList = list(values)
	limit = int(MAX_LENGTH / len(newList))
	shrink = lambda text: text if len(text) < limit else text[0:limit]+'...'
	
	length = len(newList[0])
	if length > limit:
		newList[0] = shrink(newList[0])
		
	return newList
	