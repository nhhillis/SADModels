import numpy as np
'''Testing methods for converting logAB to AB. 
Not sure values are correct yet.  np.log may be the wrong function.'''

def test(sample_size):
    RACs = []
    while len(RACs) < sample_size:
        a = np.random.lognormal(mean=10, sigma = 5, size =10)
        b = []
        for i in a:
            w = np.log(i)
            b.append(w)
            b.sort()
        RACs.append(b)
        print np.std(b),'STD'
        print np.mean(b), 'Mean'   
    return RACs
            
print test(1)

