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
        RAC = [N*.75,N*.25]
        
        while len(RAC) < S:
            x = choice(RAC)
            new1 = x * .75
            new2 = x * .25
            RAC.append(x)
            RAC.append(new1)
            RAC.append(new2)
            print RAC
        sample.append(RAC)
        
sample = SimLogNorm(20, 5, 10)
print sample


