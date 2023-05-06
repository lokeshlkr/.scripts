#!/usr/bin/python

import subprocess, sys, os
from clipman_shared import *
data = []

def make_presentable(item):
    lines = item.split(line_separator)
    res = lines[0][:50]
    if len(lines) > 1:
        res += f' ({len(lines)} lines)'
    return res


def paste():
    global data
    data = load()
    to_show = [str(i).rjust(2,'0') + ": " + make_presentable(data[i]) for i in range(len(data))]
    with open(clipman_buffer,'w') as f:
        f.write(os.linesep.join(to_show))
    res = execute(f"cat {clipman_buffer} | rofi -dmenu -multi-select")    
    # print(f"<<<<{res}>>>>")
    indexes = [int(line[:2]) for line in res.split('\\n') if line[:2].isdigit()]
    usefuldata = [data[i] for i in indexes]
    clip = '\n'.join(usefuldata)
    with open(clipman_buffer,'w') as f:
        f.write(clip)
    os.system(f"xclip -selection c -i {clipman_buffer}")
    

if __name__ == "__main__":
    paste()

