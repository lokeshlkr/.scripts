#! /usr/bin/python

import sys,os,ast
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
commands={
    'help':'Show this help message',
    'search':'Search a text in firefox in duckduckgo',
    'browse':'Browse any URL in firefox',
    'sync':'Push a git repository to origin',
    'panel':'Run a panel script',
    'rust':'Open rust practice project in VSCode',
    'rustnew':'Create new rust practice project and open it in VSCode',
    'vsc':'Open some basic locations in VSCode',
    'restart':'Restart any program',
}
filename = sys.argv[0]
command = rest = ""
def print_color(text,fg="",bg="",style="",end="\n"):
    fg = colors["fg"].get(fg.lower(),"")
    bg = colors["bg"].get(bg.lower(),"")
    style = colors["style"].get(style.lower(),"")
    reset = colors["style"]['reset']
    print(f"{fg}{style}{bg}{text}{reset}",end=end)
def run(command):
    return os.system(command) == 0
def is_git_repo():
    cwd = os.getcwd()
    cwd = cwd.split('/')[1:]
    isGitRepo = False
    for i in range(len(cwd)-1,-1,-1):
        path = '/' + '/'.join(cwd[:i])
        dirs = os.listdir(path)
        if '.git' in dirs:
            return path
################################################
################################################
################################################

def help():
    print_color("\nAvailable Commands:",fg="blue")
    for command in commands:
        print_color("○ "+command.ljust(15," "),style="bold",end="")
        print_color("- "+commands[command])
    print()

def search():
    command = f'firefox "https://duckduckgo.com/?q={rest}" 2>/dev/null &'
    run(command)

def browse():
    url = 'https://' + (rest if "." in rest else rest + ".com")
    command = f'firefox "{url}" 2>/dev/null &'
    run(command)

def sync():
    git_path = is_git_repo()
    if git_path != None:
        os.chdir(git_path)
        command = f'git add . && git commit -m "autosync: {rest}" && git push origin master'
        if run(command):
            print_color("Synced Successfully!",fg="green",style="bold")
        else:
            print_color("Some error occured!",fg="red",style="bold")

def panel():
    file = f"/home/stranger/working_folder/.scripts/panel/{rest}"
    run(file)

def rustnew():
    os.chdir("/home/stranger/working_folder/rust/")
    run('mv practice "practice_$(date +%Y%m%d_%H%M%S)"')
    run('cargo new practice')
    run('code /home/stranger/working_folder/rust/practice')

def rust():
    if os.path.exists('/home/stranger/working_folder/rust/practice'):
        run('code /home/stranger/working_folder/rust/practice')
    else:
        rustnew()

def vsc():
    match rest.strip():
        case "scripts":
            run('code /home/stranger/working_folder/.scripts')
        case "home":
            run('code /home/stranger')

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
