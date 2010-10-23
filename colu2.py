#!/usr/bin/python

import sys 
filename=sys.argv[1]
numcols=int(sys.argv[2])
totals=[0]*numcols
for line in open(filename):
    cols=line.split(',')
    nums=[int(x)for x in cols]
    totals=[(x+y)for (x,y)in zip(totals,nums)]
print totals

another way to get the same result is :

filename = 'data.py'
sums={}
for line in open(filename):
    cols=line.split(',')
    nums=[int(col) for col in cols]
    for (ix,num) in enumerate(nums):
        sums[ix]=sums.get(ix,0)+num
for key in sorted(sums):
     print key,'=',sums[key]
this way use the sys.argv ,so we should chmod the file ,and type the commond 
colu2.py data.py columnums and then it will run correctly.
 
