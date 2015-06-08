from bs4 import BeautifulSoup
from .rowextractor import RowExtractor
from prettytable import PrettyTable
import tools
import requests, os

def outputTable(ptype, extr):
	tbl = PrettyTable(list(ptype.fields))
	tbl.align = 'l'
	tbl.border = False
	tbl.header_style = 'upper'

	for r in extr:
		tbl.add_row(shrinkText(r.fields.values()))

	print(tbl)

def shrinkText(values):
	MAX_LENGTH = 100
	newList = list(values)
	limit = int(MAX_LENGTH / len(newList))
	shrink = lambda text: text if len(text) < limit else text[0:limit]+'...'
	
	length = len(newList[0])
	if length > limit:
		newList[0] = shrink(newList[0])
		
	return newList
	
def search(search, opts):
	session = requests.Session()
	ptype = opts['type']
	
	def login():
		LOGININFO = tools.getLoginInfo()
		if not LOGININFO['username'] or not LOGININFO['password']:
			print('Credentials not found! Will perform search without logging in.')
			print('\'python pypcpp -h\' for more info\n')
			return

		print('Logging in...')
		LOGIN_URL = "https://pcpartpicker.com/accounts/login/"
		session.headers.update({'referer':LOGIN_URL})
		session.headers.update({'User-Agent':'Python PCPartPicker (github.com/drivfe/pypcpp)'})

		r = session.get(LOGIN_URL)
		tokensoup = BeautifulSoup(r.text)
		token = tokensoup.find('input', attrs={'name':'csrfmiddlewaretoken'})['value']

		data = {
			'checkbox':'on',
			'csrfmiddlewaretoken':token,
			'next':''
		}
		data.update(LOGININFO)
		
		r = session.post(LOGIN_URL, data=data)
		if 'pad-block login-error' in r.text:
			print('LOGIN FAILED: Please check your credentials, \'python pypcpp -h\' for more info')
			print('Will perform the search without logging in')
		else:
			print('Login successful!\n')
		
	URL = "http://pcpartpicker.com/parts/{}/fetch/".format(ptype.name)
	CACHE = '{}\cachejson.html'.format(tools.currentDir())
	
	payload = {
		'mode': 'list',
		'xslug': '',
		'search': search,
		'page': opts.get('page', 1),
		'sort': ptype.sortString(
			opts['sortby'],
			opts['order']
			)
	}
	
	if True:
		if opts['login']:
			login()

		r = session.get(URL, params=payload)
		with open(CACHE, 'w+') as fh:
			fh.write(r.json()['result']['html'])
			
	print(
	"Searching '{}' of part type '{}' sorted by {} in {} order.\n".format(
			search,
			ptype.name,
			opts['sortby'],
			'ascending' if opts['order'] == 'a' else 'descending'
		)
	)
	
	soup = BeautifulSoup(open(CACHE))
	rows = soup.findAll('tr')
	extracted = RowExtractor(ptype, rows).extract()
	outputTable(ptype, extracted)
