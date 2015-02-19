import csv
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
import math
import sys
import os
mydir = os.path.expanduser("~Nathan_Hillis/SADModels/")
sys.path.append(mydir + "Analysis")
from AverageShape import AvgShape
from AverageShape import PlotAvgShape
sys.path.append(mydir + 'tools/')
import HeatMap

'''Comparing Obsd SADs to SimLogNorm.  
This code contains functions for reading in CSV files and obtaining predictied Avg LogNorm SADs
getting N and S.  I am currently working on a function that will get samples from a larger data set and
a function to graph the samples with LogNorm heat map, AvgLogNorm and observed'''

def SimLogNorm(N, S, sample_size):
    
    RACs = []  # 'sample' is a function. You don't want to give variables the same name as a function 
    
    while len(RACs) < sample_size:
        RAC = [N] #Initial 
        while len(RAC) < S:
            ind = randrange(len(RAC))
            v = RAC.pop(ind) # Removes randomly selected number from list RAC
            v1 = int(round(0.75 * v)) # split 75:25
            v2 = v - v1  # force all abundances to be integers 
            
            if v1 < 1 or v2 < 1: break # force min(RAC) to be > 1
                                            
            RAC.extend([v1, v2]) # add new values to RAC, increaseing len(RAC) by 1
            
        if len(RAC) == S and sum(RAC) == N: # When conditions are met sort and append
            RAC.sort()
            RAC.reverse()
            RACs.append(RAC)
            #print len(RAC)
            
    return RACs

###################################################################   

def read_csv(filepath):
    SADs = []
    
    with open(filepath, 'U') as csvfile:
        reader = csv.reader(csvfile)
    
        for row in reader:  
            SAD = [int(i) for i in row]
            SAD.reverse()
            SADs.append(SAD)
            
    return SADs

###################################################################

def get_predx(SADs):
    prdSADs=[]#list of predicted SLN average SADs 
   
    for sad in SADs:   
        N = sum(sad)
        S = len(sad)
        sample_size = 100
        prdSAD = AvgShape(SimLogNorm(N, S, sample_size)) #Get average shape of SLN
        prdSADs.append(prdSAD)
        #print prdSAD
        
    return prdSADs

###################################################################

'''def graph_SAD(SADs):
    for sad in SADs:
        rank = range(len(sad))
        sad = np.log(sad)
        plt.plot(rank, sad) 
    plt.show()'''

###################################################################

def get_N(SADs):
    N = []
   
    while len(N) < len(SADs):
        for sad in SADs:
            N.append(sum(sad))
   
    return N

###################################################################

def get_S(SADs):
    S = []
   
    while len(S) < len(SADs):
        for sad in SADs:
            S.append(len(sad))
  
    return S

###################################################################           

def get_samples(SADs, NumSamples):
    Samples = []
    while len(Samples) < NumSamples:
        samp = choice(SADs) #Randomly choose sample
        Samples.append(samp)
    print 'Samples', Samples
    return Samples

###################################################################           

SADs = read_csv('/Users/Nathan_Hillis/Dropbox/Nathan_Hillis/Data/Sample_data.csv')

Ns = get_N(SADs)
Ss = get_S(SADs)

Sample_size = 100
Samples = get_samples(SADs, 4)

RACs = get_predx(Samples)
print 'LogNorm', RACs

'''print 'Ns = ', Ns
print 'Ss = ', Ss
print 'Observed = ', SADs
print 'LogNorm Prediction = ', RACs'''




'''fig = plt.figure()
title = 'Pilot Study'

ax = fig.add_subplot(3, 3, 1)
RACsample = SimLogNorm(len(SADs[0]), sum(SADs[0]), 100)
fig = HeatMap.RACHeatMap(fig, RACsample)
fig = PlotAvgShape(fig, RACsample)

plt.title('Broken Stick', fontsize = 13)
plt.xlabel('Rank')
#plt.ylabel('Abundance')
plt.ylabel(title)

print 'finished broken stick\n'''''