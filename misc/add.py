def prime (x,y):
    while x>1:


        if y%x==0:
            print y,'has factor',x
            break
        x=x-1
    else:
        print y,'is prime'
prime(3,9) 
prime(4,10)
