""" Module that automizes precess of directories and files creation """

import os

cwd = '/home/ostap/Documents/python_projects'
os.chdir(cwd)

usr_inp = input(f'{cwd}\n')  # 'dir1/dir2/dir3 fold1.txt;;fold2.py'

usr_dirs = usr_inp.split(' ')[0].split('/')
usr_fold = usr_inp.split(' ')[1].split(';')

dirs_in_cwd = os.listdir(cwd)

for i in range(len(usr_dirs)):
    cwd += '/' + usr_dirs[i]

    if usr_dirs[i] in dirs_in_cwd:
        os.chdir(cwd)
    else:
        os.mkdir(cwd)
        os.chdir(cwd)
    
    if usr_fold[i] != '':
        with open(usr_fold[i], 'w') as empt_fl:
            pass
