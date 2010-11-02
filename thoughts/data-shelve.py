from initdata import bob, sue
import shelve
db=shelve.open('member-shelve')
db['bob']=bob
db['sue']=sue
db['tom']=tom
db.close()

