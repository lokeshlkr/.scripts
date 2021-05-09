#!/bin/python
# from tkinter import *
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

height=500
width=500

fb = []
def draw(x,y,i):
    color = str(hex((250-10*i)*0x10101))[2:]
    color = "#"+((6 - len(color))*"0")+color
    
    fb.append((x,y,color))

    # FOR PRINTING IN TERMINAL
    # density = [" ","░","▒","▓","█"]
    # print(density[i//5],end="")
    
for y in range(height):
    for x in range(width):
        zx,zy = cx,cy = -2+2.5*x/width, -1.25+2.5*y/height
        for i in range(25):
            zx,zy = (zx*zx-zy*zy)+cx, (2*zx*zy)+cy
            if (zx*zx)+(zy*zy) > 4: break
        draw(x,y,i)
    # FOR PRINTING IN TERMINAL
    # print()
  
# FOR GRAPHICAL OUTPUT
# root = Tk()
# C = Canvas(root, bg ="red",height = height, width = width)
# for x,y,color in fb:
#     C.create_rectangle( (x, y)*2 ,outline=color)
# C.pack()
# root.mainloop()

def save_image():    
    canvas = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(canvas)
    for x,y,color in fb:
        draw.point( (x, y)*2 ,fill=color)
    canvas.save("fractal_"+str(width)+"x"+str(height)+".png")
        
save_image()