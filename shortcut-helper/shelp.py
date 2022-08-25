#! /usr/bin/python

import sys,os,ast

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
commands=['help','search','browse','sync']
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
        print("○",command)
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

# sync(){
#     if [[ -d ./.git ]] ; then
#         git add . && git commit -m "autosync: $rest" && git push origin master && echo -e "\\e[1;32mSync completed.\\e[0;0m"|| echo -e "\\e[1;31mSomething went wrong.\\e[0;0m"
#     else
#         echo -e "\\e[0;33mNot a git repository.\\e[0;0m"
#     fi
# }
# help(){
#     echo -e "\\e[0;34mUsage: s COMMAND [OPTIONS]\\e[1;37m"
#     echo -e "\\e[0;32mKnown Commands:\\e[1;37m"
#     echo -e "$commands\\e[0;0m"
# }
# panel(){
#     /home/stranger/working_folder/.scripts/panel/$rest
# }
# rust(){
#     test -d /home/stranger/working_folder/rust/practice

#     if [ $? -eq "0" ]; then
#         code /home/stranger/working_folder/rust/practice
#     else
#         rustnew
#     fi
# }
# rustnew(){
#     cd /home/stranger/working_folder/rust/
#     mv practice "practice_$(date +%Y%m%d_%H%M%S)"
#     cargo new practice
#     cd practice
#     code .
# }
# vsc(){
#     case $rest in
#         *"scripts"*)
#             code /home/stranger/working_folder/.scripts ;;
#         *"home"*)
#             code /home/stranger ;;
#         *"rustnew"*)
#             rustnew ;;
#         *"rust"*)
#             rust ;;
#     esac
# }
# restart(){
#     if [[ $rest ]];then
#         killall $rest
#         sleep 1
#         $rest
#     else
#         echo -e "\\e[0;31mProvide a program to restart.\\e[1;37m"
#     fi
# }


# commands=$(typeset -F | sed s/-f//g | sed s/declare//g)

# if [[ (-z "$action") ]]; then
#     action="FILLER COMMAND WHEN NO COMMAND IS PROVIDED TO FIX BELOW CASE STATEMENT"
# fi

# case $commands in
#     *"$action"*)
#         $action;;
#     *)
#         help;;
# esac