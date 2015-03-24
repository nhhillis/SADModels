from __future__ import division
import sys                                            
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import scipy.stats                                       
from random import randrange, randint, uniform, seed, choice
def GetRelAbs(RACsample): # a function to transform abundance into relative abundances for many RACs
    
    RACs = []
    for RAC in RACsample:
        RAC = (np.array(RAC) / sum(RAC)) * 100 # operate on a numpy array (vector multiplication) get relative abundance of each species
        RACs.append(RAC.tolist()) # convert the array back to a list and append to RACs 
        
    return RACs


def SimParetoInt(N, S, sample_size, rel=False):
    '''This script codes the Pareto Model.  The divisions of N follow the 80:20
    rule.  The sections of N are selected at random for division. Returns only
    integer values.'''
    
    sample = []
    fail = [0]
    failNS = []
    while len(sample) < sample_size: 
        RAC = [0.8*N, 0.2*N]
        
        while len(RAC) < S:
            ind = randrange(len(RAC))
            v = RAC.pop(ind)
            v1 = int(round(0.8 * v))
            v2 = v - v1  # forcing all abundance values to be integers
            
            if v1 < 1 or v2 < 1: 
                for i in fail:
                    newfail = fail[0] + 1    
                    fail.pop()
                    fail.append(newfail)
                failNS.append([N, S])
                break  # forcing smallest abundance to be 
                                        # greater than one
            RAC.extend([v1, v2])       
                        
        if len(RAC) == S and sum(RAC) == N:        
            RAC.sort(reverse = True)
            sample.append(RAC)
    
    if rel == True: sample = GetRelAbs(sample) 
    sample.append(fail)
    return  sample
    
 
    
    
test =  SimParetoInt(1000, 10, 10, rel=False)
for i in test:
    if len(i) == 1:
        test.remove(i)
        print i
    
print test
