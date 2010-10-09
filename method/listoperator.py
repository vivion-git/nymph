class mylist:
    def __init__(self,start):
        self.wrapped=[]  #self.wrapped=start[:]
        for x in start:self.wrapped.append(x)   #copying the initial value 
    def __add__(self,other):
        return mylist(self.wrapped+other)
    def __mul__(self,time):
        return mylist(self.wrapped*time)
    def __getitem__(self,offset):
        return self.wrapped[offset]
    def len__(self):
        return len(self.wrapped)
    def __getslice__(self,low,high):
        return mylist(self.wrapped[low:high])
    def append(self,node):
        self.wrapped.append(node)
    def __getattr__(self,name):
        return getattr(self.wrapped,name)
    def __repr__(self):
        return repr(self.wrapped)

if __name__='__main__':
    x=mylist('spam')
    print x
    print x[2]
    print x[1:]
    print x + ['eggs']
    print x*3
    x.append('a')
    x.sort()
    for c in x: print c

