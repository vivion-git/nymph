
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
    def add(self,y):
        new={}
        for k in y.keys:new[k]=y[k]
        for k in self.keys:new[k]=self[k]
        return new
