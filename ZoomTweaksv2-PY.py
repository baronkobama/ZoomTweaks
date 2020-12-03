# Zoom Tweaks BETA - Python Rewrite

# Standard Libraries
from datetime import datetime
from os import mkdir, getcwd, path
import json
# External Libraries
import PySimpleGUI as sg

print(datetime)
print(mkdir)
print(getcwd)
print(path)
print(json)
print(sg)

cache_directory = path.join(getcwd(), "cache")
class_amount_file = path.join(cache_directory, "classAmount.json")
class_time_file = path.join(cache_directory, "classTimes.json")


def file_reset(file):
    with open(file, "w+") as f:
        f.truncate()
        f.close()


def cache_check():
    if not path.isdir(cache_directory):
        print("No cache directory, making dir")
        mkdir(cache_directory)
        file_reset(class_amount_file)
        print("Class amount file written")
        file_reset(class_time_file)
        print("Class times file written")
        print("Directory and files written")
        return True
    elif path.isdir(cache_directory):
        print("Cache directory detected")
        if not path.isfile(class_amount_file):
            print("No class amount file, writing file")
            file_reset(class_amount_file)
            print("Class amount file written")
        if not path.isfile(class_time_file):
            print("No class times file, writing file")
            file_reset(class_time_file)
            print("Class times file written")
        print("Files written")
        return True
    print("Nothing written in cache_check")
    return True


def config_file_check(file):
    file_size = path.getsize(file)
    if not file_size > 0:
        # Returns True if file is empty
        return True
    else:
        # Returns False if file is not empty
        return False


def class_amount_retrieve():
    sg.theme('LightGrey1')
    clAmountLayout = [[sg.Text("Input the amount of classes you have.")],
                      [sg.Text("Input the amount as '5' or '6', etc."),
                       sg.InputText()],
                      [sg.Button("Ok"), sg.Button("Cancel")],
                      [sg.Text("*This won't change unless you delete files and reinstall*")]]
    clAmountWindow = sg.Window('ZoomTweaks-PY-v2.0.0-beta.py', clAmountLayout)

    while True:
        if config_file_check(class_amount_file):
            pass
        else:
            break
        event, values = clAmountWindow.read()
        if event == 'Ok':
            print("Dumping input")
            with open(class_amount_file, "a+") as cache:
                json.dump(values, cache)
            clAmountWindow.close()
            return True
        elif event == sg.WIN_CLOSED or event == 'Cancel':
            print("Script cancelled.")
            clAmountWindow.close()
            exit(1)


def class_times_retrieve(layout):
    sg.theme('LightGrey1')
    clTimesWindow = sg.Window('ZoomTweaks-PY-v2.0.0-beta.py', layout)

    while True:
        if config_file_check(class_time_file):
            pass
        else:
            break
        event, values = clTimesWindow.read()
        if event == 'Ok':
            print("Dumping input")
            with open(class_time_file, "a+") as cache:
                json.dump(values, cache)
            clTimesWindow.close()
            return True
        elif event == sg.WIN_CLOSED or event == 'Cancel':
            print("Script cancelled.")
            clTimesWindow.close()
            exit(1)


try:
    cache_check()
    class_amount_retrieve()
    if not config_file_check(class_amount_file):
        with open(class_amount_file, "r") as class_amount:
            class_amount_list = json.load(class_amount)
    print(f'Class amount retrieved: [{class_amount_list["0"]}]')
    clTimesLayout = []
    i = 0
    try:
        for _ in range(int(class_amount_list["0"])):
            i += 1
            clTimesLayout.append([sg.Text(f"Input the starting time of class - {i}:"), sg.InputText()])
    except ValueError as exc:
        print("")
        if class_amount_list["0"] == "":
            print("Your input was blank, please input a number on your next try")
            file_reset(class_amount_file)
        elif not isinstance(class_amount_list["0"], int):
            print("Your input was not a number, please input a number on your next try")
            file_reset(class_amount_file)
        else:
            print("Something went wrong with your input, please try again")
            file_reset(class_amount_file)
        print("-------")
        print(str(exc))
        exit(1)
    clTimesLayout.append([sg.Button("Ok"), sg.Button("Cancel")])
    clTimesLayout.append([sg.Text
                         ("**Please ensure you place 'am' or 'pm' after the time**")])
    class_times_retrieve(clTimesLayout)
    if not config_file_check(class_time_file):
        with open(class_time_file, "r") as class_times:
            class_times_dict = json.load(class_times)
            class_times_list = list(class_times_dict.values())
    print(f'Class times retrieved: [{class_times_list}]')
    updated_times_list = []
    for time in class_times_list:
        if "am" in time.lower():
            time = time.strip(" " + "am")
            updated_times_list.append(time)
        elif "pm" in time.lower():
            time = time.strip(" " + "pm")
            hour = time.split(':')[0]
            minute = time.split(':')[1]
            hour = int(hour)
            hour += 12
            if hour != 24:
                pass
            elif hour == 24:
                hour -= 12
            hour = str(hour)
            time = (hour + ":" + minute)
            updated_times_list.append(time)
        else:
            print("Did not detect 'am' or 'pm' in a time")
            print("Please retry with 'am' or 'pm' in your times")
            file_reset(class_amount_file)
            file_reset(class_time_file)
            exit(1)
except Exception:
    raise
