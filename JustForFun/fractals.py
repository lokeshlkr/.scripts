#!/bin/python
from tk import *
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

height=500
width=500
fb = []

def show_tui():
    density = [" ","░","▒","▓","█"]
    for x,y,color,i in fb:
        end = "" if x<(width-1) else "\n"
        print(density[i//5],end=end)
    
def show_gui():
    root = Tk()
    C = Canvas(root, bg ="red",height = height, width = width)
    for x,y,color,i in fb:
        C.create_rectangle( (x, y)*2 ,outline=color)
    C.pack()
    root.mainloop()

def save_image():    
    canvas = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(canvas)
    for x,y,color,i in fb:
        draw.point( (x, y)*2 ,fill=color)
    canvas.save("fractal_"+str(width)+"x"+str(height)+".png")       


def get_color(x,y,i):
    color = str(hex((250-10*i)*0x10101))[2:]
    color = "#"+((6 - len(color))*"0")+color    
    fb.append((x,y,color,i))


for y in range(height):
    for x in range(width):
        print(y,x)
        zx,zy = cx,cy = -2+2.5*x/width, -1.25+2.5*y/height
        i = 0
        while (i < 25) and ((zx*zx)+(zy*zy) <= 4):
            zx,zy = (zx*zx-zy*zy)+cx, (2*zx*zy)+cy
        get_color(x,y,i)
# show_gui()
# save_image()
show_tui()