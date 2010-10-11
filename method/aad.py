
class adder:
    def __init__(self,start=[]):
        self.data=start
    def __add__(self,other):
        return self.add(other)
    def add(self,y):
        print 'not implemented!'

class listadder(adder):
    def add(self,y):
        return self.data+y

class dictadder(adder):
    def __init__(self,new={}):
        self.new=new    
    def add(self,y):
        self.new.updata(y)
        return self.add(y)
