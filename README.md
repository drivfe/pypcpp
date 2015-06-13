# PYPCPP
(Unofficial) Command line interface for searching parts on pcpartpicker.
Official website: https://pcpartpicker.com

Python 3.x only.

## Installation
```
git clone https://github.com/drivfe/pypcpp.git
cd pypcpp
python pypcpp
```
**Requirements** (All via pip):
* requests
* BeautifulSoup4
* PrettyTable

## Usage
```sh
  pypcpp.py (-c | -v | -r | -m | -t | -p | -s) <search>... [--sort=<sort> [-a | -d]] [-l]
  pypcpp.py logininfo --user=<username> --pass=<password>
  pypcpp.py logininfo
  pypcpp.py (-h | --help)
```
#### Options
```sh
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
  -l, --login        Login before doing search
  --user=<username>  Save username to config file
  --pass=<password>  Save password to config file
 ```

## Examples
Basic examples:
```sh
python pypcpp -v r9 280
python pypcpp -s 128gb ssd samsung
python pypcpp -r corsair vengeance --sort=speed -d # print the fastest RAMs
```

To log in you have to set up your username and password. (This is needed if you want your settings such as 'include mail-in rebates' to affect the output):
```sh
python pypcpp logininfo --user=USERHERE --pass=PASSHERE # set credentials
python pypcpp logininfo # will output your credentials
```

After you have set up your login info you can use the '-l/--login' switch and the program will log you in before performing a search:
```sh
python pypcpp --cpu fx 6300 -l
python pypcpp --storage western digital 1tb --sort=type -a -l # check the notes for more info on what to pass to --sort
python pypcpp -v r9 280 --sort=coreclock -d --login # This will list all r9 280s sorted by their coreclock speed in descending order after logging in on your account.
```

Here is the ouput of the last example:
```sh
Searching 'r9 280' of 'VideoCard' sorted by coreclock in descending order.

 VIDEOCARD   SERIES              CHIPSET  MEMORY  CORECLOCK  PRICE
 XFX         Double Dissipation  R9 280X  3GB     1.08Ghz    $242.98
 XFX         Double Dissipation  R9 280   3GB     1.0GHz     $149.99
 Gigabyte    WINDFORCE           R9 280   3GB     950MHz     $172.98
 PowerColor  TurboDuo            R9 280X  3GB     880MHz     $207.98
 PowerColor  TurboDuo            R9 280   3GB     855MHz     $188.89
 Sapphire    DUAL-X              R9 280   3GB     850MHz     $162.98
 XFX         Double Dissipation  R9 280X  3GB     850MHz     $237.50
 VisionTek                       R9 280X  3GB     850MHz     $271.98
 Sapphire    Dual-X              R9 280   3GB     850MHz     $149.99
 XFX         Double Dissipation  R9 280   3GB     827MHz     $193.98
 Club        royalKing           R9 280   3GB     N/A        $299.99
 Sapphire    Dual-X              R9 280X  3GB     N/A        $229.99
```

### Notes:
* Will sort by speed by default 
* Will sort in ascending order by default.
* Some info (such as price/gb for HDD/SSDs) are omitted because they are too long to fit the command line interface.
* To know what to pass to the --sort argument, check the table header on pcpartpicker.com
	* Go to: http://pcpartpicker.com/parts/power-supply/
	* Say you want to sort by watts, you use --sort=watts or --sort=modular to sort by the 'modular' column
		* If the header has a space in it, remove it. (e.g. core clock -> coreclock)
* Python 3.x