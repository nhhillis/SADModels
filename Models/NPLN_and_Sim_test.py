import numpy as np
'''Testing methods for converting logAB to AB. 
Not sure values are correct yet.  np.log may be the wrong function.'''
import sys
import os
mydir = os.path.expanduser("~Nathan_Hillis/SADModels/")
sys.path.append(mydir + "Analysis")

from AverageShape import AvgShape

def test(mean, sigma, size, sample_size):
    RAClst = []
    while len(RAClst) < sample_size:
        a = np.random.lognormal(mean, sigma, size)
        print a
        b = []
        for i in a:
            c = np.log(i)
            b.append(c)
            b.sort()
        
        RAClst.append(b)
        print np.std(b),'STD'
        print np.mean(b), 'Mean'   
        
    return RAClst

test = test(100, 50, 10, 10)
print test
print "AVG"
print AvgShape(test)
