
import sys, traceback
def safe(entry,*args):
    try:
         apply(entry,args)
    except:
         traceback.print_exc()
         print 'got',sys.exc_info()[0],sys.exc_info()[1]
import oops 
safe(oops.oops)


