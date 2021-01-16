"""
Module that automizes precess of directories and files creation

===== SYNTAX ======

To create folders just type their names using '/' like so: dir1/dir2...
To create files in the folders type their names using ';' separator.*

* if you want several files to be created in a specific folder, then
  use the following syntax: [folder1.txt,folder2.txt]
  use comma as a separator inside square brackets

The input needs to look like this:
dir1/dir2/dir3 file1;file2;dir3  <- ! USE EMPTY SPACE AS A SEPARATOR BETWEEN DIRS NAMES AND FILE NAMES,
                                      otherwise an exception will occur.


IF you don't want to create any files in a specific folder, then
the input needs to look like this:
dir1/dir2 ;file_in_folder2.txt  <- here we created file only in the second directory

IF you don't want to create any files in a directory, then type ';' separators instead of the file names.*
* the number of the separators needs to be (number of created folders - 1), otherwise
  an exception will occur.
  EXAMPLE: dir1/dir2 ;

"""

import os

cwd = '/home/ostap/Documents/python_projects'
os.chdir(cwd)

usr_inp = input(f'{cwd}\n').split()

usr_dirs = usr_inp[0].split('/')
usr_fold = usr_inp[1].split(';')

for i in range(len(usr_dirs)):
    dirs_in_cwd = os.listdir(cwd)  # list of existing dirs in a cwd
    cwd += '/' + usr_dirs[i]

    if usr_dirs[i] in dirs_in_cwd:
        os.chdir(cwd)
    else:
        os.mkdir(cwd)
        os.chdir(cwd)
    
    if usr_fold[i] != '':
        if usr_fold[i][0] == '[':  # can be several folders
            usr_fold[i] = usr_fold[i][1:-1].split(',')

            for folder in usr_fold[i]:
                with open(folder, 'w') as empt_fl:
                    pass

        else:
            with open(usr_fold[i], 'w') as empt_fl:
                pass
