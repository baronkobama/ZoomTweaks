strUser = CreateObject("WScript.Network").UserName

UserInput = InputBox( "Enter your 1st Period Zoom Link" )
strInput1 = UserInput

UserInput = InputBox( "Enter your 2nd Period Zoom Link" )
strInput2 = UserInput

UserInput = InputBox( "Enter your 3rd Period Zoom Link" )
strInput3 = UserInput

UserInput = InputBox( "Enter your 4th Period Zoom Link" )
strInput4 = UserInput

UserInput = InputBox( "Enter your 5th Period Zoom Link" )
strInput5 = UserInput

UserInput = InputBox( "Enter your 6th Period Zoom Link" )
strInput6 = UserInput

UserInput = InputBox( "Enter your 7th Period Zoom Link" )
strInput7 = UserInput

Const TIMEOUT = 3
Const POPUP_TITLE = "ZoomTweaksBETAV1"

dim filesys, filetxt
Set filesys = CreateObject("Scripting.FileSystemObject")
Set filetxt = filesys.OpenTextFile("C:\ZoomScripts\Classes\FirstPD.vbs", 8, True)
filetxt.WriteLine("Const TIMEOUT = 3")
filetxt.WriteLine("Const POPUP_TITLE = """ & "ZoomTweaksBETAV1" & """")
filetxt.WriteLine("URL1 = """ & strInput1 & """")
filetxt.WriteBlankLines(1)

Set filetxt = filesys.OpenTextFile("C:\ZoomScripts\Classes\SecondPD.vbs", 8, True)
filetxt.WriteLine("Const TIMEOUT = 3")
filetxt.WriteLine("Const POPUP_TITLE = """ & "ZoomTweaksBETAV1" & """")
filetxt.WriteLine("URL2 = """ & strInput2 & """")
filetxt.WriteBlankLines(1)

Set filetxt = filesys.OpenTextFile("C:\ZoomScripts\Classes\ThirdPD.vbs", 8, True)
filetxt.WriteLine("Const TIMEOUT = 3")
filetxt.WriteLine("Const POPUP_TITLE = """ & "ZoomTweaksBETAV1" & """")
filetxt.WriteLine("URL3 = """ & strInput3 & """")
filetxt.WriteBlankLines(1)

Set filetxt = filesys.OpenTextFile("C:\ZoomScripts\Classes\FourthPD.vbs", 8, True)
filetxt.WriteLine("Const TIMEOUT = 3")
filetxt.WriteLine("Const POPUP_TITLE = """ & "ZoomTweaksBETAV1" & """")
filetxt.WriteLine("URL4 = """ & strInput4 & """")
filetxt.WriteBlankLines(1)

Set filetxt = filesys.OpenTextFile("C:\ZoomScripts\Classes\FifthPD.vbs", 8, True)
filetxt.WriteLine("Const TIMEOUT = 3")
filetxt.WriteLine("Const POPUP_TITLE = """ & "ZoomTweaksBETAV1" & """")
filetxt.WriteLine("URL5 = """ & strInput5 & """")
filetxt.WriteBlankLines(1)

Set filetxt = filesys.OpenTextFile("C:\ZoomScripts\Classes\SixthPD.vbs", 8, True)
filetxt.WriteLine("Const TIMEOUT = 3")
filetxt.WriteLine("Const POPUP_TITLE = """ & "ZoomTweaksBETAV1" & """")
filetxt.WriteLine("URL6 = """ & strInput6 & """")
filetxt.WriteBlankLines(1)

Set filetxt = filesys.OpenTextFile("C:\ZoomScripts\Classes\SeventhPD.vbs", 8, True)
filetxt.WriteLine("Const TIMEOUT = 3")
filetxt.WriteLine("Const POPUP_TITLE = """ & "ZoomTweaksBETAV1" & """")
filetxt.WriteLine("URL7 = """ & strInput7 & """")
filetxt.WriteBlankLines(1)

Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Popup "Returning to Setup...", TIMEOUT, POPUP_TITLE

Dim currDir, oShell
Set fso = CreateObject("Scripting.FileSystemObject")
currDir = fso.GetParentFolderName(WScript.ScriptFullName)
Set oShell = WScript.CreateObject("WScript.Shell")
oShell.run "CMD /C start "& currDir &"\ContinuedInstaller.bat"
Set oShell = Nothing
