# Zoom Tweaks BETA - Constants Container

# Standard Libraries
from os import getcwd, path
from datetime import datetime
# External Libraries
import PySimpleGUI as sg

# # # ZoomTweaks-PY Main File Constants
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

# # # Scheduler File Constants
scheduler_config_file = path.join(cache_directory, "schedulerConfig.json")
reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
dir_path = path.dirname(path.realpath(__file__))
py_name = "scheduler.py"
address = path.join(dir_path, py_name)
