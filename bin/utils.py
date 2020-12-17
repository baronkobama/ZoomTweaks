# Zoom Tweaks - Utility Container

# Standard Libraries
from datetime import datetime
from getpass import getuser
from os import getcwd, mkdir, path, system
from sys import argv
import json
import subprocess
import win32api
# External Libraries
import PySimpleGUI as sg
# ZoomTweaks-PY (other) Functions
from bin.logger import log, lfile

# Constants
cache_directory = path.join(getcwd(), "cache")
class_amount_file = path.join(cache_directory, "classAmount.json")
class_time_file = path.join(cache_directory, "classTimes.json")
class_link_file = path.join(cache_directory, "classLinks.json")
clAmountLayout = [[sg.Text("Input the amount of classes you have.")],
                  [sg.Text("Input the amount as '5' or '6', etc."),
                   sg.InputText()],
                  [sg.Button("Ok"), sg.Button("Cancel")],
                  [sg.Text("*This won't change unless you delete files and reinstall*")]]
clTimesLayout = []
clLinksLayout = []
updated_times_list = []
now = datetime.now()
current_time = now.strftime('%H:%M')
scheduler_config_file = path.join(cache_directory, "schedulerConfig.json")
startup_path = ""
drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
for drive in drives:
    startup_path = rf'{drive}Users\{getuser()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    if path.isdir(startup_path):
        log.debug(f"Found startup path at: {startup_path}")
        break
    else:
        continue
startup_file = path.join(startup_path, "ZoomTweaks.bat")
file_path = path.join((path.dirname(path.realpath(__file__)).strip(r"\bin")), "scheduler.py")

# Functions


def file_reset(file):
    try:
        with open(file, "w+") as f:
            f.close()
        log.debug(f"Successfully reset {file}")
    except Exception as exc:
        log.debug("Caught exception in file_reset()")
        log.debug(str(exc))
        print(f"Check {lfile} for more info (debug log)")
        return False


def config_file_check(file):
    try:
        file_size = path.getsize(file)
        if not file_size > 0:
            # Returns True if file is empty
            log.debug(f"{file} is empty")
            return True
        else:
            # Returns False if file is not empty
            log.debug(f"{file} is not empty")
            return False
    except FileNotFoundError:
        log.debug(f"Missing {file} in file check instance, caught FileNotFoundError")
        pass


def retriever(layout, output):
    sg.theme('LightBrown8')
    window = sg.Window('ZoomTweaks-PY-v2.0.0-beta.py', layout)
    while True:
        if config_file_check(output):
            pass
        else:
            break
        log.debug("Awaiting input in window")
        event, values = window.read()
        if event == "Ok":
            with open(output, "a+") as cache:
                json.dump(values, cache)
            window.close()
            log.debug("Dumped input from window, exiting retriever")
            return True
        elif event == sg.WIN_CLOSED or event == 'Cancel':
            print("Script cancelled.")
            window.close()
            log.debug("Script was cancelled by user input")
            exit(1)


def cache_check():
    try:
        if not path.isdir(cache_directory):
            log.debug("Couldn't find cache directory, writing dir and files")
            mkdir(cache_directory)
            file_reset(class_amount_file)
            file_reset(class_time_file)
            file_reset(class_link_file)
            with open(scheduler_config_file, "w+") as f:
                f.truncate()
                # 0 = No startup key --- 1 = Startup key
                f.write('{"startup": "0"}')
                f.close()
            return True
        elif path.isdir(cache_directory):
            log.debug("Found cache directory, checking file integrity")
            if not path.isfile(class_amount_file):
                log.debug("Couldn't find class amount file, writing file")
                file_reset(class_amount_file)
            if not path.isfile(class_time_file):
                log.debug("Couldn't find class time file, writing file")
                file_reset(class_time_file)
            if not path.isfile(class_link_file):
                log.debug("Couldn't find class link file, writing file")
                file_reset(class_link_file)
            if not path.isfile(scheduler_config_file):
                log.debug("Couldn't find scheduler config file, writing file")
                with open(scheduler_config_file, "w+") as f:
                    f.truncate()
                    # 0 = No startup file ---- 1 = Startup file
                    f.write('{"startup": "0"}')
                    f.close()
            log.debug("Finished checking file integrity")
            return True
        return True
    except Exception as exc:
        log.debug("Caught exception in cache_check()")
        log.debug(str(exc))
        print(f"Check {lfile} for more info (debug log)")
        return False


def add_to_startup():
    python_directories = subprocess.check_output("where python", shell=True)
    python_directories = str(python_directories).strip('"' + "b" + "'").split(r'\r\n')
    for directory in python_directories:
        if 'AppData' not in directory:
            python_directories.remove(directory)
            log.debug("Removing invalid python directory")
        if 'Microsoft' in directory:
            python_directories.remove(directory)
            log.debug("Removing invalid python directory")
        if 'python.exe' not in directory:
            python_directories.remove(directory)
            log.debug("Removing invalid python directory")
    python_dir = python_directories[0]
    python_dir = python_dir.replace("python.exe", "pythonw.exe")
    with open(startup_file, "w+") as f:
        f.writelines("@echo off\n")
        f.writelines(f'"{python_dir}" "{file_path}"\n')
        f.writelines("exit")
        f.close()
    log.debug("Wrote startup file")


def check_startup_file():
    if path.isfile(startup_file):
        log.debug("Located startup file")
        return True
    else:
        log.debug("Could not locate startup file")
        return False


def job():
    try:
        system(f"CMD /c python {getcwd()}\\main.py")
        with open(lfile, "w+") as f:
            f.truncate()
            f.close()
        log.debug("Passing control to main.py")
        exit(0)
    except KeyboardInterrupt:
        pass


def proc_init():
    log.debug("=============")
    log.debug("=NEW PROCESS=")
    log.debug("=============")
    log.debug("Exec file: {0}".format(str(argv)))
