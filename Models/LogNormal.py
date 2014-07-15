from __future__ import division
import sys                                            
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
from matplotlib import patches, path

'''This script codes the LogNormal Models'''

# To code the LogNormal...Get distribution, divide into octaves, plot log
# Still working on this...


def SimLogNorm(N, S, sample_size):
    RAC = []
    RACs = []
    
    while len(RACs) < sample_size:
        
        

N = 20
S = 5
sample_size = 5
sample = SimLogNorm(20, 5, 10)