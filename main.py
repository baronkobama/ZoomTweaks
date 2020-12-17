# Zoom Tweaks - Main Container

# Standard Libraries
from os import system, getcwd
import json
import time as t
# External Libraries
import PySimpleGUI as sg
# Constants
from bin.utils import (class_amount_file, class_time_file,
                       class_link_file, clAmountLayout, clTimesLayout,
                       updated_times_list, clLinksLayout, current_time)
# ZoomTweaks-PY Functions
from bin.utils import (file_reset, retriever, config_file_check, cache_check)


try:
    cache_check()
    retriever(clAmountLayout, class_amount_file)
    if not config_file_check(class_amount_file):
        with open(class_amount_file, "r") as class_amount:
            class_amount_list = json.load(class_amount)
    print(f'Class amount retrieved: [{class_amount_list["0"]}]')
    try:
        i = 0
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
    clTimesLayout.append([sg.Text("Input the time you wish for the script to close:"), sg.InputText()])
    clTimesLayout.append([sg.Button("Ok"), sg.Button("Cancel")])
    clTimesLayout.append([sg.Text
                         ("**Please ensure you place 'am' or 'pm' after the times**")])
    clTimesLayout.append([sg.Text
                         ("**Please also ensure that you use standard time**")])
    retriever(clTimesLayout, class_time_file)
    if not config_file_check(class_time_file):
        with open(class_time_file, "r") as class_times:
            class_times_dict = json.load(class_times)
            class_times_list = list(class_times_dict.values())
    print(f'Class times retrieved: [{class_times_list}]')
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
            elif hour >= 24:
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
    try:
        i = 0
        for _ in range(int(class_amount_list["0"])):
            i += 1
            clLinksLayout.append([sg.Text(f"Input the link of class #{i}:"), sg.InputText()])
    except Exception as exc:
        print(exc)
    clLinksLayout.append([sg.Button("Ok"), sg.Button("Cancel")])
    retriever(clLinksLayout, class_link_file)
    if not config_file_check(class_link_file):
        with open(class_link_file, "r") as class_links:
            class_links_dict = json.load(class_links)
            class_links_list = list(class_links_dict.values())
    print(f'Class links retrieved: [{class_links_list}]')
    joiner_dict = {}
    try:
        i = -1
        for link in class_links_list:
            i += 1
            joiner_dict[updated_times_list[i]] = link
        i = len(updated_times_list) - 1
        joiner_dict[updated_times_list[i]] = None
    except Exception as exc:
        raise
    print(joiner_dict)
    sg.Popup("Now entering sleep mode...", title="ZoomTweaks-PY-v2.0.0-beta.py",
             auto_close=True, auto_close_duration=5)
    while True:
        for key, value in joiner_dict.items():
            if key == current_time:
                try:
                    if "https" or "http" not in value:
                        value = f"https://{value}"
                    system(f"CMD /c start {value}")
                except Exception as exc:
                    print(str(exc))
                    raise
        if list(joiner_dict.keys())[-1] == current_time:
            print("Script runtime finished, returning to scheduler!")
            system(fr"CMD /c python {getcwd()}\scheduler.py")
            exit(0)
        t.sleep(60)
except KeyboardInterrupt:
    pass
except Exception:
    system(fr"CMD /c python {getcwd()}\scheduler.py")
    raise
