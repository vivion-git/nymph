import shelve
from person import person
fieldnames=('name','age','job','pay')
db=shelve.open('class-shelve')
while True:
    key=raw_input('\nkey?=> ')
    if not key:break
    if key in db.keys():
         record=db[key]
    else:
        record=person(name='?',age='?')
    for field in fieldnames:
        currval=getattr(record,field)
        newtext=raw_input('\t[%s]=%s\n\t\tnew?=>' % (field,currval))
        if newtext:
            setattr(record,field,eval(newtext))
    db[key]=record
db.close()
