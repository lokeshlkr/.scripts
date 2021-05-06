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
    firefox "https://duckduckgo.com/?q=$rest"
    exit
fi

if [[ $1 = "push" ]] ; then
    if [[ -d ./.git ]] ; then
        git add . && git commit -m "syncing" && git push origin master || echo ">>Something went wrong<<".
    else
        echo Not a git repository.
    fi
    exit
fi
