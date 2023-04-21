#! /usr/bin/python

import sys,os,ast,subprocess
from time import sleep
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
################################################
#################### SETUP #####################
################################################
editor = "codium"
browser = "firefox"
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
    'gui':'show dialog box to capture a command'
}
paths = {
    'home' : home,
    'rust' : f'{home}/working_folder/rust/practice',
    'self' : f'{home}/working_folder/.scripts',
}
################################################
################################################
################################################

filename = sys.argv[0]
command = rest = ""
def run(command):
    return os.system(command) == 0

def print_color(text,fg="",bg="",style="",end="\n", notify=0):
    if notify in (0,2):
        fg = colors["fg"].get(fg.lower(),"")
        bg = colors["bg"].get(bg.lower(),"")
        style = colors["style"].get(style.lower(),"")
        reset = colors["style"]['reset']
        formatted_mesasge = f"{fg}{style}{bg}{text}{reset}"
        print(formatted_mesasge,end=end)
    if notify > 0:
        timeout = "-t 0" if len(text) > 100 else ""
        run(f'notify-send ShortcutHelper "<span font-family=\'Stranger Nerd Font Mono\'>{text}</span>" -i keyboard {timeout}')

def is_git_repo():
    cwd = os.getcwd()
    cwd = cwd.split('/')[1:]
    isGitRepo = False
    l = len(cwd)
    for i in range(l):
        path = '/' + '/'.join(cwd[:l-i])
        dirs = os.listdir(path)
        if '.git' in dirs:
            return path
################################################
################################################
################################################

def help():
    print_color("\nAvailable Commands:",fg="blue")
    text = "Available Commands:\n"
    for command in commands:
        text += "○ "+command.ljust(10," ")
        text += "- "+commands[command] + "\n"
        print_color("○ "+command.ljust(10," "),style="bold",end="")
        print_color("- "+commands[command])
    print_color(text,notify=1)
    print()

def search():
    command = f'{browser} "https://duckduckgo.com/?q={rest}" 2>/dev/null &'
    run(command)

def browse():
    url = 'https://' + (rest if "." in rest else rest + ".com")
    command = f'{browser} "{url}" 2>/dev/null &'
    run(command) 

def sync():
    git_path = is_git_repo()
    if git_path != None:
        os.chdir(git_path)
        command = f'git add . && git commit -m "autosync: {rest}" && git push origin master'
        if run(command):
            print_color("Synced Successfully!",fg="green",style="bold", notify=2)
        else:
            print_color("Some error occured!",fg="red",style="bold", notify=2)
    else:
        print_color("Not a git repo!",fg="orange",style="bold", notify=2)

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
        print_color("Something went wrong, new practice project could not be created.",fg="red",style="bold",notify=2)

def rust():
    if not openineditor(paths['rust']):
        rustnew()

def edit():
    match rest.strip():
        case "":
            openineditor(paths['self'])
        case "home":
            openineditor(paths['home'])
        case _:
            print_color(f"Folder name not configured.\nCheck spelling or add it in script.",fg="orange",style="bold",notify=2)


def restart():
    if len(rest.strip()) == 0:
        print_color("Provide a program to restart.",fg="red")
    else:
        x = run(f'killall {rest}')
        if(not x):
            run(rest)
        else:
            sleep(0.2)
            run(rest)


################################################
#################### INIT ######################
################################################

def gui():
    x = subprocess.Popen("zenity --entry --text='Enter a shelp command:'",shell=True,stdout=subprocess.PIPE)
    (command, error) = x.communicate()
    command = str(command)[2:-3] # to get rid of auotes and new line character
    run(f's {command}')

if(len(sys.argv) == 1):
    print_color("\n[✘] Error: No command provided.",fg="red",style="bold")
    help()
else:
    command = sys.argv[1]
    rest = " ".join(sys.argv[2:])
    if(command not in commands):
        print_color("\n[✘]Error: Given command is not valid.",fg="red",style="bold")
        help()
    else:
        locals()[command]()
################################################
################################################
################################################
