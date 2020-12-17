# Zoom Tweaks - Main Container

# Standard Libraries
from datetime import datetime
from inspect import currentframe, getframeinfo
from os import system, getcwd
import json
import time as t
# External Libraries
import PySimpleGUI as sg
# Constants
from bin.utils import (class_amount_file, class_time_file,
                       class_link_file, clAmountLayout, clTimesLayout,
                       updated_times_list, clLinksLayout)
# ZoomTweaks-PY Functions
from bin.utils import (file_reset, retriever, config_file_check, cache_check,
                       lfile, proc_init)
from bin.logger import log


try:
    proc_init()
    log.debug("Entering main.py")
    frame_info = getframeinfo(currentframe())
    cache_check()
    retriever(clAmountLayout, class_amount_file)
    if not config_file_check(class_amount_file):
        with open(class_amount_file, "r") as class_amount:
            class_amount_list = json.load(class_amount)
    log.debug(f'Class amount retrieved: [{class_amount_list["0"]}]')
    try:
        i = 0
        for _ in range(int(class_amount_list["0"])):
            i += 1
            clTimesLayout.append([sg.Text(f"Input the starting time of class - {i}:"), sg.InputText()])
        log.debug("Appended starting time inputs to class time layout")
    except ValueError as exc:
        if class_amount_list["0"] == "":
            log.debug("Your input was blank, please input a number on your next try")
            print(f"Check {lfile} for info (debug log)")
            file_reset(class_amount_file)
        elif not isinstance(class_amount_list["0"], int):
            log.debug("Your input was not a number, please input a number on your next try")
            print(f"Check {lfile} for info (debug log)")
            file_reset(class_amount_file)
        else:
            log.debug("Something went wrong with your input, please try again")
            print(f"Check {lfile} for info (debug log)")
            file_reset(class_amount_file)
        log.debug("-------")
        log.debug(str(exc))
        exit(1)
    clTimesLayout.append([sg.Text("Input the time you wish for the script to close:"), sg.InputText()])
    clTimesLayout.append([sg.Button("Ok"), sg.Button("Cancel")])
    clTimesLayout.append([sg.Text
                         ("**Please ensure you place 'am' or 'pm' after the times**")])
    clTimesLayout.append([sg.Text
                         ("**Please also ensure that you use standard time**")])
    log.debug("Finished class time layout setup")
    retriever(clTimesLayout, class_time_file)
    if not config_file_check(class_time_file):
        with open(class_time_file, "r") as class_times:
            class_times_dict = json.load(class_times)
            class_times_list = list(class_times_dict.values())
    log.debug(f'Class times retrieved: [{class_times_list}]')
    log.debug("Parsing times into military time")
    for time in class_times_list:
        if "am" in time.lower():
            time = time.strip(" " + "am")
            hour = time.split(':')[0]
            minute = time.split(':')[1]
            hour = int(hour)
            minute = int(minute)
            if minute == 00:
                minute = 59
                hour -= 1
            elif minute != 00:
                minute -= 1
            if hour < 10:
                hour = f"0{hour}"
            hour = str(hour)
            minute = str(minute)
            time = (hour + ":" + minute)
            updated_times_list.append(time)
        elif "pm" in time.lower():
            time = time.strip(" " + "pm")
            hour = time.split(':')[0]
            minute = time.split(':')[1]
            hour = int(hour)
            minute = int(minute)
            if minute == 00:
                minute = 59
                hour -= 1
            elif minute != 00:
                minute -= 1
            hour += 12
            if hour != 24:
                pass
            elif hour >= 24:
                hour -= 12
            if hour < 10:
                hour = f"0{hour}"
            hour = str(hour)
            minute = str(minute)
            time = (hour + ":" + minute)
            updated_times_list.append(time)
        else:
            log.debug("Did not detect 'am' or 'pm' in a time")
            log.debug("Please retry with 'am' or 'pm' in your times")
            file_reset(class_amount_file)
            file_reset(class_time_file)
            exit(1)
    log.debug("Successfully parsed times into military time")
    try:
        i = 0
        for _ in range(int(class_amount_list["0"])):
            i += 1
            clLinksLayout.append([sg.Text(f"Input the link of class #{i}:"), sg.InputText()])
        log.debug("Appended link inputs to class link layout")
    except Exception as exc:
        log.debug(f"Caught exception at clLinksLayout.append at lineno: {frame_info.lineno}")
        log.debug(str(exc))
        exit(1)
    clLinksLayout.append([sg.Button("Ok"), sg.Button("Cancel")])
    retriever(clLinksLayout, class_link_file)
    if not config_file_check(class_link_file):
        with open(class_link_file, "r") as class_links:
            class_links_dict = json.load(class_links)
            class_links_list = list(class_links_dict.values())
    log.debug(f'Class links retrieved: [{class_links_list}]')
    joiner_dict = {}
    try:
        i = -1
        for link in class_links_list:
            i += 1
            joiner_dict[updated_times_list[i]] = link
        i = len(updated_times_list) - 1
        joiner_dict[updated_times_list[i]] = None
        log.debug("Wrote joiner dictionary")
    except Exception as exc:
        raise
    sg.Popup("Now entering sleep mode...", title="ZoomTweaks-PY-v2.0.0-beta.py",
             auto_close=True, auto_close_duration=5)
    log.debug("Entering zoomtweaks waiter")
    while True:
        now = datetime.now()
        current_time = now.strftime('%H:%M')
        log.debug("Checking times...")
        for key, value in joiner_dict.items():
            log.debug("Checking keys")
            print(key, value)
            print(current_time)
            if key == current_time:
                log.debug("Caught proper time, starting link")
                try:
                    if "https" or "http" not in value:
                        value = f"https://{value}"
                    system(f"CMD /c start {value}")
                    log.debug(f"Attempted to open {value}")
                except Exception as exc:
                    log.debug(f"Caught exception at joiner dictionary waiter at lineno: {frame_info.lineno}")
                    log.debug(str(exc))
                    log.debug("Check console traceback for more info:")
                    print(f"Check {lfile} for more info (debug log)")
                    raise
        if list(joiner_dict.keys())[-1] == current_time:
            log.debug("Script runtime finished, returning to scheduler")
            system(fr"CMD /c python {getcwd()}\scheduler.py")
            exit(0)
        t.sleep(60)
except KeyboardInterrupt:
    log.debug("Exiting due to keyboard interrupt (ctrl + c)...")
    print("Exiting...")
    pass
except Exception as exc:
    system(fr"CMD /c python {getcwd()}\scheduler.py")
    log.debug(str(exc))
    log.debug("Pushing control to scheduler upon exception in main.py")
    log.debug("Check console traceback for more info:")
    raise
