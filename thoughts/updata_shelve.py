from initdata import tom
import shelve
db=shelve.open('member-shelve')
sue=db['sue']
sue['pay']*=1.5
db['tom']=tom
db['sue']=sue
db.close()






























































































from initdata import tom
import shelve
db=shelve.open('member-shelve')

sue=db['sue']
db['sue']['pay']*=1.5
db['tom']=tom
db['sue']=sue
db.close()

