"""Python PCPartPicker
Usage:
  pypcpp.py (-c | -v | -r | -m | -t | -p | -s) <search>... [--sort=<sort> [-a | -d]] [-l]
  pypcpp.py logininfo --user=<username> --pass=<password>
  pypcpp.py logininfo
  pypcpp.py (-h | --help)

Options:
  -c, --cpu          CPU search
  -v, --videocard    Video Card search
  -r, --ram          RAM search
  -m, --motherboard  Motherboard search
  -t, --tower        Tower/Case search
  -p, --psu          Power Supply search
  -s, --storage      Storage search (HDD/SSD)
  
  --sort=<sort>      Sort by. [default: price]
  -a, --ascending    Ascending order
  -d, --descending   Descending order
  
  -h, --help         Show help
  -l, --login        Log in before doing search
  --user=<username>  Save username to config file
  --pass=<password>  Save password to config file
"""
import os
from docopt import docopt

def cDir():
	return os.path.dirname(os.path.abspath(__file__))

try:
	import pypcpp as pcp
except ImportError:
	import sys
	sys.path.append(os.path.join(cDir(), '..'))
	import pypcpp as pcp

def main(args):
	if args['logininfo']:		
		if args['--user'] or args['--pass']:
			pcp.tools.writeLoginInfo(args['--user'], args['--pass'])
		
		linfo = pcp.tools.getLoginInfo()
		if not linfo['username'] or not linfo['password']:
			print('Your info is not yet saved, Use \'--user=<user>\' and \'--pass=<password>\' to save your info')
		else:
			print('Here is your login info: {}'.format(linfo))
		print('The config file is saved in:', cDir())
	
	else:
		sterm = ' '.join(arguments['<search>'])
		
		type = pcp.tools.PartType.typeFromArgs(args)
		options = {
			'type' : type,
			'sortby' : args['--sort'],
			'order' : 'd' if args['--descending'] else 'a',
			'login' : args['--login']
		}

		pcp.search(sterm, options)
	
if __name__ == '__main__':
	arguments = docopt(__doc__, version='Python PCPartPicker 0.1')
	#print(arguments)
	main(arguments)