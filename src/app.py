from src import one
from src import two
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--module", help="Run the specified module.  Accepts ['one', 'two']")
parser.add_argument("--path", help="Path to be supplied to module one.  Note: only tested on unix filesystem", default="")
parser.add_argument("--string", help="String to be supplied to module two", default="")
args = parser.parse_args()

if args.module == 'one':
    if args.path != '':
        one.run((args.path))
    else:
        print('You must supply an argument to `path` to use this module.  For help, run: \n\n\tpython3 -m src.app -h \n')
elif args.module == 'two':
    if args.string != '':
        print(two.count_recurring(args.string))
    else:
        print('You must supply an argument to `string` to use this module.  For help, run: \n\n\tpython3 -m src.app -h \n')
