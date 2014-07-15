from __future__ import division
import sys                                            
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
from matplotlib import patches, path
import scipy.stats
'''This script codes the LogNormal Models'''

# To code the LogNormal...each division is 75:25 
# Still working on this...numbers are not properly summing to N yet
# Getting proper number of divisions but whole thing is yet to come together


def SimLogNorm(N, S, sample_size):
    
    for i in range(sample_size):
        
        sample = []
        RAC = []
        
        while len(RAC) < S:
            
            sp1 = N * .75
            RAC.append(sp1)
            sp2 = N * .25
            RAC.append(sp2)
            sp3 = choice(RAC) * .75
            RAC.append(sp3)
            sp4 = sp3 * 1/3
            RAC.append(sp4)
            #print RAC
            
        sample.append(RAC)
    
        print sample
    
samples = SimLogNorm(8, 4, 5)


