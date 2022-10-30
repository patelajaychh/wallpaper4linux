import os
from datetime import datetime

HOME_DIR = os.path.expanduser("~")
APP_HOME_DIR = os.path.join(HOME_DIR, ".wallpaper4linux")
DB_PATH = os.path.join(APP_HOME_DIR, "w4l_app.db")
LOG_PATH = os.path.join(APP_HOME_DIR, '{:%Y-%m-%d}.log'.format(datetime.now()))

if not os.path.exists(APP_HOME_DIR):
    os.makedirs(APP_HOME_DIR)

ACCESS_TOKEN = os.getenv("PX_ACCESS_TOKEN", None)    