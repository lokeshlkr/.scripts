; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir% ; Ensures a consistent starting directory.
#NoTrayIcon
#NoEnv
#SingleInstance force

#Include JSON.ahk
FileRead, secrets, %A_ScriptDir%\secrets
credentials := JSON.Load(secrets)

;;editor := "S:\Programs\VSCodium\VSCodium.exe"
editor := "C:\Users\STRANGER\AppData\Local\Programs\Microsoft VS Code\Code.exe"

;; Helper Functions ;;

startApp(name,path){
  Process, Exist, % name,
  if(!ErrorLevel){
    run, % path
  }
  return
}

runWaitOne(command) {
  shell := ComObjCreate("WScript.Shell")
  ; Execute a single command via cmd.exe
  exec := shell.Exec(ComSpec " /C " command)
  ; Read and return the command's output
  return exec.StdOut.ReadAll()
}

;; AutoStarts ;;
; startApp("TrafficMonitor.exe","D:\Stranger\Programs\Files\TrafficMonitor\TrafficMonitor.exe")
MsgBox,,AHK Started, Keybinds are now active., 0.1

:*:eora::
  send,% credentials.ora.e
return
:*:pora::
  send,% credentials.ora.p
return

:*:eepic::
  send,% credentials.epic.e
return
:*:pepic::
  send,% credentials.epic.p
return

:*:ehex::
  send,% credentials.hex.e
return
:*:phex::
  send,% credentials.hex.p
return

#Enter:: ;Win+Enter
  run, wt
  WinWait,PowerShell,, 3
  if (!ErrorLevel){
    ControlClick,,PowerShell
  }
return

#+t::
  run, %A_ScriptDir%\testing.ahk
return

#+k::
  run, %editor% %A_ScriptDir%
return

#+v::
  run, %editor% "S:\Programs\VSCodium\resources\app\out\vs\workbench\workbench.desktop.main.css"

#+r::
  run, %A_ScriptDir%\shelp.ahk
return

#+o::
  run, "C:\Users\STRANGER\AppData\Local\Obsidian\Obsidian.exe"
return

#+d::
  run, %editor%
return
