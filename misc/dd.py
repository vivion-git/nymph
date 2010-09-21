L = [1,2,3]
D = {'a':1, 'b':2}

A = L[:]              # instead of: A = L (or list(L))
B = D.copy()          # instead of: B = D
print A,B
A[1] = 'Ni'
B['c'] = 'spam'

print L, D

print A, B
