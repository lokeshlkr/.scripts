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
        git add . && git commit -m "syncing" && git push origin master && echo "\e[0;32Sync completed."|| echo "\e[0;31Something went wrong."
    else
        echo "\e[0;33Not a git repository."
    fi
    exit
fi
