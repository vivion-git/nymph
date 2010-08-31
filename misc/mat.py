import re
x=['sit','a','span','a']
while x:
    if re. match(x[0],'a'):
        print 'Ni'
    else:
        print x
    x = x[1:]
else:
     print 'not found'
