#!/bin/sh

args=($@)
rest="${args[@]:1}"
commands=(configure updatetheme search browse sync)

if [[ $1 = ${commands[0]} ]] ; then
    nvim ~/.scripts/shortcut-helper/shelp.sh
    exit
fi

if [[ $1 = ${commands[1]} ]] ; then
    nvim ~/.config/xfce4/terminal/terminalrc
    exit
fi

if [[ $1 = ${commands[2]} ]] ; then
    firefox "https://duckduckgo.com/?q=$rest" 2>/dev/null &
    exit
fi

if [[ $1 = ${commands[3]} ]] ; then
    firefox "https://$rest" 2>/dev/null &
    exit
fi

if [[ $1 = ${commands[4]} ]] ; then
    if [[ -d ./.git ]] ; then
        git add . && git commit -m "syncing $rest" && git push origin master && echo -e "\\e[0;32mSync completed.\\e[0;0m"|| echo -e "\\e[0;31mSomething went wrong.\\e[0;0m"
    else
        echo -e "\\e[0;33mNot a git repository.\\e[0;0m"
    fi
    exit
fi

echo -e "\\e[0;31mUnknown command:\\e[0;0m $1"
echo -e "\\e[1;34mKnown Commands:\\e[0;32m ${commands[@]:0}\\e[0;0m"
exit
