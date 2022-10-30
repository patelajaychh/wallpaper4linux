#!/usr/bin/python3

# import os

# home_dir = os.getenv('HOME')
# project_dir = home_dir+'/wallpaper4linux'
# python_home = None
# while 1:
#     python_home = input('Enter correct python3 location ... ')
#     if os.path.isfile(python_home):
#        break 

# cwd = os.getcwd()
# print(project_dir, cwd)

# if project_dir != cwd:
#     print('Project is not in home directory. \nPlease move project dir into user HOME directory and follow installation instructions.')
#     exit()
# else:
#     os.system(f'echo "{python_home} {home_dir}/wallpaper4linux/app.py>>/dev/null&" >> ~/.bashrc')
#     os.system('bash')

from setuptools import setup, find_packages

PACKAGE_NAME="w4l"
PACKAGE_VERSION="0.1-beta"
AUTHER_NAME = "AJAY KUMAR PATEL"
AUTHER_EMAIL = "PATELAJAYCHH@gmail.com"

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description="Linux Wallpaper application",
    author=AUTHER_NAME,
    author_email=AUTHER_EMAIL,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    python_requires=">=3.6, <4",
    install_requires=[
        "requests",
        "screeninfo"
    ],
    
    entry_points={
       "console_scripts":[
           "w4l-app-start=w4l.app:wallpaper4inux_main"
       ] 
    },
)