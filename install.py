#!/usr/bin/python3

import os

home_dir = os.getenv('HOME')
project_dir = home_dir+'/wallpaper4linux'
python_home = None
while 1:
    python_home = input('Enter correct python3 location ... ')
    if os.path.isfile(python_home):
       break 

cwd = os.getcwd()
print(project_dir, cwd)

if project_dir != cwd:
    print('Project is not in home directory. \nPlease move project dir into user HOME directory and follow installation instructions.')
    exit()
else:
    os.system(f'echo "{python_home} {home_dir}/wallpaper4linux/app.py>>/dev/null&" >> ~/.bashrc')
    os.system('bash')