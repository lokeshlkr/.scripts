#! /usr/bin/sh


alias ls='ls --color=auto'
alias ll='ls -lav --ignore=..'   # show long listing of all except ".."
alias l='ls -lav --ignore=.?*'   # show long listing but no hidden dotfiles except "."


alias install='paru -S'
alias remove='paru -Rns'
alias update='paru -Syyu'
alias exe='chmod +x'