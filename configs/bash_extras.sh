#! /usr/bin/sh

alias ls='ls -lah --color=auto --ignore=..'
alias ll='ls -lav --ignore=..'   # show long listing of all except ".."
alias l='ls -lav --ignore=.?*'   # show long listing but no hidden dotfiles except "."
alias lf='ls | grep -i'


alias install='paru -S'
alias remove='paru -Rns'
alias update='paru -Syyu'
alias exe='chmod +x'

alias 'cd..'='cd ..'

# function mkcd() {
#     mkdir $1
#     cd $1
# }
# export -f mkcd
JAVA_HOME=/home/stranger/.apps/android-studio/jbr/

PATH=$PATH:/home/stranger/.apps/android-studio/bin/
PATH=$PATH:/home/stranger/.apps/android-studio/jbr/bin/
# PS1='\[\e[93m\]╭\[\e[92m\]\@ \[\e[93;1m\]◦ \[\e[22m\]\u \[\e[1m\]◦ \[\e[0;95m\]\w\[\e[38;5;242m\]⏎\n\[\e[93m\]╰─────────⌲ \[\e[0m\]'
