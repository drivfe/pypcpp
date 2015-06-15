import requests
from bs4 import BeautifulSoup
from pypcpp.rowextractor import RowExtractor
import pypcpp.tools as tools

def search(search, opts):
	session = requests.Session()
	ptype = opts['type']
	cback = opts.get('callback', print)
	
	def login():
		LOGININFO = tools.getLoginInfo()
		if not LOGININFO['username'] or not LOGININFO['password']:
			cback('Credentials not found! Will perform search without logging in.')
			cback('run \'pypcpp logininfo\' for more information\n')
			return

		cback('Logging in...')
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
			cback('LOGIN FAILED: Please check your credentials, run \'pypcpp logininfo\' for more information')
			cback('Will perform the search without logging in\n')
		else:
			cback('Login successful!\n')
		
	URL = "http://pcpartpicker.com/parts/{}/fetch/".format(ptype.fetch)
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
	
	if True: # debug if statement :p
		if opts['login']:
			login()

		r = session.get(URL, params=payload)
		with open(CACHE, 'w+') as fh:
			try:
				rjson = r.json()['result']['html']
				fh.write(rjson)
			except ValueError:
				import sys
				cback("ERROR: No JSON returned. The website might be down. Exiting")
				sys.exit()
			
	cback("Searching '{}' of '{}' sorted by {} in {} order.\n".format(
			search,
			ptype.name,
			opts['sortby'],
			'ascending' if opts['order'] == 'a' else 'descending'
		)
	)
	
	soup = BeautifulSoup(open(CACHE))
	rows = soup.findAll('tr')
	extracted = RowExtractor(ptype, rows).extract()
	return extracted
