#!/usr/bin/python

import subprocess, os, time

history_file = '/tmp/clipman_history'
history_length = 50
separator = "::clipmanseparator::"
newline = '\n'
data = []


def execute(command):
    x = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdout,error) = x.communicate()
    res = str(stdout)[2:-3].strip() # slicing to get rid of quotes and new line character
    return res

def load():
    global data, history_file, separator
    if not os.path.isfile(history_file):
        execute(f"touch {history_file}")
    with open(history_file,'r+') as f:
        data = f.read().split(separator)

def save():
    global data, history_file, history_length, separator
    if not os.path.isfile(history_file):
        execute(f"touch {history_file}")
    with open(history_file,'w') as f:
        txt = str(separator.join(data))
        f.write(txt)

def read_clipboard():
    global data
    clip = execute(f"xclip -selection clipboard -o")
    if data[0] != clip:
        data.insert(0,clip)
        data = data[:history_length]
        save()    
    
load()
while True:
    read_clipboard()
    time.sleep(0.1)
