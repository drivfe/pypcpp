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
import sys
from prettytable import PrettyTable

cDir = lambda: os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(cDir()))

import pypcpp as pcp

from pypcpp.docopt import docopt

def tableOutput(result):
    if len(result) < 1:
        print('No results found!')
        return
    
    tbl = PrettyTable(list(result[0].fields))
    tbl.align = 'l'
    tbl.border = False
    tbl.header_style = 'upper'

    for r in result:
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

def main(args=None):
    args = docopt(__doc__, version='Python PCPartPicker 0.1')
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
        sterm = ' '.join(args['<search>'])
        
        type = pcp.tools.PartType.typeFromArgs(args)
        options = {
            'type' : type,
            'sortby' : args['--sort'],
            'order' : 'd' if args['--descending'] else 'a',
            'login' : args['--login']
        }

        result = pcp.search(sterm, options)
        
        tableOutput(result)

if __name__ == '__main__':
    main()