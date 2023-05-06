#!/usr/bin/python

import subprocess, os, time
from clipman_shared import *
data = []

def read_clipboard():
    global data, line_separator
    clip = execute(f"xclip -selection c -o")
    clip = clip.replace('\n', line_separator)
    if len(data)==0 or clip not in data[0]:
        try:data.remove(clip)
        except:pass
        data.insert(0,clip)
        data = data[:history_length]
        save(data)
    
data = load()
while True:
    read_clipboard()
    time.sleep(0.1)
