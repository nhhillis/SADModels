import numpy as np
'''Testing methods for converting logAB to AB. 
Not sure values are correct yet.  np.log may be the wrong function.'''

a = np.random.lognormal(mean=10, sigma = 8, size =10)
a.sort()
print a

b = []
for i in a:
    w = np.log(i)
    b.append(w)
    b.sort()

print b
print np.std(b),'STD'
print np.mean(b), 'Mean'