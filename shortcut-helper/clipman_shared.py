import asyncio, os,subprocess,re

history_file = '/tmp/clipman_history'
clipman_buffer = '/tmp/clipman_buffer'
history_length = 50
item_separator = "--++-+-++--"
line_separator = "::..:.:..::"
line_length = 50


def execute(command):
    x = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdout,error) = x.communicate()
    res = str(stdout)[2:-1].strip() # slicing to get rid of quotes b'xxxxxx'
    return res


def load():
    global history_file, item_separator
    data = []
    if not os.path.isfile(history_file):
        execute(f"touch {history_file}")
    with open(history_file,'r') as f:
        data = f.read()
        data = re.sub("\\+n", line_separator, data)
        data = data.split(item_separator)
    return data

def save(data):
    global history_file, history_length, item_separator
    if not os.path.isfile(history_file):
        execute(f"touch {history_file}")
    x = item_separator.join(data)
    execute(f"echo -e {x} > {history_file}")
    # cleandata = [re.sub("\\+n", line_separator, item) for item in data]
    # with open(history_file,'w') as f:
    #     txt = str(item_separator.join(cleandata))
    #     txt = re.sub("\\+n", line_separator, txt)
    #     f.write(txt)


if __name__ == "__main__":
    a = """\\n\\n\\n\\n\\\\nnnn\\\n\\\\\n\\\\\n\\\\n"""
    a = re.sub(r"\\",r"\\\\",a)
    a = re.findall(r"\\+n",a)
    print(a)