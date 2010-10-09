 the notice in using class 
there are three ideas about python's implementation of
OOP:inheritance,polymorpyism and encapsulation.
1)inheritance:
the example is related to the built-in  method "add",replace argument
in-place,if we don't want to replace in-place,we should use two argument ,just
like the under example:
class adder:
    def __init__(self,data=[]):
        self.data=data
    def add(self,x,y):
        print"Not Implemented"
    def __add__(self,other):
        return self.add(self,other)
class listadder(adder):
    def add(self,x,y):
        return x+y
class dictadder(adder):
    def add(self,x,y):
        new={}
        for k in x.keys():
            new[k]=x[k]
        for k in y.keys():
            new[k]=y[k]
            return new
note:in above code ,init has define the type of  argument,"data=[]",so if x or
y is not that type ,there will be a erro display.(e.g if we input
y=({q:1},{w:2}),there will be erro output )
another way to complete this task ,we also can write code like this ,this way
will save a value in the instance anyhow ,we just take one argument .
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
        pass
to run it in python,we can get the same result with the first one. 
