from __future__ import division                                        
import matplotlib.pyplot as plt
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
    a1 = 10**10 # assume an initially high average difference among ranks 
    v1 = 0 # variance in overlap of ranks
    
    xRAC = list()
    for RAC in RACs: # for a RAC in the list of RACs
        AvgDiffAcrossRanks = [] # the number of times that each value of the ranks
                            # in the reference RAC is found in the other RACs
        
        for i, ab in enumerate(RAC): # for each value at each rank in reference RAC
            
            diff = 0 # 
            for RAC1 in RACs: # selecting which RAC will be compared to reference
                ab1 = RAC1[i] # the abundance value at the index[i] of RAC1
                diff += np.abs(ab1 - ab)/S # absolute difference between reference and querry RACs, divided by S....yields avg absolute difference at a given rank
                
            AvgDiffAcrossRanks.append(np.log(diff)) #  Transforming C to not give disproportionate weight to large numbers
            
        a2 = np.mean(AvgDiffAcrossRanks) #find mean of in_common
        v2 = np.var(AvgDiffAcrossRanks)  #find variance of in_common
        
        if a2 < a1: # if our new mean is lower than the previous mean
            a1 = a2 # assigns new average to a1
            v1 = v2 # assigns new variance to v1
            xRAC = RAC
        
        elif a2 == a1: # if the means are the same, use variance
            if v2 < v1: # if new variance is lower than previous ...
                a1 = a2 # assigns new average to a1
                v1 = v2 # assigns new variance to v1
                xRAC = RAC
        
    #if sum(xRAC) != N and len(xRAC) != S:
    #    print 'Sum of RAC and/or length of RAC not equal to starting N and S'
    
    return xRAC
    

    
    
def PlotAvgShape(fig, sampleRACs):
    
    avgRAC = AvgShape(sampleRACs)
    ranks = range(1, len(avgRAC)+1)
    plt.plot(ranks, np.log(avgRAC), lw=1, color='Lime')
    return fig
    
    
    
    
    