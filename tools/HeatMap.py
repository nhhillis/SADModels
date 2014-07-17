from __future__ import division
import sys                                            
import numpy as np
from random import randrange, choice
import scipy.stats
import matplotlib.pyplot as plt



'''This file contains attempts to generate heat maps from expected RACs'''
# This is a work in progress
# Need to find function that creates heat maps


def SimLogNorm(N, S, sample_size, integer=False): #Using this function to generate
                                                #RACs to plot
    
    sample = []
    
    for i in range(sample_size): 
        
        
        RAC = [0.75*N, 0.25*N]
        
        while len(RAC) < S:
            ind = randrange(len(RAC))
            v = RAC.pop(ind)
            v1, v2 = [0.75 * v, v - 0.75 * v]
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
       
        plt.plot(RAC)  #plots RACs in a pretty graph
        plt.show()     #need to find average of these lines
                        #Have yet to find out to plot this
        
        
        
    
    return sample
    
        
        
sample = SimLogNorm(1000, 50, 50)


