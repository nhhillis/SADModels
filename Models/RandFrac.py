from __future__ import division
import sys                                            
import numpy as np
from random import randrange
import math
from random import choice




""" This script does some stuff

    1. house functions for random fraction models
    2. return expected of random fraction models 
    
"""


def simple_random_fraction(N, S, sample_size):
    
    """ What this doesn't do:
    1. Currently is not callable by outside """

    
    RAC_samples = [] # this is a list of RACs, and each RAC is a list   ...a list of lists            
    while len(RAC_samples) < sample_size:
    
        RAC = [N]
        
        while len(RAC) < S:
            
            sp1_ab = choice.random(RAC) # pick a species abundance at random
            if sp1_ab == 0:
                print 'you\'re model stick sucks. fix your bug'
                sys.exit()
                
            if sp1_ab == 1:
                continue # this is a control statement
                
            sp2_ab = randrange(1, sp1_ab) # pick a random number (abundance) between 1 and sp1_ab - 1, inclusive
            sp1_index = RAC.index(sp1_ab) # index in the RAC of the species we picked
            RAC[sp1_index] = sp1_ab - sp2_ab # decrease its abundance according to sp2_ab
            
            RAC.append(sp2_ab)
            
        RAC_samples.append(RAC) # appending a list (i.e. an RAC) to another list
    
    # Get the average form from the set of random samples
    
    return RAC_samples
    
    N = 100
    S = 4
    sample_size = 100
    RAC_samples = simple_random_fraction(N, S, sample_size)

    print(RAC_samples)
    
    
    
'''def logNormal_random_fraction(N, S, sample_size):
    
    pass
    
    return
    



def get_expectedRAC(N, S, size, algorithm ):
    
    if algorithm == 'simple random fraction':
        RACsample =  simple_random_fraction(N, S, sample_size)
        

def get_sample(N, S, size, algorithm)



def get_heatmap_data(N, S,....)'''



    
