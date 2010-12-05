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

note:the callback handler is an anoymous function made with a lambda now,In
practice, the lambda could appear within the call to Button itself because it
is an expression and it need not be assigned to a name,we alse can use it like
the following:
func=(lambda self =self,name=key: self.printit(name))
func=(lambda handler=self.printit,name=key: handler(name))

we can write the def function instead of lambda:
for (key,value) in demos.items():
    def func(key=key): self.printit(key)
lambda is very import in widget .
