import requests
import random
from screeninfo import get_monitors
import os
from datetime import datetime as dt
import random
import sys
import base64
import time
import atexit
import pathlib
import logging

logger = None

def get_screen_info():
    width = None
    height = None
    for m in get_monitors():
        width = m.width
        height = m.height
    print(f'Screen res : {width}x{height}')
    return width, height

def download_image(image_save_dir, home_dir):
    
    key = None
    width, height = get_screen_info()
    query_categories = ['buildings', 'workspace', 'Animals', 'Education', 'Cartoons', \
            'food+drink', 'music', 'Places+Monumnets', 'science+technology']
    category_idx = random.choice(range(len(query_categories)))
    query = query_categories[category_idx]
    editors_choice =  "true"
    per_page = 50
    img_idx = random.choice(range(per_page))
    if not os.path.exists(f'{home_dir}/wallpaper4linux/.data/file'):
        print('Access token has been deleted please reinstall application........')
        logger.info('Access token has been deleted please reinstall application........ Exiting...')
        exit()
    with open(f'{home_dir}/wallpaper4linux/.data/file', 'r') as f:
        key = f.readline()[2:]
    key = key.encode('ascii')
    key = base64.b64decode(key)
    key = key.decode('ascii')

    url = f'https://pixabay.com/api/?key={key}&q={query}&image_type=photo&min_width={width}&min_height={height}&editors_choice={editors_choice}&per_page={per_page}'
    response = requests.get(url)
    meta = response.json()
    #print(meta)
    img_name = None
    try:
        img_name = meta['hits'][img_idx]['id']
        raw_url = meta['hits'][img_idx]['largeImageURL']
        print(img_name, raw_url)
        #img = dic_meta['img']
        response = requests.get(raw_url)
        
        # check if image is already present
        if os.path.exists(f'{image_save_dir}/{img_name}.jpg'):
            sys.stderr.write('Wallpaper is already used')
            return download_image(image_save_dir, home_dir)
            
        else:         
            with open(f'{image_save_dir}/{img_name}.jpg', 'wb') as f: 
                f.write(response.content)
            
    except Exception as e:
        return download_image(image_save_dir, home_dir)
    
    print(f'new wallpaper {img_name} downloaded ... ')
    return img_name


def cleanup(pid_file):

    if os.path.exists(pid_file):
        os.remove(pid_file)
        logger.info('Program interrupted.. cleaning PID and exiting....')

def main(): 

    global logger
    
    home_dir = os.path.expanduser("~")
    app_root_dir = f'{home_dir}/wallpaper4linux/'

    logfile = f'{app_root_dir}/log/run.log'
    if not os.path.exists(logfile):
        os.makedirs(logfile)
    
    logging.basicConfig(
        filename=logfile, 
        level=logging.INFO, 
        format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logger = logging.getLogger('wallpaper4linux')
    
    # Checking if application is already running
    pid = str(os.getpid())
    pid_file_path = f'{home_dir}/wallpaper4linux/.data/pid/'
  
    if not os.path.exists(pid_file_path):
        os.makedirs(pid_file_path)

    pid_file = os.listdir(pid_file_path)

    if len(pid_file)>0:
        print('Applicatin already in runing state....')
        logger.info("Application run requested. Found already running")
        exit()
    else:
        pid_file_path = pid_file_path+'/'+pid
        pathlib.Path(pid_file_path).touch()
        logger.info(f'Application started with PID {pid}')

    
    while(1):
        now = dt.today().date()
        text_file = os.path.join(app_root_dir, '.data', 'record')
        saved_state = 'None'
        with open(text_file,'r') as f:
            saved_state = f.readline()
        if saved_state=='':
            saved_state = "1990-01-01"
        
        saved_state = dt.strptime(saved_state, "%Y-%m-%d").date()
        if now>saved_state:
            
            
            image_save_dir = f'{home_dir}/wallpaper4linux/downloaded_wallpapers/'
            if not os.path.exists(image_save_dir):
                os.makedirs(image_save_dir)
                
            image_name = download_image( image_save_dir, home_dir )
            #image_full_path = os.getcwd()+'/'+image_save_dir+str(image_name)+'.jpg'
            image_full_path = image_save_dir+'/'+str(image_name)+'.jpg'
            print(image_full_path)
            cmd = f'gsettings set org.gnome.desktop.background picture-uri {image_full_path}'
            os.system(cmd)
            logger.info('Wallpaper changed......')

            #updating date into file
            with open(text_file, 'w') as f:
                f.write(str(now))

            logger.info('Record date updated to today')

        time.sleep(7200)
        
    atexit.register(cleanup, pid_file_path) 
        


if __name__== "__main__":
    main()
    
            
