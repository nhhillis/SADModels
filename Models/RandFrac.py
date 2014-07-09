from __future__ import division
import sys                                            
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
from matplotlib import patches, path # import multiple methods from the same module


""" This file contains code to generate either random samples from simple random
    fraction models. Everything in here is a function or a class of functions"""


def Sample_SimpleRandomFraction(N, S, sample_size):
    
    """ 
    This function randomly and sequently splits N into two integers by
    starting with a vector where N is the only value, i.e. N, and then splitting
    N into two positive integers at random, [N] -> [x1, x2], where x1+x2 = N.
    The function then draws one of the integers at random from the new vector
    (having 2 values), and then splits the integer into two other integers. 
    At this point, the vector has three values [x1, x2, x3], where x1+x2+x3 = N.  
    This process keeps on until there are a number of integers equal to S.
    
    N  :  total abundance; number of individuals in the community
    S  :  species richness; number of species in the community
    sample_size  :  number of random rank-abundance vectors to generate    
    """
    
    sample = []
    for i in range(sample_size):
        RAC = [N]
        
        while len(RAC) < S:
                
            sp1_ab = choice(RAC) # pick a species (i.e. vector value) abundance at random
            if sp1_ab == 0:
                print 'you\'re model has a bug'
                sys.exit()
                
            if sp1_ab == 1:
                continue # this is a control statement to prevent the program
                # from encountering an impossible conditions, i.e., dividing 1
                # at random into two positive integers
                
            sp2_ab = randrange(1, sp1_ab) # pick a random number (abundance) between 1 and sp1_ab - 1, inclusive
            sp1_index = RAC.index(sp1_ab) # index in the RAC of the species we picked
                
            RAC[sp1_index] = sp1_ab - sp2_ab # decrease its abundance according to sp_ab
            RAC.append(sp2_ab)
            
        RAC.sort(reverse = True)  #sorts RAC's in decending order to aid in graphing. 
        #Ken: Nice job. But it was in a loop that caused it to be repeated w/out need.
        
        sample.append(RAC) # appending a list (i.e. an RAC) to another list
        
    return sample
    


def Expected_SimpleRandomFraction(N, S, sample_size): # Find and return the 'average' form
    
    """ 
    This function obtains a sample of random rank-abundance vectors and then 
    finds the average of them all. Nathan, think about how this might be done!
    """
    
    sample = Sample_SimpleRandomFraction(100, 5, 4)
    print sample # print statement just to make sure the above function works.
    # Comment out this print statement if you don't want the sample printed to
    # your screen.
    
    AvgSAD = [float(sum(col))/len(col) for col in zip(*sample)]
    print AvgSAD
    #finds average for sample
    
    """ Need a function to find the average form of the SAD from the sample you
    obtained """
    
    return AvgSAD


Expected_SimpleRandomFraction(100, 4, 5)
