from Tkinter import *
def hello(event):
    print 'press twice to exit'
def quit(event):
    print 'hello,go'
    import sys;
    sys.exit()
widget=Button(None,text='hello event')
widget.pack()
widget.bind('<Button-1>',hello)
widget.bind('<Double-1>',quit)
widget.mainloop()
