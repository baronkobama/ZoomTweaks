# Zoom Tweaks - Logger Container

# Standard Libraries
from getpass import getuser
from logging import Formatter, getLogger, DEBUG
from logging.handlers import RotatingFileHandler
from os import path, mkdir

# Constants
zt_directory = path.join(path.expanduser("~{0}".format(getuser())), ".zoomtweaks")
lfile = path.join(zt_directory, "zoomtweaks-py-debug.log")


def get_logger():
    formatter = Formatter(
        "%(asctime)s - %(filename)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
    )
    logfile = lfile

    if not path.isdir(zt_directory):
        mkdir(zt_directory)

    logger = getLogger("zoomtweaks-py-debug")
    logger.setLevel(DEBUG)

    file_handler = RotatingFileHandler(logfile, maxBytes=3145728,
                                       backupCount=1)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


log = get_logger()
