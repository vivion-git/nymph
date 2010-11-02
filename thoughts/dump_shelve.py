import shelve
db=shelve.open('member-shelve')
for key in db:
    print key, '=>\n ', db[key]
print db['sue']['name']
db.close()
