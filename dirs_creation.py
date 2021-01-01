import os

os.chdir('/home/ostap/Documents/python_projects')

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
    try:
        file_name = input('Enter filename\n')
        with open(file_name, 'w') as empt_file:
            pass
    except KeyboardInterrupt:
        break
