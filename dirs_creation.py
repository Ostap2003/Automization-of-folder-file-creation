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


# usr_dir = input('/home/ostap/Documents/python_projects/\n')
# if usr_dir != '':
#     os.chdir(usr_dir)

# # here user can skip
# create_dir = input('Enter what dirs you want to create\n')

# # if user don't want to create folder, then don't make dirs
# if create_dir != '':
#     os.makedirs(create_dir)
#     os.chdir(create_dir)


# while True:
#     file_name = input('Enter filename\n')
#     if file_name != '':
#         with open(file_name, 'w') as empt_file:
#             pass
#     else:
#         break