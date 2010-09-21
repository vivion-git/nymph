def adder1(*args):
    print 'adder1',
    if type(args[0])==type(0):
        sum=0
    else:
        sum=args[0][:0]
    for arg in args:
        sum=sum+arg
    return sum
print adder1(2,3,4)
print adder1([7,8,9],[1,2,3])        

