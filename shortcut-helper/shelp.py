#! /usr/bin/python

import sys,os,ast,subprocess
import datetime
from time import sleep
from enum import Enum
#################### SETUP #####################

class Level(Enum):
    TERMINAL = 0
    NOTIFICATION = 1
    BOTH = 2

colors = {
    "style" : {
        'reset' : '\033[0m',
        'bold' : '\033[01m',
        'disable' : '\033[02m',
        'underline' : '\033[04m',
        'reverse' : '\033[07m',
        'strikethrough' : '\033[09m',
        'invisible' : '\033[08m',
    },
    "fg" : {
        'black' : '\033[30m',
        'red' : '\033[31m',
        'green' : '\033[32m',
        'orange' : '\033[33m',
        'blue' : '\033[34m',
        'purple' : '\033[35m',
        'cyan' : '\033[36m',
        'lightgrey' : '\033[37m',
        'darkgrey' : '\033[90m',
        'lightred' : '\033[91m',
        'lightgreen' : '\033[92m',
        'yellow' : '\033[93m',
        'lightblue' : '\033[94m',
        'pink' : '\033[95m',
        'lightcyan' : '\033[96m',
    },
    "bg" : {
        'black' : '\033[40m',
        'red' : '\033[41m',
        'green' : '\033[42m',
        'orange' : '\033[43m',
        'blue' : '\033[44m',
        'purple' : '\033[45m',
        'cyan' : '\033[46m',
        'lightgrey' : '\033[47m',
    }
}
editor = "codium"
browser = "firefox"
terminal = "alacritty"
home = os.path.expanduser("~")
commands={
    'help':'Show this help message',
    'search':f'Search a text in {browser} in duckduckgo',
    'browse':f'Browse any URL in {browser}',
    'sync':'Push a git repository to origin',
    'panel':'Run a panel script',
    'rust':f'Open rust practice project in {editor}',
    'rustnew':f'Create new rust project and open in {editor}',
    'edit':f'Open some basic locations in {editor}',
    'restart':'Restart any program',
    'gui':'show dialog box to capture a command',
    'iresize':'Resizes image to given size'
}
paths = {
    'home' : home,
    'rust' : f'{home}/working_folder/rust/practice',
    'self' : f'{home}/working_folder/.scripts',
    ''     : f'{home}/working_folder/.scripts',
}
mappings = {
    't':terminal,
    'terminal':terminal,
    'b':browser,
    'browser':browser,
}

filename = sys.argv[0]
command = rest = ""


def run(command):
    return os.system(command) == 0

def execute(command):
    x = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return x.communicate()

def notify(text,fg="",bg="",style="",end="\n", level=Level.TERMINAL):
    if notify in (Level.TERMINAL,Level.BOTH):
        fg = colors["fg"].get(fg.lower(),"")
        bg = colors["bg"].get(bg.lower(),"")
        style = colors["style"].get(style.lower(),"")
        reset = colors["style"]['reset']
        formatted_mesasge = f"{fg}{style}{bg}{text}{reset}"
        print(formatted_mesasge,end=end)
    if level in (Level.NOTIFICATION,Level.BOTH): 
        timeout = "-t 0" if len(text) > 100 else ""
        run(f'notify-send ShortcutHelper "<span font-family=\'Stranger Nerd Font Mono\'>{text}</span>" -i keyboard {timeout}')

def is_git_repo(path):
    if path == '.':
        path = os.getcwd()
    cwd = path.split('/')[1:]
    isGitRepo = False
    l = len(cwd)
    for i in range(l):
        path = '/' + '/'.join(cwd[:l-i])
        dirs = os.listdir(path)
        if '.git' in dirs:
            return path

def help():
    notify("\nAvailable Commands:",fg="blue")
    text = "Available Commands:\n"
    for command in commands:
        text += "○ "+command.ljust(10," ")
        text += "- "+commands[command] + "\n"
        notify("○ "+command.ljust(10," "),style="bold",end="")
        notify("- "+commands[command])
    notify(text,level=Level.NOTIFICATION)
    print()

def search():
    command = f'{browser} "https://duckduckgo.com/?q={rest}" 2>/dev/null &'
    run(command)

def browse():
    url = 'https://' + (rest if "." in rest else rest + ".com")
    command = f'{browser} "{url}" 2>/dev/null &'
    run(command) 

def sync():
    path = paths.get(rest,rest)
    path = os.path.normpath(path)
    if not os.path.exists(path):
        notify(f"'{path}' Not a valid path",fg="red",style="bold", level=Level.BOTH)
        return
    git_path = is_git_repo(path)
    if git_path != None:
        os.chdir(git_path)
        command = f'git add --all && git commit -m "autosync" && git push origin master'
        if run(command):
            notify(f"'{git_path}' Synced Successfully!",fg="green",style="bold", level=Level.BOTH)
        else:
            notify(f"'{git_path}' Some error occured!",fg="red",style="bold", level=Level.BOTH)
    else:
        notify("Not a git repo!",fg="red",style="bold", level=Level.BOTH) 

def panel():
    file = f'{home}/working_folder/.scripts/panel/{rest}'
    run(file)

def openineditor(path):
    if os.path.exists(path):
        run(f'{editor} {path}')
        return True
    return False

def rustnew():
    os.chdir(f'{paths["rust"]}/..')
    run('mv practice "practice_$(date +%Y%m%d_%H%M%S)"')
    run('cargo new practice')
    if not openineditor(paths['rust']):
        notify("Something went wrong, new practice project could not be created.",fg="red",style="bold",level=Level.BOTH)

def rust():
    if not openineditor(paths['rust']):
        rustnew()

def edit():
    path = paths.get(rest.strip(),None)
    if path:
        openineditor(path)
    else:
        notify(f"Folder name '{rest}' not configured",fg="orange",style="bold",level=Level.BOTH)

def restart():
    if len(rest.strip()) == 0:
        notify("Provide a program to restart.",fg="red")
    else:
        r=0
        x = run(f'killall {rest}')
        if(not x):
            r = run(f'{rest} &')
        else:
            sleep(0.5)
            r = run(f'{rest} &')
        if r:
            notify(f"'{rest}' restarted!", level=Level.BOTH)
        else:
            notify(f"'{rest}' failed to start!", level=Level.BOTH)

def iresize():
    path = os.path.normpath(rest)
    if rest.strip() and os.path.isfile(path) and not os.path.islink(path):
        (stdout, stderr) = execute("zenity --entry --text='Enter new size as widthxheight:'")
        size = str(stdout)[2:-3].strip() # slicing to get rid of quotes and new line character
        ext = path.split(".")[-1]
        oldname = f'{rest[:-(len(ext)+1)]}_{datetime.datetime.now().strftime("%Y%m%dT%H%M%S")}.{ext}'
        newname = path
        if not run(f'cp {path} {oldname}'):
            notify(f"Error in backing up, Resizing with new name!",fg="red",style="bold",level=Level.BOTH)
            newname = path+size
        if run(f'convert {path} -resize {size} {newname}'):
            notify(f"Resize completed!",fg="green",style="bold",level=Level.BOTH)
        else:
            notify(f"Some error occured while resizing!",fg="red",style="bold",level=Level.BOTH)

    else:
        notify(f"'{rest}' Invalid file path!",fg="red",style="bold",level=Level.BOTH)

def gui():
    run('killall zenity')
    (stdout, stderr) = execute("zenity --entry --text='Enter a shelp command:'")
    command = str(stdout)[2:-3].strip() # slicing to get rid of quotes and new line character
    if command: run(f's {command}')

################################################
#################### INIT ######################
################################################
if __name__ == '__main__':
    if(len(sys.argv) == 1):
        notify("\n[✘] Error: No command provided.",fg="red",style="bold")
        help()
    else:
        command = sys.argv[1]
        rest = " ".join(sys.argv[2:])
        given = command + " " + rest
        a = locals().get(command, None)
        b = mappings.get(command,None)
        if a:
            a()
        elif b:
            run(b)
        else:
            run(f"{terminal} --command {given} &")
################################################
################################################
################################################
