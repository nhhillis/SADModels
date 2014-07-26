from __future__ import division                                        
import numpy as np
import random


def AvgShape(RACs):
    """ Find the SAD in a random sample with the greatest average commonness 
        among its ranked abundance states. This SAD is taken to represent the 
        central tendency of the set, based on the SAD shape. """
    
    if len(RACs) > 500:
        RACs = random.sample(RACs,500)
    
    N = sum(RACs[0])
    S = len(RACs[0])
    a1 = 0 # mean of overlap of the ranks
    v1 = 0 # variance in overlap of ranks
    
    for RAC in RACs: # for a RAC in the list of RACs
        in_common = [] # the number of times that each value of the ranks
                            # in the reference RAC is found in the other RACs
        ct1 = 0 # the index we are looking at
        
        for a in RAC: # for each value at each rank in reference RAC
            c = 0 # number of common values
            
            for RAC1 in RACs: # selecting which RAC will be compared to reference
                if a == RAC1[ct1]: # if value of the rank = the value at the index[ct1]
                    c += 1 
           
            in_common.append(np.log(c)) #  Transforming C to not give unequal weights to large numbers
            ct1 += 1 # this changes the index we are looking at
        
        a2 = np.mean(in_common) #find mean of in_common
        v2 = np.var(in_common)  #find variance of in_common
        
        if a2 > a1: # if our new mean is higher than previous mean
            a1 = a2 # assigns new average to a1
            v1 = v2 # assigns new variance to v1
            xRAC = RAC
        
        elif a2 == a1: # if the means are the same, use variance
            if v2 < v1: # if new variance is lower than previous ...
                a1 = a2 # assigns new average to a1
                v1 = v2 # assigns new variance to v1
                xRAC = RAC
        
    if sum(xRAC) != N and len(xRAC) != S:
        print 'Sum of RAC and/or length of RAC not equal to starting N and S'
    
    return xRAC
    

    