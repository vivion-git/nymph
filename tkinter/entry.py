from Tkinter import *
def fetch():
    print 'Input => "%s"' % ent.get()
    ent.insert(END,'X')
    ent.insert(0,'x')    
root=Tk()
ent=Entry(root)
ent.pack(side=TOP,fill=X)
ent.focus()
ent.bind('<Return>',(lambda event:fetch()))
btn=Button(root,text='fetch',command=fetch)
btn.pack(side=LEFT)
root.mainloop()

