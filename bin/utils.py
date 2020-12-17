# Zoom Tweaks - Utility Container

# Standard Libraries
from datetime import datetime
from getpass import getuser
from os import getcwd, mkdir, path, system
import json
import subprocess
import win32api
# External Libraries
import PySimpleGUI as sg

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
        break
    else:
        continue
startup_file = path.join(startup_path, "ZoomTweaks.bat")
file_path = path.join((path.dirname(path.realpath(__file__)).strip(r"\bin")), "scheduler.py")
file_path = file_path.split('\\')
index = -1
for name in file_path:
    index += 1
    if " " in name:
        file_path[index] = ('"' + name + '"')
file_path = '\\'.join([str(elem) for elem in file_path])

# Functions


def file_reset(file):
    try:
        with open(file, "w+") as f:
            f.close()
    except Exception as exc:
        print("")
        print("Caught exception in file_reset()")
        print("")
        print(str(exc))


def config_file_check(file):
    try:
        file_size = path.getsize(file)
        if not file_size > 0:
            # Returns True if file is empty
            return True
        else:
            # Returns False if file is not empty
            return False
    except FileNotFoundError:
        print("Missing file(s) in file check instance")
        pass


def retriever(layout, output):
    sg.theme('LightBrown8')
    window = sg.Window('ZoomTweaks-PY-v2.0.0-beta.py', layout)
    while True:
        if config_file_check(output):
            pass
        else:
            break
        event, values = window.read()
        if event == "Ok":
            with open(output, "a+") as cache:
                json.dump(values, cache)
            window.close()
            return True
        elif event == sg.WIN_CLOSED or event == 'Cancel':
            print("Script cancelled.")
            window.close()
            exit(1)


def cache_check():
    try:
        if not path.isdir(cache_directory):
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
            if not path.isfile(class_amount_file):
                file_reset(class_amount_file)
            if not path.isfile(class_time_file):
                file_reset(class_time_file)
            if not path.isfile(class_link_file):
                file_reset(class_link_file)
            if not path.isfile(scheduler_config_file):
                with open(scheduler_config_file, "w+") as f:
                    f.truncate()
                    # 0 = No startup file ---- 1 = Startup file
                    f.write('{"startup": "0"}')
                    f.close()
            return True
        return True
    except Exception as exc:
        print("")
        print("Caught exception in cache_check()")
        print("")
        print(str(exc))
        return False


def add_to_startup():
    python_directories = subprocess.check_output("where python", shell=True)
    python_directories = str(python_directories).strip('"' + "b" + "'").split(r'\r\n')
    for directory in python_directories:
        if 'AppData' not in directory:
            python_directories.remove(directory)
        if 'Microsoft' in directory:
            python_directories.remove(directory)
    python_dir = python_directories[0]
    with open(startup_file, "w+") as f:
        f.writelines("@echo off\n")
        f.writelines(f'"{python_dir}" "{file_path}"\n')
        f.writelines("pause")
        f.close()


def check_startup_file():
    if path.isfile(startup_file):
        return True
    else:
        return False


def job():
    try:
        system(f"CMD /c python {getcwd()}\\main.py")
        exit(0)
    except KeyboardInterrupt:
        pass
