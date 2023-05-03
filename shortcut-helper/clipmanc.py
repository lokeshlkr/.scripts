#!/usr/bin/python

import subprocess, sys, os

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


def make_presentable(item):
    lines = item.split(newline)
    res = ""
    if len(lines[0]) < 30:
        res = lines[0]
    else:
        res = lines[0][:30]
    # if len(lines) > 1:
    res += f' ({len(lines)} lines)'
    return res


def paste():
    load()
    to_show = [str(i).rjust(2,'0') + ": " + make_presentable(data[i]) for i in range(len(data))]
    to_show = "\n".join(to_show)
    print(to_show)
    res = execute(f"echo -e {to_show} | rofi -dmenu -multi-select &")
    print ("selected",res)
    
if __name__ == "__main__":
    command = sys.argv[1]
    x = locals().get(command, None) 
    if x:
        x()