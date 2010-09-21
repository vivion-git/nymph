x=5
l=[]
for i in range(7):
    l.append(2**i)
print l    
if (2**x) in l:
    print (2**x),'was found',l.index(2**x)
else:
    print x,'not found'
