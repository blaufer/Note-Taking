import os,sys
import csv

name = 'to_do.txt'
if not os.path.exists(name):
    open(name, 'w').close()

todo_dict = {}

note1 = 'Hi'
note2 = 'Hell'

notes = [note1,note2]

for i in range(len(notes)):
    todo_dict[i] = notes[i]

with open(name, 'w') as wf:
    for key in todo_dict:
        wf.write('{0:d},{1:s}'.format(key,todo_dict[key]))
        wf.write('\n')

reader = csv.reader(open(name, 'r') )
imp_dict = {}
for row in reader:
    key, value = row
    imp_dict[key] = value

print(imp_dict)
