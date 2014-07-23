from __future__ import division
import sys                                            
import numpy as np
import random 

'''This script codes Tokeshi's Dominance Preemption Model'''
#To Code the DPM: 1st species = random selection between .5 and 1
# of N, add species one to RAC, randomly select .5 and 1 of remaining N, 
# and until S is satisified
'''Currently this code has a bug.  It is not returning the sample and
the RAC is not properly summing to N.
Also, I realize this could probably be cut down to fewer lines of code'''

def DomPre(N, S, sample_size):
    sample = [] # A list of RACs
   
    for i in range(sample_size): # number of samples loop     
        RAC = [] #RAC is a list
        sp1 = random.uniform((N *.5), N) #Rand select from N to N(.5)
        ab1 = N - sp1
        RAC.append(ab1)
        RAC.append(sp1)  
        
        while len(RAC) < S:
            ab2 = min(RAC)
            sp2 = random.uniform((ab2*.5), ab2)
            RAC.append(sp2)#original N not the new in
            RAC.sort(reverse = True)
            
        return RAC
    	sample.append(RAC)
        
    return sample
    
trial = DomPre(10000,10,2)
print sum(trial), len(trial), trial
