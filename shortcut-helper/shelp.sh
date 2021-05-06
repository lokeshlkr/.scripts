#!/bin/sh

args=($@)
rest="${args[@]:1}"

if [[ $1 = "scripts" ]] ; then
    nvim ~/.scripts/
    exit
fi

if [[ $1 = "updatetheme" ]] ; then
    nvim ~/.config/xfce4/terminal/terminalrc
    exit
fi

if [[ $1 = "search" ]] ; then
    firefox "https://duckduckgo.com/?q=$rest" 2>/dev/null &
    exit
fi

if [[ $1 = "sync" ]] ; then
    if [[ -d ./.git ]] ; then
        git add . && git commit -m "syncing" && git push origin master && echo "\\e[0;32mSync completed.\\e[0;0m"|| echo "\\e[0;31mSomething went wrong.\\e[0;0m"
    else
        echo -e "\\e[0;33mNot a git repository.\\e[0;0m"
    fi
    exit
fi
