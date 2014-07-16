from __future__ import division
import sys                                            
import numpy as np
from random import randrange
import math
import random
import matplotlib.pyplot as plt

"""This script codes Broken Stick models for species abundance distribution.
    These are generally conceived as models for how species partition a niche
    dimension or shared and limited resource. -KL 
    
    Task: Nathan contribute one or two nice sentences. """
    
     
def SimBrokenStick(N, S, sample_size):
    
    """
    A function to generate random samples of the simultaneous Broken Stick Model
    of MacArthur 1957 or 1961. We need the actual citation.
        
    N  :  Total abundance, i.e., number of individuals
    S  :  Species richness, i.e., number of species
    sample_size  :  number of rank-abundance vectors to generate
    
    How this model works.  Create list of range of N, then make S - 1 random 
    divisions in range of N, repeat sample_size times. So, first we have to get
    our indices. Which you've figured out. Then, we can split a list of N 1's at
    those indices points. A few rules apply, e.g. 0 can't be one of the indices.
    Say the simultanesouly drawn indices are [2, 9, 5]. Here, simultaneous means
    those numbers were drawn without replacement, i.e., were not allowed to
    can't draw any number twice. Once you sort those numbers then you can...
    
    Hint: Let N = 15, S = 4, and SortedIndices = [2, 5, 9]
    So: oo|ooo|oooo|oooooo  = [2, 3, 4, 6] -> N = 15 and S = 4
    2-0 = 2  :  5-2 = 3  :  9-5 = 4  :  15-9 = 6
    
    """    

    
    RACs = []
    RAC = []
    
    while len(RACs) < sample_size:
        
        cuts = random.sample(range(N), S-1) # This is a time costly operation
                                            # We want something faster                       
        cuts.sort()
        RAC = [cuts[0]]
        
        sp_ab = float()
        cut = float()
        for i, cut in enumerate(cuts):    
            if i == 0:
                continue
            
            sp_ab = cut - cuts[i-1]
            RAC.append(sp_ab)
        
        RAC.append(N - cut) 
        RAC.sort(reverse = True)    
        RACs.append(RAC)
        
        print RACs
        
        for _list in RACs:
            if sum(RAC) !=N or len(RAC) != S:
                print 'Incorrect N and S: N=',sum(RAC),' S=', len(RAC)
        
    return RACs 
    