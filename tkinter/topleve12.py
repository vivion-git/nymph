from Tkinter import *
root =Tk()
trees=[('the larch!','light blue'),('the pine!','light green'),
       ('the biant redwood!','red')]
for (tree,color) in trees:
    win=Toplevel(root)
    win.title('sing....')
    win.protocol('WM_DELETE_WINDOW',lambda:0)
    msg=Button(win,text=tree,command=win.destroy)
    msg.pack(expand=YES,fill=BOTH)
    msg.config(padx=10,pady=10,bd=10,relief=RAISED)
    msg.config(bg='black',fg=color,font=('times',30,'bold italic'))
root.title('Lumberjack demo')
Label(root,text='Main widow',width=30).pack()
Button(root,text='Quit All',command=root.quit).pack()
root.mainloop()

