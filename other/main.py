import os,sys
import argparse
from datetime import datetime
# Use datetime.now() to get current date and time
# Use datetime.now().year (or .day, or .month, etc.)
# to get specific year

#----------------------------------------------------------

def files():
    '''
    Create the necessary files if they don't already exist
    '''
    # Find user home directory
    home = os.environ['HOME']

    # Notes directory, create if not present
    notes_dir = '{:s}/.notes'.format(home)
    if not os.path.exists(notes_dir):
        os.mkdir(notes_dir)

    # Create lists
    to_do = '{:s}/to_do.txt'.format(notes_dir)
    running = '{:s}/runnning.txt'.format(notes_dir)
    completed = '{:s}/completed.txt'.format(notes_dir)
    lists = [to_do, running, completed]
    for name in lists:
        if not os.path.exists(name):
            open(name, 'w').close()

    return to_do,running,completed

#----------------------------------------------------------

def arg_vals(argv=None):
    '''
    Parse the command line input
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--add',help='Add an item')
    parser.add_argument('-l','--list',help='List contents of a note',action='store_true')
    parser.add_argument('-t','--todo',help='Access to do list',action='store_true')
    parser.add_argument('-c','--completed',help='Access completed list',action='store_true')
    parser.add_argument('-r','--running',help='Access running list',action='store_true')
    
    return parser.parse_args()

#----------------------------------------------------------

def which_list(args):
    '''
    Choose which list(s) is being used
    '''
    if args.todo:
        nname = to_do
    elif args.completed:
        nname = completed
    elif args.running:
        nname = running
    else:
        nname = [to_do, running, completed]

    return nname

#----------------------------------------------------------

def print_list(nname):
    count = 1
    with open(nname, 'r') as wf:
        print('-------------------------------------------')
        for line in wf:
            print('{0:d}. {1:s}'.format(count, line.rstrip()))
            count += 1
        print('-------------------------------------------')

#----------------------------------------------------------

# Run the program

to_do,running,completed = files()
args = arg_vals()
nname = which_list(args)

if args.add is not None:
    if isinstance(nname, list):
        print('You have to choose a list to add to.')
        sys.exit(1)
    else:
        with open(nname, 'a') as wf:
            wf.write(args.add)
            wf.write('\n')

if args.list:
    if isinstance(nname, list):
        print_list(nname[0])
        print_list(nname[1])
        print_list(nname[2])
    else:
        print_list(nname)
