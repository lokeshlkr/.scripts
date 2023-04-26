#! /usr/bin/sh


alias ls='ls --color=auto'
alias ll='ls -lav --ignore=..'   # show long listing of all except ".."
alias l='ls -lav --ignore=.?*'   # show long listing but no hidden dotfiles except "."
alias lf='ls | grep -i'


alias install='paru -S'
alias remove='paru -Rns'
alias update='paru -Syyu'
alias exe='chmod +x'

# clears the state of capslock
xmodmap -e 'clear lock' 
# remaps capslock key to F35 key
# so sxhkd can use it without issues
xmodmap -e 'keycode 66 = F35' 
