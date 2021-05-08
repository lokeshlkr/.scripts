#!/bin/sh

args=($@)
rest="${args[@]:1}"

configure(){
    code ~/.scripts/shortcut-helper/shelp.sh
}
updatetheme(){
    code ~/.config/xfce4/terminal/terminalrc
}
search(){    
    firefox "https://duckduckgo.com/?q=$rest" 2>/dev/null &
}
browse(){
    firefox "https://$rest" 2>/dev/null &
}
sync(){
    if [[ -d ./.git ]] ; then
        git add . && git commit -m "syncing $rest" && git push origin master && echo -e "\\e[1;32mSync completed.\\e[0;0m"|| echo -e "\\e[1;31mSomething went wrong.\\e[0;0m"
    else
        echo -e "\\e[0;33mNot a git repository.\\e[0;0m"
    fi
}
help(){
    echo -e "\\e[1;31m[!] Unknown command:\\e[1;37m '$1'"
    echo -e "\\e[0;32m[i] Known commands:\\e[1;37m"
    echo -e "$commands\\e[0;0m"
}

# commands=$(typeset -F | sed s/-f//g | sed s/declare//g)
commands=$(typeset -f)
$1 || help

