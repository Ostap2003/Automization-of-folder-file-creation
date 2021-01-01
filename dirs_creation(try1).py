""" Module that automizes precess of directories and files creation """

import os

cwd = '/home/ostap/Documents/python_projects'
os.chdir(cwd)

usr_dir = input('/home/ostap/Documents/python_projects/\n')
if usr_dir != '':
    os.chdir(usr_dir)

# here user can skip
create_dir = input('Enter what dirs you want to create\n')

# if user don't want to create folder, then don't make dirs
if create_dir != '':
    os.makedirs(create_dir)
    os.chdir(create_dir)


while True:
    file_name = input('Enter filename\n')
    if file_name != '':
        with open(file_name, 'w') as empt_file:
            pass
    else:
        break