@echo off

REM ### Administrator Permission Prompt for Continuation
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
 
REM ### Creating Background Process
 echo.>"C:\ZoomScripts\BackgroundScript\BackgroundProcess.bat"
Set "out=C:\ZoomScripts\BackgroundScript"
 >> "%out%\BackgroundProcess.bat" Echo;@echo off
 >> "%out%\BackgroundProcess.bat" Echo;
 >> "%out%\BackgroundProcess.bat" Echo;:TL
 >> "%out%\BackgroundProcess.bat" Echo;set hour=%%time:~0,2%%
 >> "%out%\BackgroundProcess.bat" Echo;set min=%%time:~3,2%%
 >> "%out%\BackgroundProcess.bat" Echo;set datetimef= %%hour%%:%%min%%
 >> "%out%\BackgroundProcess.bat" Echo;
 >> "%out%\BackgroundProcess.bat" Echo;if %%datetimef%%==7:19 start C:\ZoomScripts\Classes\FirstPD.vbs
 >> "%out%\BackgroundProcess.bat" Echo;if %%datetimef%%==8:17 start C:\ZoomScripts\Classes\SecondPD.vbs
 >> "%out%\BackgroundProcess.bat" Echo;if %%datetimef%%==9:20 start C:\ZoomScripts\Classes\ThirdPD.vbs
 >> "%out%\BackgroundProcess.bat" Echo;if %%datetimef%%==10:48 start C:\ZoomScripts\Classes\FourthPD.vbs
 >> "%out%\BackgroundProcess.bat" Echo;if %%datetimef%%==11:47 start C:\ZoomScripts\Classes\FifthPD.vbs
 >> "%out%\BackgroundProcess.bat" Echo;if %%datetimef%%==12:58 start C:\ZoomScripts\Classes\SixthPD.vbs
 >> "%out%\BackgroundProcess.bat" Echo;if %%datetimef%%==13:56 start C:\ZoomScripts\Classes\SeventhPD.vbs
 >> "%out%\BackgroundProcess.bat" Echo;if %%datetimef%%==14:00 exit
 >> "%out%\BackgroundProcess.bat" Echo;timeout /t 60
 >> "%out%\BackgroundProcess.bat" Echo;goto TL
 
REM ### Background Script
 echo.>"C:\ZoomScripts\BackgroundScript\BackgroundProcess.vbs"
Set "out=C:\ZoomScripts\BackgroundScript"
 >> "%out%\BackgroundProcess.vbs" Echo;Set oShell = CreateObject ("Wscript.Shell") 
 >> "%out%\BackgroundProcess.vbs" Echo;Dim strArgs
 >> "%out%\BackgroundProcess.vbs" Echo;strArgs = "cmd /c C:\ZoomScripts\BackgroundScript\BackgroundProcess.bat"
 >> "%out%\BackgroundProcess.vbs" Echo;oShell.Run strArgs, 0, false

REM ### First Period 
Set "out=C:\ZoomScripts\Classes"
 >> "%out%\FirstPD.vbs" Echo;result = MsgBox ("Do you want to join first period?", vbYesNo, "First Period Zoom")
 >> "%out%\FirstPD.vbs" Echo;
 >> "%out%\FirstPD.vbs" Echo;Select Case result
 >> "%out%\FirstPD.vbs" Echo;Case vbYes
 >> "%out%\FirstPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\FirstPD.vbs" Echo;	objShell.Popup "Joining...", TIMEOUT, POPUP_TITLE
 >> "%out%\FirstPD.vbs" Echo;	Dim URL,WshShell,i
 >> "%out%\FirstPD.vbs" Echo;	URL = URL1
 >> "%out%\FirstPD.vbs" Echo;	Set WshShell = CreateObject("WScript.shell")
 >> "%out%\FirstPD.vbs" Echo;	For i = 0 to 50
 >> "%out%\FirstPD.vbs" Echo;		WshShell.SendKeys(chr(175))
 >> "%out%\FirstPD.vbs" Echo;	Next
<<<<<<< HEAD
 >> "%out%\FirstPD.vbs" Echo;	WshShell.run "CMD /C start opera.exe " ^& URL ^&"",0,False
=======
 >> "%out%\FirstPD.vbs" Echo;	WshShell.run "CMD /C start " ^& URL ^&"",0,False
>>>>>>> testing
 >> "%out%\FirstPD.vbs" Echo;Case vbNo
 >> "%out%\FirstPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\FirstPD.vbs" Echo;	objShell.Popup "Cancelled... returning to background.", TIMEOUT, POPUP_TITLE
 >> "%out%\FirstPD.vbs" Echo;End Select
 
REM ### Second Period
Set "out=C:\ZoomScripts\Classes"
 >> "%out%\SecondPD.vbs" Echo;result = MsgBox ("Do you want to join Second period?", vbYesNo, "Second Period Zoom")
 >> "%out%\SecondPD.vbs" Echo;
 >> "%out%\SecondPD.vbs" Echo;Select Case result
 >> "%out%\SecondPD.vbs" Echo;Case vbYes
 >> "%out%\SecondPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\SecondPD.vbs" Echo;	objShell.Popup "Joining...", TIMEOUT, POPUP_TITLE
 >> "%out%\SecondPD.vbs" Echo;	Dim URL,WshShell,i
 >> "%out%\SecondPD.vbs" Echo;	URL = URL2
 >> "%out%\SecondPD.vbs" Echo;	Set WshShell = CreateObject("WScript.shell")
 >> "%out%\SecondPD.vbs" Echo;	For i = 0 to 50
 >> "%out%\SecondPD.vbs" Echo;		WshShell.SendKeys(chr(175))
 >> "%out%\SecondPD.vbs" Echo;	Next
<<<<<<< HEAD
 >> "%out%\SecondPD.vbs" Echo;	WshShell.run "CMD /C start opera.exe " ^& URL ^&"",0,False
=======
 >> "%out%\SecondPD.vbs" Echo;	WshShell.run "CMD /C start " ^& URL ^&"",0,False
>>>>>>> testing
 >> "%out%\SecondPD.vbs" Echo;Case vbNo
 >> "%out%\SecondPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\SecondPD.vbs" Echo;	objShell.Popup "Cancelled... returning to background.", TIMEOUT, POPUP_TITLE
 >> "%out%\SecondPD.vbs" Echo;End Select
 
REM ### Third Period
Set "out=C:\ZoomScripts\Classes"
 >> "%out%\ThirdPD.vbs" Echo;result = MsgBox ("Do you want to join Third period?", vbYesNo, "Third Period Zoom")
 >> "%out%\ThirdPD.vbs" Echo;
 >> "%out%\ThirdPD.vbs" Echo;Select Case result
 >> "%out%\ThirdPD.vbs" Echo;Case vbYes
 >> "%out%\ThirdPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\ThirdPD.vbs" Echo;	objShell.Popup "Joining...", TIMEOUT, POPUP_TITLE
 >> "%out%\ThirdPD.vbs" Echo;	Dim URL,WshShell,i
 >> "%out%\ThirdPD.vbs" Echo;	URL = URL3
 >> "%out%\ThirdPD.vbs" Echo;	Set WshShell = CreateObject("WScript.shell")
 >> "%out%\ThirdPD.vbs" Echo;	For i = 0 to 50
 >> "%out%\ThirdPD.vbs" Echo;		WshShell.SendKeys(chr(175))
 >> "%out%\ThirdPD.vbs" Echo;	Next
<<<<<<< HEAD
 >> "%out%\ThirdPD.vbs" Echo;	WshShell.run "CMD /C start opera.exe " ^& URL ^&"",0,False
=======
 >> "%out%\ThirdPD.vbs" Echo;	WshShell.run "CMD /C start " ^& URL ^&"",0,False
>>>>>>> testing
 >> "%out%\ThirdPD.vbs" Echo;Case vbNo
 >> "%out%\ThirdPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\ThirdPD.vbs" Echo;	objShell.Popup "Cancelled... returning to background.", TIMEOUT, POPUP_TITLE
 >> "%out%\ThirdPD.vbs" Echo;End Select

REM ### Fourth Period
Set "out=C:\ZoomScripts\Classes"
 >> "%out%\FourthPD.vbs" Echo;result = MsgBox ("Do you want to join Fourth period?", vbYesNo, "Fourth Period Zoom")
 >> "%out%\FourthPD.vbs" Echo;
 >> "%out%\FourthPD.vbs" Echo;Select Case result
 >> "%out%\FourthPD.vbs" Echo;Case vbYes
 >> "%out%\FourthPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\FourthPD.vbs" Echo;	objShell.Popup "Joining...", TIMEOUT, POPUP_TITLE
 >> "%out%\FourthPD.vbs" Echo;	Dim URL,WshShell,i
 >> "%out%\FourthPD.vbs" Echo;	URL = URL4
 >> "%out%\FourthPD.vbs" Echo;	Set WshShell = CreateObject("WScript.shell")
 >> "%out%\FourthPD.vbs" Echo;	For i = 0 to 50
 >> "%out%\FourthPD.vbs" Echo;		WshShell.SendKeys(chr(175))
 >> "%out%\FourthPD.vbs" Echo;	Next
<<<<<<< HEAD
 >> "%out%\FourthPD.vbs" Echo;	WshShell.run "CMD /C start opera.exe " ^& URL ^&"",0,False
=======
 >> "%out%\FourthPD.vbs" Echo;	WshShell.run "CMD /C start " ^& URL ^&"",0,False
>>>>>>> testing
 >> "%out%\FourthPD.vbs" Echo;Case vbNo
 >> "%out%\FourthPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\FourthPD.vbs" Echo;	objShell.Popup "Cancelled... returning to background.", TIMEOUT, POPUP_TITLE
 >> "%out%\FourthPD.vbs" Echo;End Select

REM ### Fifth Period
Set "out=C:\ZoomScripts\Classes"
 >> "%out%\FifthPD.vbs" Echo;result = MsgBox ("Do you want to join Fifth period?", vbYesNo, "Fifth Period Zoom")
 >> "%out%\FifthPD.vbs" Echo;
 >> "%out%\FifthPD.vbs" Echo;Select Case result
 >> "%out%\FifthPD.vbs" Echo;Case vbYes
 >> "%out%\FifthPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\FifthPD.vbs" Echo;	objShell.Popup "Joining...", TIMEOUT, POPUP_TITLE
 >> "%out%\FifthPD.vbs" Echo;	Dim URL,WshShell,i
 >> "%out%\FifthPD.vbs" Echo;	URL = URL5
 >> "%out%\FifthPD.vbs" Echo;	Set WshShell = CreateObject("WScript.shell")
 >> "%out%\FifthPD.vbs" Echo;	For i = 0 to 50
 >> "%out%\FifthPD.vbs" Echo;		WshShell.SendKeys(chr(175))
 >> "%out%\FifthPD.vbs" Echo;	Next
<<<<<<< HEAD
 >> "%out%\FifthPD.vbs" Echo;	WshShell.run "CMD /C start opera.exe " ^& URL ^&"",0,False
=======
 >> "%out%\FifthPD.vbs" Echo;	WshShell.run "CMD /C start " ^& URL ^&"",0,False
>>>>>>> testing
 >> "%out%\FifthPD.vbs" Echo;Case vbNo
 >> "%out%\FifthPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\FifthPD.vbs" Echo;	objShell.Popup "Cancelled... returning to background.", TIMEOUT, POPUP_TITLE
 >> "%out%\FifthPD.vbs" Echo;End Select

REM ### Sixth Period
Set "out=C:\ZoomScripts\Classes"
 >> "%out%\SixthPD.vbs" Echo;result = MsgBox ("Do you want to join Sixth period?", vbYesNo, "Sixth Period Zoom")
 >> "%out%\SixthPD.vbs" Echo;
 >> "%out%\SixthPD.vbs" Echo;Select Case result
 >> "%out%\SixthPD.vbs" Echo;Case vbYes
 >> "%out%\SixthPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\SixthPD.vbs" Echo;	objShell.Popup "Joining...", TIMEOUT, POPUP_TITLE
 >> "%out%\SixthPD.vbs" Echo;	Dim URL,WshShell,i
 >> "%out%\SixthPD.vbs" Echo;	URL = URL6
 >> "%out%\SixthPD.vbs" Echo;	Set WshShell = CreateObject("WScript.shell")
 >> "%out%\SixthPD.vbs" Echo;	For i = 0 to 50
 >> "%out%\SixthPD.vbs" Echo;		WshShell.SendKeys(chr(175))
 >> "%out%\SixthPD.vbs" Echo;	Next
<<<<<<< HEAD
 >> "%out%\SixthPD.vbs" Echo;	WshShell.run "CMD /C start opera.exe " ^& URL ^&"",0,False
=======
 >> "%out%\SixthPD.vbs" Echo;	WshShell.run "CMD /C start " ^& URL ^&"",0,False
>>>>>>> testing
 >> "%out%\SixthPD.vbs" Echo;Case vbNo
 >> "%out%\SixthPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\SixthPD.vbs" Echo;	objShell.Popup "Cancelled... returning to background.", TIMEOUT, POPUP_TITLE
 >> "%out%\SixthPD.vbs" Echo;End Select

REM ### Seventh Period
Set "out=C:\ZoomScripts\Classes"
 >> "%out%\SeventhPD.vbs" Echo;result = MsgBox ("Do you want to join Seventh period?", vbYesNo, "Seventh Period Zoom")
 >> "%out%\SeventhPD.vbs" Echo;
 >> "%out%\SeventhPD.vbs" Echo;Select Case result
 >> "%out%\SeventhPD.vbs" Echo;Case vbYes
 >> "%out%\SeventhPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\SeventhPD.vbs" Echo;	objShell.Popup "Joining...", TIMEOUT, POPUP_TITLE
 >> "%out%\SeventhPD.vbs" Echo;	Dim URL,WshShell,i
 >> "%out%\SeventhPD.vbs" Echo;	URL = URL7
 >> "%out%\SeventhPD.vbs" Echo;	Set WshShell = CreateObject("WScript.shell")
 >> "%out%\SeventhPD.vbs" Echo;	For i = 0 to 50
 >> "%out%\SeventhPD.vbs" Echo;		WshShell.SendKeys(chr(175))
 >> "%out%\SeventhPD.vbs" Echo;	Next
<<<<<<< HEAD
 >> "%out%\SeventhPD.vbs" Echo;	WshShell.run "CMD /C start opera.exe " ^& URL ^&"",0,False
=======
 >> "%out%\SeventhPD.vbs" Echo;	WshShell.run "CMD /C start " ^& URL ^&"",0,False
>>>>>>> testing
 >> "%out%\SeventhPD.vbs" Echo;Case vbNo
 >> "%out%\SeventhPD.vbs" Echo;	Set objShell = WScript.CreateObject("WScript.Shell")
 >> "%out%\SeventhPD.vbs" Echo;	objShell.Popup "Cancelled... returning to background.", TIMEOUT, POPUP_TITLE
 >> "%out%\SeventhPD.vbs" Echo;End Select
 
REM ### Scheduling Background Registry Process
SchTasks /Create /F /RL HIGHEST /SC DAILY /ST 07:18 /TN "ZoomAutojoiner" /TR "C:\ZoomScripts\BackgroundScript\BackgroundProcess.vbs" >nul

goto Finished

:Finished
echo Setup finished!
timeout /t 5 >NUL
<<<<<<< HEAD
if exist "C:\ZoomScripts\BackgroundScript\BackgroundProcess.vbs" (taskkill /F /IM cmd.exe /T) else exit
=======
if exist "C:\ZoomScripts\BackgroundScript\BackgroundProcess.vbs" (taskkill /F /IM cmd.exe /T) else exit
>>>>>>> testing
