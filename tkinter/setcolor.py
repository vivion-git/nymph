from Tkinter import *
from tkColorChooser import askcolor
def setBgColor():
    (triple,hexstr)=askcolor()
    if hexstr:
        print hexstr
        push.config(bg=hexstr)
root =Tk()
push=Button(root,text='set Background Color',command=setBgColor)
push.config(height=3,font=('times',20,'bold'))
push.pack(expand=YES,fill=BOTH)
root.mainloop()

note:ther script is run ,when you choose the color in the askcolor dialog,the
background of the Button will be changed.
