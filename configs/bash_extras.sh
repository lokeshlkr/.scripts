#! /usr/bin/sh


CM_LAUNCHER=rofi

alias ls='ls --color=auto'
alias ll='ls -lav --ignore=..'   # show long listing of all except ".."
alias l='ls -lav --ignore=.?*'   # show long listing but no hidden dotfiles except "."
alias lf='ls | grep -i'


alias install='paru -S'
alias remove='paru -Rns'
alias update='paru -Syyu'
alias exe='chmod +x'
alias code='codium'

alias 'cd..'='cd ..'

function mkcd(){
    mkdir $1
    cd $1
}
export -f mkcd

