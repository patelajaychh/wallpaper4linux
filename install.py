#!/usr/local/bin/python3

import os

home_dir = os.getenv('HOME')
project_dir = home_dir+'/wallpaper4linux'

cwd = os.getcwd()
print(project_dir, cwd)

if project_dir != cwd:
    print('Project is not in home directory. \nPlease move project dir into user HOME directory and follow installation instructions.')
    exit()
else:
    os.system(f'echo "/usr/local/bin/python3 {home_dir}/wallpaper4linux/app.py>>/dev/null&" >> ~/.bashrc')
    os.system('bash')