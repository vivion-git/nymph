from Tkinter import *
from dialogtable import demos
class Demo(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        Label(self,text='Basic demos').pack()
        for (key,value)in demos.items():
            func=(lambda key=key: self.printit(key))
            Button(self,text=key,command=func).pack(side=TOP,fill=BOTH)
    def printit(self,name):
        print name,'returns =>',demos[name]()
if __name__=='__main__': Demo().mainloop()

