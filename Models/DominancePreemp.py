from __future__ import division
import sys                                            
import numpy as np
from random import randrange, randint, uniform

'''This script codes Tokeshi's Dominance Preemption Model
this code does not work well with small N or high S'''

def DomPreInt(N, S, sample_size): # Works only with positive integers
    sample = [] # A list of RACs
   
    while len(sample) != sample_size: # number of samples loop     
        RAC = [] #RAC is a list
        sp1 = randrange(int(N *.5), N) #Rand select from N to N(.5)
        ab1 = N - sp1
        RAC.extend([sp1, ab1]) 
        
        while len(RAC) < S:
            ab2 = RAC.pop()
            if ab2 < S - len(RAC):
                break
            sp2 = randrange(int(ab2*.5), ab2)
            RAC.extend([sp2, ab2-sp2])

        if len(RAC) == S and sum(RAC) == N:
            sample.append(RAC)
        else:
            print len(RAC), sum(RAC)
        
    return sample
    

def DomPreFloat(N, S, sample_size):#Works with decimal values
    sample = [] # A list of RACs
   
    for i in range(sample_size):     
        RAC = []
        sp1 = uniform((N *.5), N) 
        ab1 = N - sp1
        RAC.extend([sp1, ab1])
       
        
        while len(RAC) < S:
            ab2 = RAC.pop()
            sp2 = uniform((ab2*.5), ab2)
            RAC.extend([sp2, ab2-sp2])
            
    	sample.append(RAC)
        
    return sample
    
