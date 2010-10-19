
import sys, traceback
def safe(entry,*args):
    try:
         apply(entry,args)
    except:
         traceback.print_exc()
         print 'got',sys.exc_type,sys.exc_value
import oops 
safe(oops.oops)


