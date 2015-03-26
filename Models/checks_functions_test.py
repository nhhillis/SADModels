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
    failNS = [0]
    
    while len(sample) < sample_size: 
        RAC = [0.8*N, 0.2*N]
        
        while len(RAC) < S:
            ind = randrange(len(RAC))
            v = RAC.pop(ind)
            v1 = int(round(0.8 * v))
            v2 = v - v1  # forcing all abundance values to be integers
            
            if v1 < 1 or v2 < 1: 
                
                for i in fail: #everytime a sad fails this condition
                    newfail = fail[0] + 1   #count of fails
                    fail.pop(0) #remove old fail count
                    fail.append(newfail) #add new count to fail
                
                newNS = [N, S] #defines the n/s fail combo
                failNS.pop(0)
                failNS.append(newNS) #add NS of failed combo
                break  # forcing smallest abundance to be 
                                        # greater than one
            RAC.extend([v1, v2])       
                        
        if len(RAC) == S and sum(RAC) == N:        
            RAC.sort(reverse = True)
            sample.append(RAC)
    
    if rel == True: sample = GetRelAbs(sample) 
   
    sample.append(failNS) #adds the failed N/S combos to sample
    sample.append(fail) #adds the failed count to sample, 
                                #failed N/S and fail count will be removed by get_fail function
    return  sample
    
 
def SimLogNormInt(N, S, sample_size, rel=False):
    '''This script codes the Lognormal Model'''
    
    sample = []
    fail = [0]
    failNS = [0]
    while len(sample) < sample_size:
        
        n = int(round(0.75 * N))
        RAC = [n, N - n]
        
        while len(RAC) < S:
            
            ind = randrange(len(RAC))
            v = RAC.pop(ind)
            v1 = int(round(0.75 * v)) 
            v2 = v - v1   # forcing all abundance values to be integers
            
            if v1 < 1 or v2 < 1: 
               
                for i in fail:
                    newfail = fail[0] + 1    
                    fail.pop(0)
                    fail.append(newfail)
                
                newNS = [N, S]
                failNS.pop(0)
                failNS.append(newNS)
                break  # forcing smallest abundance to be 
                                        # greater than one
            RAC.extend([v1, v2])
        
        if len(RAC) == S and sum(RAC) == N:
            RAC.sort()
            RAC.reverse()
            sample.append(RAC)
    
    if rel == True: sample = GetRelAbs(sample)       
   
    sample.append(failNS)
    sample.append(fail)
    return sample  

def DomPreInt(N, S, sample_size, rel=False): # Works only with positive integers
    '''This script codes Tokeshi's Dominance Preemption Model
    this code does not work well with small N or high S.
    This model is not practical for species richness of greater than 10'''
    sample = [] # A list of RACs
    fail = [0]
    failNS = [0]   
    
    while len(sample) < sample_size: # number of samples loop     
        RAC = [] #RAC is a list
        sp1 = randrange(int(round(N *.5)), N) #Rand select from N to N(.5)
        ab1 = N - sp1
        RAC.extend([sp1, ab1])
        
        while len(RAC) < S:
            ab2 = RAC.pop()
            
            if ab2 < S - len(RAC) or ab2 < 2:
                
                for i in fail:
                    newfail = fail[0] + 1    
                    fail.pop(0)
                    fail.append(newfail)
            
                newNS = [N, S]
                failNS.pop(0)
                failNS.append(newNS)
                break
                
            sp2 = randrange(int(round(ab2*.5)), ab2)
            RAC.extend([sp2, ab2-sp2])

        if len(RAC) == S and sum(RAC) == N:
            sample.append(RAC)
    
    if rel == True: sample = GetRelAbs(sample)    
   
    sample.append(failNS)
    sample.append(fail)
    return sample
    
    
def DomDecayInt(N, S, sample_size, rel=False): # Works only with positive integers    ...if you think about it, there can never be two 1's
    '''This model randomly divides N into 2 sections, then the largest section of N is then
    divided at random.  This continues until there are S divisions. This model
    returns only integer values.'''
    
    sample = [] # A list of RACs
    fail = [0]
    failNS = [0]   
    
    while len(sample) < sample_size: # number of samples loop     
        
        RAC = [] #RAC is a list
        sp1 = randint(1, int(round(N*.5)))
        ab1 = N - sp1
        RAC.extend([sp1, ab1]) 
        
        while len(RAC) < S:
            
            if min(RAC) < 2: 
                 
                 for i in fail:
                    newfail = fail[0] + 1    
                    fail.pop(0)
                    fail.append(newfail)
                
                 newNS = [N, S]
                 failNS.pop(0)
                 failNS.append(newNS)
                 break
            
            ab2 = RAC.pop()
            sp2 = randint(1, int(round(ab2 * .5)))
            RAC.extend([sp2, ab2 - sp2])

        if len(RAC) == S and sum(RAC) == N:
            RAC.sort(reverse = True)
            sample.append(RAC)
     
    if rel == True: sample = GetRelAbs(sample)     
    sample.append(failNS)
    sample.append(fail)
    return sample
    
def get_fail(SAD, sample_size):
    '''This function pulls the number of fails and failed N/S
    combos out of the SAD that is returned from models.py'''

    fail = [] # number of fails
    failNS = [[0]] # n/s combo that failed
   
    while len(SAD) > sample_size:
        x = SAD.pop() # pull count of fails
        y = SAD.pop() #pull failed n/s combo 
      
        for i in failNS:
            if i != y: # if n/s combo is not in list 
                failNS.append(y) # add n/s combo
      
        fail.append(x) #add count of fails
        #print 'fail #', fail, 'Failed NS', failNS
        print 'Fail #', fail
        print 'Fail Combo' , failNS
    if len(fail) == 0: # if there is no fails
        print 'none failed'

    
    print 'length', len(SAD)
    #print 'SAD',SAD
    return SAD, fail, failNS
    
    
    
N = 1000
S = 10
sample_size = 10

print '#1 - SLN'
get_fail(SimLogNormInt(N, S, sample_size, rel=False), sample_size)
print '#2 - Pareto'
get_fail(SimParetoInt(N, S, sample_size, rel=False), sample_size)
print '#3 - DomPre'
get_fail(DomPreInt(N, S, sample_size, rel=False), sample_size)
print '#4 - DomDec'
get_fail(DomDecayInt(N, S, sample_size, rel=False), sample_size)



