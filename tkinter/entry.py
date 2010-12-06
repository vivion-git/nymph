from Tkinter import *
def fetch():
    print 'Input => "%s"' % ent.get()
root=Tk()
ent=Entry(root)
ent.insert(0,'type words here')
ent.pack(side=TOP,fill=X)
ent.focus()
ent.bind('<Return>',(lambda event:fetch()))
btn=Button(root,text='fetch',command=fetch)
btn.pack(side=LEFT)
root.mainloop()

note:the bind < >,the lower-level callback must get an event argument,this is
very impotant ,keep in mind,otherwise ,there will be a wrong message.
