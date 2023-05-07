#!/usr/bin/python

import subprocess, time
from clipman_core import *

temp = ""

def read_clipboard():
    global temp
    clip = execute(f"xclip -selection c -o")
    if clip != temp:
        clipboard.add(clip)
    temp = clip
    
clipboard.read_file()
while True:
    read_clipboard()
    time.sleep(0.1)
