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
            chunks = []
            
            sp1 = N * .75 # divide N 75-25 and place into chunks list
            chunks.append(sp1)
            sp2 = N * .25
            chunks.append(sp2)
            
            sp3 = choice(chunks) * .75 #Choose one of the existing chunks to
            RAC.append(sp3)            #divide by 75.
            sp4 = sp3 * 1/3 #Find the 25% portion of the selected chunk
            RAC.append(sp4)
            #print RAC
            RAC.sort(reverse = True)
            
        
        sample.append(RAC)     
        for _list in sample:
            if sum(RAC) !=N or len(RAC) != S:
                print 'Incorrect N and S: N=',sum(RAC),' S=', len(RAC)
        
       
    
        print sample
    
samples = SimLogNorm(8, 4, 5)


