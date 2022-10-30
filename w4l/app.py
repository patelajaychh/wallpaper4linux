import multiprocessing
import time
from screeninfo import get_monitors
import os
from datetime import datetime as dt
import sys
import logging
from retry import retry
from w4l.constant import DB_PATH
from w4l.db_connection import (
    get_details_by_date, 
    create_wallpaper_details_table, 
    update_wallpaper_details_table,
    wallpaper_details_table_exist
)
from w4l.utils import change_wallpaper, download_wallpaper


logger = logging.getLogger(__name__)

    
    
MAX_RETRY = 5
# @retry(tries=MAX_RETRY, deplay=5)
def start_app():
    logger.info("Wallpaper4Linux application STARTED")
    todays_date = str(dt.today().date())

    if not wallpaper_details_table_exist():
        # logger.info("Initializing Database...")
        print("Initializing Database...")
        create_wallpaper_details_table()
    
    else:
        details = get_details_by_date(todays_date)
        if details:
            return 

    img_path = download_wallpaper()
    change_wallpaper(img_path)
    img_name = os.path.basename(img_path)
    update_wallpaper_details_table(date=todays_date, wallpaper_name=img_name)
    return 

def wallpaper4inux_main():
    """This is entry point of application"""
    # time.sleep(30)
    try:
        while True:
            proc = multiprocessing.Process(target=start_app)
            proc.start()
            proc.join()
            if proc.exitcode!=0:
                logger.error("Application restarted...")
                time.sleep(10)
            else:
                #Going to Sleep
                logger.info("Going to to sleep for 2Hrs....")
                time.sleep(3600)
            
    except (KeyError, KeyboardInterrupt):
        sys.exit(1)
    except Exception as e:
        logger.exception("Exception occured in starting application:", e)
        sys.exit(2)
