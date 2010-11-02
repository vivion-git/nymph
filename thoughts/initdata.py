bob={'name':'bob smith','age':42,'pay':3000,'job':'dev'}
sue={'name':'sue jones','age':45,'pay':4000,'job':'mus'}
tom={'name':'tom','age':50,'pay':0,'job':None}
#database
db={}
db['bob']=bob
db['sue']=sue
db['tom']=tom

if __name__=='__main__':
    for key in db:
        print key,'=>\n',db[key]

