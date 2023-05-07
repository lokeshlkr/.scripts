#!/bin/sh
redshift -PO 4500 &
xset r rate 250 20 &
# clears the state of capslock
# remaps capslock key to F35 key
# so sxhkd can use it without issues
xmodmap -e 'clear lock' 
xmodmap -e 'keycode 66 = F35' 
ksuperkey -e 'Super_L=F34' -t 250

~/working_folder/.scripts/shortcut-helper/clipman_deamon.py &
sxhkd &
