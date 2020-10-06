@echo off

if exist C:\ZoomScripts (start %~dp0\AZJ_data\ContinuedInstaller.bat) else goto Setup

:Setup
REM ### Administrator Permission Prompt
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)

REM ### Making Directories
md C:\ZoomScripts
md C:\ZoomScripts\Setup
md C:\ZoomScripts\Classes
md C:\ZoomScripts\BackgroundScript

REM ### Making Necessary Files
 echo.>"C:\ZoomScripts\Classes\FirstPD.vbs"
 echo.>"C:\ZoomScripts\Classes\SecondPD.vbs"
 echo.>"C:\ZoomScripts\Classes\ThirdPD.vbs"
 echo.>"C:\ZoomScripts\Classes\FourthPD.vbs"
 echo.>"C:\ZoomScripts\Classes\FifthPD.vbs"
 echo.>"C:\ZoomScripts\Classes\SixthPD.vbs"
 echo.>"C:\ZoomScripts\Classes\SeventhPD.vbs"

REM ### Entering Registerer Script
wscript "%~dp0..\AutoZoomJoiner\AZJ_data\InputRegister.vbs"
exit
