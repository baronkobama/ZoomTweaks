# Zoom Tweaks BETA - Python Rewrite

# Standard Libraries
from os import mkdir, getcwd, path
import json
# External Libraries
import PySimpleGUI as sg

print(mkdir)
print(getcwd)
print(path)
print(json)
print(sg)

cache_directory = path.join(getcwd(), "cache")
class_amount_file = path.join(cache_directory, "classAmount.json")


def cache_check():
    if not path.isdir(cache_directory):
        print("No cache directory, making dir")
        mkdir(cache_directory)
        with open(class_amount_file, "w+") as f:
            print("No class amount file, writing file")
            f.close()
            print("Directory and class amount file written")
        return True
    elif path.isdir(cache_directory):
        print("Cache directory detected")
        if not path.isfile(class_amount_file):
            print("No class amount file, writing file")
            with open(class_amount_file, "w+") as f:
                f.close()
                print("Class amount file written")
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
    layout = [[sg.Text("Input the amount of classes you have.")],
              [sg.Text("Input the amount as '5' or '6', etc."),
               sg.InputText()],
              [sg.Button("Ok"), sg.Button("Cancel")],
              [sg.Text
              ("*This won't change unless you delete files and reinstall*")]]
    window = sg.Window('ZoomTweaksBETA.py', layout)

    while True:
        if config_file_check(class_amount_file):
            pass
        else:
            break
        event, values = window.read()
        if event == 'Ok':
            print("Dumping input")
            with open(class_amount_file, "a+") as cache:
                json.dump(values, cache)
            window.close()
            return True
        elif event == sg.WIN_CLOSED or event == 'Cancel':
            print("Script cancelled.")
            window.close()
            exit(1)


try:
    cache_check()
    class_amount_retrieve()
    if not config_file_check(class_amount_file):
        with open(class_amount_file, "r") as class_amount:
            class_file = json.load(class_amount)
    print(f'Class amount retrieved: [{class_file["0"]}]')
except Exception:
    raise

# with open(clsAmt, newline='') as outfile:
#     reader = csv.reader(outfile)
#     for row in reader:
#         print(row)
