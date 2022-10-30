import os
import sys
import logging
import random
from tkinter import image_names
import requests
from screeninfo import get_monitors
from wallpaper4linux.constant import APP_HOME_DIR, ACCESS_TOKEN

logger = logging.getLogger(__name__)

def get_screen_info():
    width = None
    height = None
    for m in get_monitors():
        width = m.width
        height = m.height
    print(f'Screen res : {width}x{height}')
    return width, height

def change_wallpaper(wallpaper_full_path: str):
    cmd = f'gsettings set org.gnome.desktop.background picture-uri {wallpaper_full_path}'
    os.system(cmd)
    logger.info('Wallpaper changed......')

def download_wallpaper(image_save_dir:str=None):
    """
    Dowloads wallpaper image
    Args:
        image_save_dir (str): Directory path to save downloaded wallpaper image
    returns: Full path to wallpaper image
    """

    if not image_save_dir:
        image_save_dir = os.path.join(APP_HOME_DIR, "images")
        
    if not os.path.exists(image_save_dir):
        os.makedirs(image_save_dir)

    while True:
            
        width, height = get_screen_info()
        query_categories = ['buildings', 'workspace', 'Animals', 'Education', 'Cartoons', \
                'food+drink', 'music', 'scifi', 'Places+Monumnets', 'science+technology']
        
        category_idx = random.choice(range(len(query_categories)))
        query = query_categories[category_idx]
        
        editors_choice =  "true"
        per_page = 50
        img_idx = random.choice(range(per_page))
        if not ACCESS_TOKEN:
            logger.error('Access token not found. Please follow User_guide.pdf or readme for '\
                "genrating Access Token from https://pixabay.com/ and adding it to bashrc file. " \
                        "Exiting.....")
            sys.exit(2)
        
        try:
            url = f'https://pixabay.com/api/?key={ACCESS_TOKEN}&q={query}&image_type=photo&min_width={width}&min_height={height}&editors_choice={editors_choice}&per_page={per_page}'
            response = requests.get(url)
            meta = response.json()
            img_name = None
            
            img_name = meta['hits'][img_idx]['id']
            raw_url = meta['hits'][img_idx]['largeImageURL']
            print(img_name, raw_url)
            #img = dic_meta['img']
            response = requests.get(raw_url)
            
            # check if image is already present
            img_path = os.path.join(image_save_dir, str(img_name)+".jpg")
            if os.path.exists(img_path):
                logger.error('Wallpaper is already used')
                
            else:    
                     
                with open(img_path, 'wb') as f: 
                    f.write(response.content)
                return img_path
            
        except requests.HTTPError as e:
            logger.exception("HTTPError:", e)
        except requests.exceptions.RequestException as e:
            logger.exception("RequestException:", e)
        except Exception as e:
            logger.exception(f'download_image: Exception caught, {e}')
