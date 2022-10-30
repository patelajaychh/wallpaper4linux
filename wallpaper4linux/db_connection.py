import os
from wallpaper4linux.constant import DB_PATH
import sqlite3 as sqlite
import logging

logger = logging.getLogger(__name__)

def SQLiteConnection():
    try:
        db_path = os.path.join(DB_PATH)
        con = sqlite.connect(db_path, timeout=100)
        cur = con.cursor()
        return con, cur
    
    except sqlite.OperationalError as e:
        logger.exception("DB Exception-", e)
        raise Exception from e
    
def list_db_tables():
    
    con, cur = SQLiteConnection()
    cur.execute(
        "SELECT name from sqlite_master WHERE type='table'"
    )
    status = cur.fetchall()
    con.commit()
    
    cur.close()
    con.close()
    return status

def create_wallpaper_details_table():
    con, cur = SQLiteConnection()
    # Date Format 'YYYY-MM-DD'
    cur.execute(
        """CREATE TABLE wallpaper_details (
            date text,
            filename text, 
            status integer  default 0
            )
        """ 
    )    
    con.commit()
    logger.info("create_wallpaper_details_table table created ......")
    cur.close()
    con.close()
    return True

def wallpaper_details_table_exist():
    try:
        con, cur = SQLiteConnection()
        cur.execute(
            "SELECT name from sqlite_master WHERE type='table' AND name='wallpaper_details'"
        )
        status = cur.fetchall()
        con.commit()
        
        cur.close()
        con.close()
        return len(status)
    except sqlite.OperationalError as e:
        logger.exception(e)
        return 0
    
def update_wallpaper_details_table(date: str, wallpaper_name:str):
    """
    Args:
        date (str): Date in string format. (YYY-MM-DD)
        wallpaper_name (str): Filename of the image
    """
    con, cur = SQLiteConnection()
    cur.execute(
        """INSERT INTO wallpaper_details (date, filename) 
            VALUES (:date, :filename)""",
            {"date": date, "filename":wallpaper_name},
    )
    con.commit()
    
    cur.close()
    con.close()
    return True

def get_details_by_date(date: str):
    con, cur = SQLiteConnection()
    cur.execute(
        "SELECT * from wallpaper_details WHERE date=:date",
            {"date": date},
    )
    deatils = cur.fetchall()
    if deatils:
        deatils = list(deatils)
    con.commit()
    
    cur.close()
    con.close()
    return deatils
    
def get_details_by_wallpaper_name(wallpaper_name: str):
    
    con, cur = SQLiteConnection()
    cur.execute(
        "SELECT * from wallpaper_details WHERE filename=:filename",
            {"filename": wallpaper_name},
    )
    deatils = cur.fetchall()
    if deatils:
        deatils = list(deatils)
    con.commit()
    
    cur.close()
    con.close()
    return deatils
