"""Python PCPartPicker
Usage:
  pypcpp.py (-c | -v | -r | -m | -t) <search>... [--sort=<sort> [-a | -d]] [-l]
  pypcpp.py logininfo --user=<username> --pass=<password>
  pypcpp.py logininfo
  pypcpp.py (-h | --help)

 Options:
  -c, --cpu          CPU search
  -v, --videocard    Video Card search
  -r, --ram          RAM search
  -m, --motherboard  Motherboard search
  -t, --tower        Tower/Case search
  -s, --sort <sort>  Sort by. [default: price]
  -a, --ascending    Ascending order
  -d, --descending   Descending order
  -h, --help         Show help
  -l, --login        Login before doing search
  --user=<username>  Save username to config file
  --pass=<password>  Save password to config file
"""

import sys, tools
import pypcpp.pypcpp as pcp
from docopt import docopt

def main(args):
	if args['logininfo']:		
		if args['--user'] or args['--pass']:
			tools.writeLoginInfo(args['--user'], args['--pass'])
		
		linfo = tools.getLoginInfo()
		print('Here is your login info: {}\nThe config file is saved in: {}'.format(linfo, tools.configFilePath()))
	
	else:
		search = ' '.join(arguments['<search>'])
		
		type = tools.typeFromArgs(args)
		sort = tools.sortFromColumnName(type, args['--sort'], args['--descending'])
		options = { 'type' : type,
					'sort' : sort,
					'login' : args['--login'] }
		
		pcp.Search(search, options).run()
	
if __name__ == '__main__':
	arguments = docopt(__doc__, version='Python PCPartPicker 0.1')
	#print(arguments)
	main(arguments)