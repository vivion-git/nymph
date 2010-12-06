import sys
from Tkinter import *
makemodal=(len(sys.argv)>1)
def dialog():
    win=Toplevel()
    Label(win,text='Hard drive reformatted!').pack()
    Button(win,text='OK',command=win.destroy).pack()
    if makemodal:
        win.focus_set()
        win.grab_set()
        win.wait_window()
    print 'dialog exit'
root =Tk()
Button(root,text='popup',command=dialog).pack()
root.mainloop()

note:behind the if ,there are three
functions,win.focus_set(),win.grab_set()and win.wait_window(),the three
functions will lock other windows and waiting for a reply ,making the dialogs
modal.
