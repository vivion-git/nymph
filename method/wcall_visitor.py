import os ,sys
alllines=allfiles=0
allexts=['.py','.pyc']
allsums=dict.fromkeys(allexts,0)
def sum(dir,file,ext):
    global allfiles,alllines,dcount
    print file
    fname=os.path.join(dir,file)
    lines=open(fname).readlines()
    allfiles+=1
    alllines+=len(lines)
    allsums[ext]+=1
def wc(ignore,dir,fileshere):
    for file in fileshere:
        for ext in allexts:
            if file.endswith(ext):
                sum(dir,file,ext)
                break
if __name__=='__main__':
    os.path.walk(sys.argv[1],wc,None)
    print "visited %s files  " % allfiles
    print '-'*30
    print 'files=>',allfiles,'lines=>',alllines
    print allsums
 summary:
when we use the module os.path.walk(argv,func,name),the call func must have
three or more arguments,func(arg,top,names),if the arguments is less that
three,there will be a wrong message.so the above func "wc"
(ignore,dir,fileshere) and sum(dir,file,ext).if we don't use os.path.walk ,no
need three arguments.
