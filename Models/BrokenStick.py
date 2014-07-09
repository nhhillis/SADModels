from __future__ import division
import sys                                            
import numpy as np
from random import randrange
import math
import random



'''def BrokenStick(N, S, sample_size):

    """This script codes Broken Stick models """ # playing around with this 
    #N = number of individuals
    #S = number of species
    #sample_size = number of rank abundance vectors to be generated'''
'''just some thoughts on how to make this work.  Create list of range of N, then make S - 1 random divisions in range of N, repeat sample_size times.'''
#i now have values that represent divisions in N not the number of individuals in each species

N = 20
S = 4
sample_size = 10

n = range(N) # creates range of N 
print n
s = S-1 #number of divisions(species minus 1)

cuts = random.sample(set(n), s) #randomly selecting s number of items in range 
cuts.sort(reverse = True) #sorts numbers
print cuts #gives where the range is split 
