import os,sys
import fnmatch
from color import color
from datetime import datetime

#----------------------------------------------------------

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

#----------------------------------------------------------

def title_options():
    # Title Screen
    title = '\nThe note taking application created by me.\n\n'

    options = '  L)ist the current notes\n' \
        '  N)ote choice\n' \
        '  P)rint the chosen note\n' \
        '  A)dd to the chosen note\n' \
        '  D)elete an entry\n' \
        '  R)eorder entries\n' \
        '  S)ave the current note\n' \
        '  eX)it the program\n' \
        '  H)elp - Display help information\n'
    color.cyan(title + options)

#----------------------------------------------------------

def no_note():
    color.red('\nPlease choose a note to work with')

#----------------------------------------------------------

def create_dir():
    # Create directory if it doesn't exist
    home = os.environ['HOME']
    notes_dir = '{:s}/.notes'.format(home)
    if not os.path.exists(notes_dir):
        os.mkdir(notes_dir)
    
    return notes_dir

#----------------------------------------------------------

def current_notes(notes_dir):
    # Find any existing notes and display names
    note_list = os.listdir(notes_dir)
    note_list = fnmatch.filter(note_list, '*.txt')
    note_list = [x[:-4] for x in note_list] 
    if len(note_list) > 0:
        color.green('\nThe current notes are:')
        for i in range(len(note_list)):
            color.blue('  {0:d}. {1:s}'.format(i+1,note_list[i]))
    else:
        color.green('\nThere are no current notes')

#----------------------------------------------------------

def note(notes_dir):
    # Create note if it doesn't exist otherwise
    # read into a list
    n = input('\nWhat is the name of the note?\n')
    n_file = '{0:s}/{1:s}.txt'.format(notes_dir, n)
    if not os.path.exists(n_file):
        n_list = []
    else:
        x = open(n_file, 'r').read().splitlines()
        n_list = [[line[:-9],line[-8:]] for line in x]

    return n, n_list, n_file

#----------------------------------------------------------

def print_note(n, n_list):
    # Print the contents of the note
    color.green('\n{0:s}'.format(n.capitalize()))
    for i in range(len(n_list)):
        print('  {0:d}. {1:s}\t{2:s}'.format(i+1, n_list[i][0], \
            n_list[i][1]))

#----------------------------------------------------------

def add_entry(n_list):
    # Add an entry to the note
    clear_screen()
    color.two_types(color.PURPLE,color.UNDERLINE,'Enter your note:\n')
    note_input = input()
    date = datetime.now().strftime('%m/%d/%y')
    n_list.append([note_input,date])

    return n_list

#----------------------------------------------------------

#def edit_entry(n_list):
    # Do something

#----------------------------------------------------------

def delete_entry(n_list):
    # Delete an entry from the note
    del_num = input('\nWhich entry would you like to delete? (All or number)\n')
    try:
        int(del_num)
        del n_list[int(del_num)-1]
        return n_list
    except:
        pass

    if del_num.lower() in ['all','a']:
        del n_list[:]
    else:
        color.red('That is an invalid entry.')

    return n_list

#----------------------------------------------------------

def reorder_note(n_list):
    # Reorder the note entries
    while True:
        try:
            move = int(input('\nWhich entry would you like to move?\n'))
            break
        except:
            print('You need to enter an integer')
    while True:
        try:
            loc = int(input('\nWhere would you like to put it?\n'))
            break
        except:
            print('You need to enter an integer')

    x = n_list.pop(move-1)
    n_list.insert(loc-1,x)

    return n_list

#----------------------------------------------------------

def save_note(n_list, n_file):
    # Write the list to the file
    with open(n_file, 'w') as f:
        for i in range(len(n_list)):
            f.write(n_list[i][0] + ' ' + n_list[i][1] + '\n')

#----------------------------------------------------------

def help_info():
    color.two_types(color.GREEN,color.UNDERLINE,'Saving')
    s_help = '\tAll entried are saved upon changing to a differ-\n' \
        '\tent note or upon exit. Notes can also be saved\n' \
        '\tusing the S command from the title page.'
    color.cyan(s_help)

    color.two_types(color.GREEN,color.UNDERLINE,'Listing')
    l_help = '\tThis command lists the notes that are currently\n' \
        '\tpresent in the ~/.notes/ directory. All notes\n' \
        '\twill be saved to this directory as plain text\n' \
        '\tfiles'
    color.cyan(l_help)

    color.two_types(color.GREEN,color.UNDERLINE,'Note Choice')
    n_help = '\tAllows the user to choose one of the notes alrea-\n' \
        '\tdy present as shown with the L command, or to cr-\n' \
        '\teate a new note.'
    color.cyan(n_help)

    color.two_types(color.GREEN,color.UNDERLINE,'Print')
    p_help = '\tPrints an ordered list of entries within the note\n' \
        '\tchosen with the L command. The numbers prior to\n' \
        '\teach entry are used for reordering the note with\n' \
        '\tthe R command.'
    color.cyan(p_help)

    color.two_types(color.GREEN,color.UNDERLINE,'Add')
    a_help = '\tAdds an entry to the end of the note selected wi-\n' \
        '\tth the L command.'
    color.cyan(a_help)
    
    color.two_types(color.GREEN,color.UNDERLINE,'Delete')
    d_help = '\tDeletes an entry of the selected note. The number\n' \
        '\tcorresponds to the number shown prior to the entry\n' \
        '\twith the L command.'
    color.cyan(d_help)
    
    color.two_types(color.GREEN,color.UNDERLINE,'Reorder')
    r_help = '\tReorders entries within the note selected. Numbe-\n' \
        '\trs correspond to those shown with the L command.\n' \
        '\tThe first number input is the note to be moved and\n' \
        '\tthe second is the location to put it.'
    color.cyan(r_help)
    
    color.two_types(color.GREEN,color.UNDERLINE,'Exit')
    e_help = '\tExits the program after saving the current note.'
    color.cyan(e_help)
    
    color.two_types(color.GREEN,color.UNDERLINE,'Help')
    h_help = '\tDisplays this screen.'
    color.cyan(h_help)
    
    print('\n')
    color.red('Press enter to return to the main menu') 
    main_menu = input()
    if main_menu:
        return

#----------------------------------------------------------
