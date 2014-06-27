from __future__ import division
import sys                                            
import numpy as np
from random import randrange
import math
import random

"""This script codes lognormal models """

""" N = Total abundance #copied from RandFrac_1 
    S = Number of Species (Total Abundance)
    sample_size = Sample Size"""
    
'''def broken_stk(N, S, sample_size): 
    RAC_samples = []
    while len(RAC_samples) < sample_size:
        RAC = [N]
        
        while len(RAC) < S:'''

N = 20
S = 4
sample_size = 10
            
 #something i found on stack overflow to generate a list of random numbers summing to 1, now just trying to figure out how to change what they sum up to.
RAC = [] 
s = 0
for i in range(N):
    r = random.random()
    s += r
    RAC.append(r)
print RAC #this gives me random float numbers 



for i in range(sample_size): # this is giving me just random nums between 0 and N, but not sure how to figure out how to make them sum to N
    print random.randrange(0, N, 1)



RAC = [] #this gives me S random divisions of N but haven't yet figured out how to make sure they sum to N
for i in xrange(S-1):
    maxSize = math.ceil(N/(S - len(RAC)))
    newSize = random.randint(0, maxSize)
    n = N - newSize
    RAC.append(newSize)
RAC.append(n)
print RAC     
            
