import sys
from Tkinter import Toplevel,Button,Label
win1=Toplevel()
win2=Toplevel()
Button(win1,text='spam',command=sys.exit).pack()

Button(win2,text='SPAM',command=sys.exit).pack()
Label(text='Popups').pack()
win1.mainloop()

