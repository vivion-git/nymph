d1=[1,2,3,4]
d2=[5,6,7,2,3]
new=[]
for x in d1:
        if x in d2:
            new.append(x)
print new
 
so now ,how the difference between sort and sorted()

  the .sort() method of lists sorts the list in place, while sorted() creates a
new list. So if you have a large list, part of your performance difference
will be due to copying.list.sort() is about 2% faster than sorted(), which
would make sense due to the copying overhead.


