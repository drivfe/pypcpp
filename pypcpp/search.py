import os
import pickle
import requests
from bs4 import BeautifulSoup, SoupStrainer
import pypcpp.tools as tools

def search(search, opts):
	ptype = opts['type']
	cback = opts.get('callback', print)
	sess_file = os.path.join(tools.currentDir(), 'sess.pkl')
	
	def _load_session():
		if os.path.isfile(sess_file) and opts.get('login', False):
			return pickle.load(open(sess_file, 'rb')), False
		
		return requests.Session(), True

	session, new_s = _load_session()

	def _dump_session():
		if opts.get('login', False):
			pickle.dump(session, open(sess_file, 'w+b'))
	
	def login():
		if not new_s:
			cback('Automatic log in (from the previous session).')
			return
			
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
		toparse = SoupStrainer('input', attrs={'name':'csrfmiddlewaretoken'})
		token = BeautifulSoup(r.text, parse_only=toparse).find('input')['value']
		
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
	CACHE = os.path.join(tools.currentDir(), 'cachejson.html')
	
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
			
		# save session to file for later
		_dump_session()
		
	cback("Searching '{}' of '{}' sorted by {} in {} order.\n".format(
			search,
			ptype.name,
			opts['sortby'],
			'ascending' if opts['order'] == 'a' else 'descending'
		)
	)
	
	soup = BeautifulSoup(open(CACHE))
	rows = soup.findAll('tr')
	extracted = tools.extractRows(ptype, rows)
	return extracted
