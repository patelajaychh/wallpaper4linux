import logging
from wallpaper4linux.constant import LOG_PATH

log_level = "DEBUG"
formatter = logging.Formatter(
             fmt= "[%(asctime)s] %(levelname)s - %(message)s",
             datefmt='%Y-%m-%d %H:%M:%S'
        )

file_handler = logging.FileHandler(filename=LOG_PATH, mode='a')
file_handler.setFormatter(formatter)
file_handler.setLevel(log_level)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(log_level)


logger = logging.getLogger(__name__)
logger.setLevel(log_level)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.propagate=False