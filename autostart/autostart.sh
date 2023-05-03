#!/bin/sh
redshift -PO 4500 &
xset r rate 250 20 &
# clears the state of capslock
xmodmap -e 'clear lock' 
# remaps capslock key to F35 key
# so sxhkd can use it without issues
xmodmap -e 'keycode 66 = F35' 
clipmenud &
sxhkd &
