def factorial(n):
  if n == 0:
    return 1
  else:
    recurse = factorial(n-1)
    print recurse, n
    result = n * recurse
    return result
   
a=3
print factorial(a)
