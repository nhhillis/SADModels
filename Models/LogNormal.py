from __future__ import division
import sys                                            
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
from matplotlib import patches, path
import scipy.stats
'''This script codes the LogNormal Models'''

# To code the LogNormal...each division is 75:25 
# Still working on this...numbers are not properly summing to N yet
# Getting proper number of divisions but whole thing is yet to come together



def SimLogNorm(N, S, sample_size, integer=False):
    
    for i in range(sample_size): # This is where the RACs are accumulated
        
        sample = []
        RAC = [0.75*N, 0.25*N]
        
        while len(RAC) < S: # This is where the RACs are built
            
                
                
                        
            
        if integer == True:    
            if sum(RAC) !=N or len(RAC) != S:
                print 'Incorrect N and S: N=',sum(RAC),' S=', len(RAC)
        elif integer == False:
            if len(RAC) != S:
                print 'Incorrect S:', len(RAC)
        else: 
            print 'Integer values need to be either \'False\' or \'True\' 
            
         
       
    
        print sample
    
samples = SimLogNorm(8, 4, 5)


