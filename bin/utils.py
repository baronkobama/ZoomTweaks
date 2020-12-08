# Zoom Tweaks BETA - Utility Container

# Standard Libraries
from os import getcwd, mkdir, path, system
import json
import winreg as reg
# External Libraries
import PySimpleGUI as sg
# Constants
from bin.constants import (cache_directory, class_amount_file, class_time_file,
                           class_link_file, scheduler_config_file, reg_path,
                           address)


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
    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, reg_path, 0, reg.KEY_ALL_ACCESS) as registry_key:
            reg.SetValueEx(registry_key, "ZoomTweaks", 0, reg.REG_SZ, address)
            reg.CloseKey(registry_key)
        return True
    except WindowsError:
        print("Caught windows error in add_to_startup()")
        return False


def check_reg_key():
    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, reg_path, 0, reg.KEY_READ) as registry_key:
            value, regtype = reg.QueryValueEx(registry_key, "ZoomTweaks")
            reg.CloseKey(registry_key)
            return value
    except WindowsError:
        print("Caught windows error in check_reg_key()")
        raise
        # return None


def job():
    try:
        system(f"CMD /c python {getcwd()}\\main.py")
        exit(0)
    except KeyboardInterrupt:
        pass
