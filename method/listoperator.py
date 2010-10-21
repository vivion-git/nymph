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

if __name__ == '__main__':
    x=mylist('spam')
    print x
    print x[2]
    print x[1:]
    print x + ['eggs']
    print x*3
    x.append('a')
    x.sort()
    for c in x: print c


built-in methods
---------------------------------
pprint :The pprint module provides a capability to “pretty-print” arbitrary
Python data structures in a form which can
be used as input to the interpreter. If the formatted structures include
objects which are not fundamental Python
types, the representation may not be loadable. This may be the case if objects
such as files, sockets, classes, or
instances are included, as well as many other builtin objects which are not
representable as Python constants.

pprint(object[, stream[, indent[, width[, depth ]]]])
    Prints the formatted representation of object on stream, followed by a
newline. If stream is omitted,
    sys.stdout is used. This may be used in the interactive interpreter
instead of a print statement for in-
    specting values. indent, width and depth will be passed to the
PrettyPrinter constructor as formatting
    parameters.
           >>> stuff = sys.path[:]
           >>> stuff.insert(0, stuff)
           >>> pprint.pprint(stuff)
           [<Recursion on list with id=869440>,
             ’’,
             ’/usr/local/lib/python1.5’,
             ’/usr/local/lib/python1.5/test’,
             ’/usr/local/lib/python1.5/sunos5’,
             ’/usr/local/lib/python1.5/sharedmodules’,
             ’/usr/local/lib/python1.5/tkinter’]



