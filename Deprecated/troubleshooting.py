# ZoomTweaksBETA - Python Rewrite

import time as t
import PySimpleGUI as sg


# Layout function
def psgLayoutArgs(wtd, amttxt, b1, b2):
    [[sg.Text(wtd)],
     [sg.Text(amttxt),
     sg.InputText()],
     [sg.Button(b1), sg.Button(b2)]]


# Defines the color theme of the window
theme = sg.theme('LightGrey1')

# Creates window elements
# layout = [[sg.Text("Input your amount of classes.")],
#          [sg.Text("Input the amount as '6' or '7', etc."),
#           sg.InputText()],
#          [sg.Button("Ok"), sg.Button("Cancel")]]

layout = psgLayoutArgs("Input", "6", "Ok", "Cancel")

# Creates the window itself
window = sg.Window('ZoomTweaksBETA.py', layout, no_titlebar=True,
                   grab_anywhere=False)

t.sleep(.1)

event, values = window.read()
