from __future__ import division
import sys                                            
import numpy as np
from random import randrange
import math # delete if you it's not sued
import random
import itertools
import matplotlib.pyplot as plt
from matplotlib import patches, path # import multiple methods from the same module




""" This file contains code to generate either random samples of simple random
    fraction models. Everything in here is a function or a class of functions"""


def SimpleRandomFraction_Sample(N, S, sample_size):
    
    RAC_samples = [] # this is a list of RACs, and each RAC is a list   ...a list of lists            
    while len(RAC_samples) < sample_size:
    
        RAC = [N]
        
        while len(RAC) < S:
            
            sp1_ab = random.choice(RAC) # pick a species abundance at random
            if sp1_ab == 0:
                print 'you\'re model stick sucks. fix your bug'
                sys.exit()
                
            if sp1_ab == 1:
                continue # this is a control statement
                
            sp2_ab = randrange(1, sp1_ab) # pick a random number (abundance) between 1 and sp1_ab - 1, inclusive
            sp1_index = RAC.index(sp1_ab) # index in the RAC of the species we picked
            RAC[sp1_index] = sp1_ab - sp2_ab # decrease its abundance according to sp_ab
            
            RAC.append(sp2_ab)
            RAC.sort(reverse = True)  #sorts RAC's in decending order to aid in graphing
        RAC_samples.append(RAC) # appending a list (i.e. an RAC) to another list
       

    return RAC_samples
    


def SimpleRandomFraction_Single(N, S, sample_size): # Find and return the 'average' form
    AvgSAD = []

    return AvgSAD




'''def logNormal_random_fraction(N, S, sample_size):
    
    pass
    
    return
    



def get_expectedRAC(N, S, size, algorithm ):
    
    if algorithm == 'simple random fraction':
        RACsample =  simple_random_fraction(N, S, sample_size)
        

def get_sample(N, S, size, algorithm)



def get_heatmap_data(N, S,....)'''

