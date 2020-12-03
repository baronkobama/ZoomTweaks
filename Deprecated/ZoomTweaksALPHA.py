# ZoomTweaksBETA - Python Rewrite

import webbrowser as wb
import time as t
import PySimpleGUI as sg
import pickle as p
from datetime import datetime as dt
from pathlib import Path as pt


# Loop to process events, get values of input, and pickle data for later use
def fileCheck(fileName):
    if event == sg.WIN_CLOSED or event == 'Cancel':
        print("Script cancelled.")
        exit(1)
    else:
        print("Values recieved.")
        v = values
        p.dump(v, open(fileName, "wb"))
        if event == 'Ok':
            window.Close()


# Defines the layout of the window
theme = sg.theme('LightGrey1')
# Creates window elements
layout = [[sg.Text("Input the amount of classes you have.")],
          [sg.Text("Input the amount as '6' or '7', etc."),
           sg.InputText()],
          [sg.Button("Ok"), sg.Button("Cancel")],
          [sg.Text
          ("*This won't change unless you delete files and reinstall.*")]]
# Creates the window itself
window = sg.Window('ZoomTweaksBETA.py', layout, no_titlebar=False,
                   grab_anywhere=False)

# Checks if file is already created and gives the current data
ClsAmt = pt("cache/clsamt.p")
if ClsAmt.is_file():
    pass
else:
    event, values = window.read()
    fileCheck(ClsAmt)
    if event == 'Ok':
        print("Response recieved")
        sg.popup_timed("Caching values...", title="ZoomTweaksBETA.py",
                       no_titlebar=True, grab_anywhere=True)

pClsAmt = p.load(open(ClsAmt, "rb"))


def layoutClassTime():
    global layout
    layout =


























# # # # # Class Times Input Frame
if pClsAmt == {0: '1'}:
    layout = [[sg.Text("Input the times that each class starts.")],
              [sg.Text("Input as '7:20' or '13:30', etc.")],
              [sg.Text(("1st"), size=(15, 1)), sg.InputText()],
              [sg.Button("Ok"), sg.Button("Cancel")]]
elif pClsAmt == {0: '2'}:
    layout = [[sg.Text("Input the times that each class starts.")],
              [sg.Text("Input as '7:20' or '13:30', etc.")],
              [sg.Text(("1st"), size=(15, 1)), sg.InputText()],
              [sg.Text(("2nd"), size=(15, 1)), sg.InputText()],
              [sg.Button("Ok"), sg.Button("Cancel")]]
elif pClsAmt == {0: '3'}:
    layout = [[sg.Text("Input the times that each class starts.")],
              [sg.Text("Input as '7:20' or '13:30', etc.")],
              [sg.Text(("1st"), size=(15, 1)), sg.InputText()],
              [sg.Text(("2nd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("3rd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("4th"), size=(15, 1)), sg.InputText()],
              [sg.Button("Ok"), sg.Button("Cancel")]]
elif pClsAmt == {0: '4'}:
    layout = [[sg.Text("Input the times that each class starts.")],
              [sg.Text("Input as '7:20' or '13:30', etc.")],
              [sg.Text(("1st"), size=(15, 1)), sg.InputText()],
              [sg.Text(("2nd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("3rd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("4th"), size=(15, 1)), sg.InputText()],
              [sg.Button("Ok"), sg.Button("Cancel")]]
elif pClsAmt == {0: '5'}:
    layout = [[sg.Text("Input the times that each class starts.")],
              [sg.Text("Input as '7:20' or '13:30', etc.")],
              [sg.Text(("1st"), size=(15, 1)), sg.InputText()],
              [sg.Text(("2nd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("3rd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("4th"), size=(15, 1)), sg.InputText()],
              [sg.Text(("5th"), size=(15, 1)), sg.InputText()],
              [sg.Button("Ok"), sg.Button("Cancel")]]
elif pClsAmt == {0: '6'}:
    layout = [[sg.Text("Input the times that each class starts.")],
              [sg.Text("Input as '7:20' or '13:30', etc.")],
              [sg.Text(("1st"), size=(15, 1)), sg.InputText()],
              [sg.Text(("2nd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("3rd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("4th"), size=(15, 1)), sg.InputText()],
              [sg.Text(("5th"), size=(15, 1)), sg.InputText()],
              [sg.Text(("6th"), size=(15, 1)), sg.InputText()],
              [sg.Button("Ok"), sg.Button("Cancel")]]
elif pClsAmt == {0: '7'}:
    layout = [[sg.Text("Input the times that each class starts.")],
              [sg.Text("Input as '7:20' or '13:30', etc.")],
              [sg.Text(("1st"), size=(15, 1)), sg.InputText()],
              [sg.Text(("2nd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("3rd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("4th"), size=(15, 1)), sg.InputText()],
              [sg.Text(("5th"), size=(15, 1)), sg.InputText()],
              [sg.Text(("6th"), size=(15, 1)), sg.InputText()],
              [sg.Text(("7th"), size=(15, 1)), sg.InputText()],
              [sg.Button("Ok"), sg.Button("Cancel")]]
elif pClsAmt == {0: '8'}:
    layout = [[sg.Text("Input the times that each class starts.")],
              [sg.Text("Input as '7:20' or '13:30', etc.")],
              [sg.Text(("1st"), size=(15, 1)), sg.InputText()],
              [sg.Text(("2nd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("3rd"), size=(15, 1)), sg.InputText()],
              [sg.Text(("4th"), size=(15, 1)), sg.InputText()],
              [sg.Text(("5th"), size=(15, 1)), sg.InputText()],
              [sg.Text(("6th"), size=(15, 1)), sg.InputText()],
              [sg.Text(("7th"), size=(15, 1)), sg.InputText()],
              [sg.Text(("8th"), size=(15, 1)), sg.InputText()],
              [sg.Button("Ok"), sg.Button("Cancel")]]
else:
    print("Value either too high (higher than 8), blank, or not num value")

window = sg.Window('ZoomTweaksBETA.py', layout, no_titlebar=False,
                   grab_anywhere=False)

ClsTimes = pt("cache/clstimes.p")
if ClsTimes.is_file():
    pass
else:
    event, values = window.read()
    fileCheck(ClsTimes)
    if event == 'Ok':
        print("'Ok' response recieved")

pClsTimes = p.load(open(ClsTimes, "rb"))


def zoomJoiner():
    with open('cache/clstimes.p') as rClsTimes:
        if '7' in rClsTimes.read():
            print("POGGERS MOMENT HOLY SHIT")
        else:
            print("yeah no")
            print(pClsTimes)


zoomJoiner()
exit(0)
# (dt.now().strftime('%H:%M'))
if ClsAmt.is_file():
    if ClsTimes.is_file():
        print("===========")
        print("===========")
        print("===========")
        print("***DEBUGGING PURPOSES ONLY***")
        print("Loaded Classes -------")
        print(pt)
        print(dt)
        print("Loaded Modules -------")
        print(wb)
        print(t)
        print(sg)
        print(p)
        print("Cached File Paths ----")
        print(ClsAmt)
        print(ClsTimes)
        print("Cached Values --------")
        print(pClsAmt)
        print(pClsTimes)
        print("===========")
        print("===========")
        print("===========")
    else:
        pass
else:
    pass

exit(0)
