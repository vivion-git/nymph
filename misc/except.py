class myerro():
    def __init__(self,data):
        self.data=data        
    def __repr__(self):
        return ("myerror.value is %s" % self.data)

def oops():
   raise  myerro('hello')
   
def dot():
    try:
        oops()
    except IndexError:
        print "an indexerror"
    except myerro,extraInfo:
       print  "myerro is :",extraInfo    
 #extraInfo is the return value of the  invoking function ,in this exmple ,is the function oops's return value.
 #when there is no return value ,we can add extraInfo to the raise statment
#for exmple,we can write in this way"raise myerro,extraInfo.(if myerro has not arguement)
    else:
        print "no error"
if __name__=='__main__':
    dot()
           
        
