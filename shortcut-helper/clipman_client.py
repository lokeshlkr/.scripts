#!/usr/bin/python

import subprocess, sys, os,re
from clipman_core import *

def get_indexes(text):
    items = re.split(r"\n|\\+n",text)
    return [int(i[:clipboard.padding]) for i in items if i]


def paste():
    presentable = clipboard.show()
    with open(clipman_buffer,'w') as f:
        f.write(presentable)
    text = execute(f'cat {clipman_buffer} | dmenu -l 20')
    to_paste = clipboard.paste(get_indexes(text))
    with open(clipman_buffer,'w') as f:
        f.write(to_paste)
    os.system(f'cat {clipman_buffer} | xclip -selection c')


    
clipboard.read_file()
if __name__ == "__main__":
    paste()







