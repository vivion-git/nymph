from Tkinter import *
from dialogtable import demos
class Demo(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        Label(self,text="Basic demos").pack()
        for (key,value) in demos.items():
            Button(self,text=key,command=value).pack(side=TOP,fill=BOTH)
if __name__=='__main__':
    Demo().mainloop()

