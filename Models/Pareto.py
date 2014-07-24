from __future__ import division
import sys                                            
import numpy as np
from random import randrange, choice
import scipy.stats


'''This script codes the Pareto Model'''


def SimPareto(N, S, sample_size, integer=False):
    
    sample = []
    
    for i in range(sample_size): 
        
        
        RAC = [0.8*N, 0.2*N]
        
        while len(RAC) < S:
            ind = randrange(len(RAC))
            v = RAC.pop(ind)
            v1, v2 = [0.8 * v, v - 0.8 * v]
            RAC.extend([v1, v2])       
                        
        if integer == True:    
            if sum(RAC) !=N or len(RAC) != S:
                print 'Incorrect N and S: N=',sum(RAC),' S=', len(RAC)
                sys.exit()
        elif integer == False:
            if len(RAC) != S:
                print 'Incorrect S:', len(RAC)
                sys.exit()
        else: 
            print 'Integer values need to be either \'False\' or \'True\''
            sys.exit()
       
        RAC.sort(reverse = True)
        sample.append(RAC)
    
    return sample

print SimPareto(10,5,5)