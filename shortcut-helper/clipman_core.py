import  os,subprocess,re

clipman_history = '/tmp/clipman_history'
clipman_buffer = '/tmp/clipman_buffer'
clipman_capacity = 50
presentable_line_length = 50



def execute(command):
    x = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (stdout,error) = x.communicate()
    res = str(stdout)[2:-1].strip() # slicing to get rid of quotes b'xxxxxx'
    return res

class Clip():
    def get_lines(text):
        res = re.split(r"\\+n|\n", text)
        return res

    def __init__(self,text):
        self.text = Clip.get_lines(text)

    def __str__(self):
        global presentable_line_length
        t = self.text[0][:presentable_line_length]
        lines = str(len(self.text))
        padding = presentable_line_length - len(t)
        padding = " "*padding
        return f"{t}{padding} ({lines}) lines"
    
    def __eq__(self,other):
        return self.write() == other.write()
    
    def write(self):
        return "\n".join(self.text)


class Clipboard():
    def __init__(self,capacity):
        self.clip_separator = "\n##==#==##\n"
        self.clips = []
        self.capacity = capacity
        self.padding = len(str(self.capacity))

    def is_present(self,clip):
        for c in self.clips:
            if c == clip:
                return True
        return False

    def add(self,text):
        clip = Clip(text)
        if self.is_present(clip):
            return
        self.clips.append(clip)
        if len(self.clips) > self.capacity:
            del self.clips[0]
        self.save_file()

    def paste(self,ids):
        res = ""
        for i in ids:
            res += self.clips[i].write()
        for i in ids:
            del self.clips[i]
        return res

    def show(self):
        items = [str(i) for i in self.clips]
        presentable = [str(i).rjust(self.padding,"0") + ": " + items[i] for i in range(len(items)-1,-1,-1)]
        rofi_list = "\n".join(presentable)
        return rofi_list
    
    def read_file(self):
        global clipman_history
        data = ""
        if not os.path.isfile(clipman_history):
            execute(f"touch {clipman_history}")
            return
        with open(clipman_history,'r') as f:
            data = f.read()
            data = re.split(self.clip_separator, data)
        self.clips = [Clip(i) for i in data if len(i)>0]

    def save_file(self):
        global clipman_history
        data = [x.write() for x in self.clips]
        x = self.clip_separator.join(data)
        with open(clipman_history,'w') as f:
            f.write(x)


clipboard = Clipboard(clipman_capacity)

if __name__ == "__main__":
    c = Clipboard(50)
    c.add("asdasdasdasd asd asd  ads dasd asd asd asd \n ad asd asda sdas d\nasd asd asd asda sd\nads as asd.")
    c.add("asdasdasdasd asd asd  ads dasd asd asd asd \n ad asd asda sdas d\nasd asd asd asda sd\nads as asd.")
    c.add("asdasdasdasd asd asd  ads dasd asd asd asd \n ad asd asda sdas d\nasd asd asd asda sd\nads as asd.")
    c.add("asdasdasdasd asd asd\nads dasd\nasd asd asd \n ad asd asda sdas d\nasd asd asd asda sd\nads as asd.")
    c.add("asdasdasdasd asd asd\nads dasd\nasd asd asd \n ad asd asda sdas d\nasd asd asd asda sd\nads as asd.")
    c.add("asdasdasdasd asd asd\nads dasd\nasd asd asd \n ad asd asda sdas d\nasd asd asd asda sd\nads as asd.")
    c.add("asdasdasdasd asd asd\nads dasd\nasd asd asd \n ad asd asda sdas d\nasd asd asd asda sd\nads as asd.")
    c.add("asdasdasdasd asd asd\nads dasd\nasd asd asd \n ad asd asda sdas d\nasd asd asd asda sd\nads as asd.")
    print(c.show())
    print(c.paste([0]))