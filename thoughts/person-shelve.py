import shelve
from person import person
from manager import manager
bob=person('bob smith',42,30000,'sweng')
sue=person('sue jones',45,40000,'music')
tom=manager('tom doe',50,50000)
db=shelve.open('class-shelve')
db['bob']=bob
db['sue']=sue
db['tom']=tom
db.close()

