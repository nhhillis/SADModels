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
    
    RACs = []  # List of SimLogNorm RACs
    
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
'''Function to read in a .CSV file and to reorder for SAD'''

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
'''Gets predicted average LogNormal SAD for sample'''

def get_predx(SADs, sample_size):
    prdSADs=[]#list of predicted SLN average SADs 
   
    for sad in SADs:   
        N = sum(sad)
        S = len(sad)
        prdSAD = AvgShape(SimLogNorm(N, S, sample_size)) #Get average shape of SLN
        prdSADs.append(prdSAD)
        #print prdSAD
        
    return prdSADs

###################################################################
'''Function to graph SADs, as of now only plots to one graph. May not be of much use right now.
I want to graph each sample with a heat map of predicted and the average predicted.  Still not working
properly.'''

'''def graph_SAD(SADs, Title):
    for sad in SADs:
        rank = range(len(sad))
        sad = np.log(sad)
        plt.plot(rank, sad)
        plt.title(Title, fontsize = 13) 
        plt.xlabel('Rank')
        plt.ylabel('Abundance')
    plt.savefig('/Users/Nathan_Hillis/SADModels/figures/Pilot_Study/Pilot_Study_'+Title+'.png', dpi=None, facecolor='w', edgecolor='w',)    
    plt.show()'''
 
    

###################################################################
'''Function to obtain N from SADs in sample'''

def get_N(SADs):#Returns the Ns for the sample
    N = []
   
    while len(N) < len(SADs):
        for sad in SADs:
            N.append(sum(sad))
   
    return N

###################################################################
'''Function to obtain S from SADs in sample'''

def get_S(SADs): #Returns the Ss for the sample
    S = []
   
    while len(S) < len(SADs):
        for sad in SADs:
            S.append(len(sad))
  
    return S

###################################################################           
'''Function to pull samples from large data set.
Need to do this so that same SAD is not selected twice.'''

def get_samples(SADs, NumSamples):
    Samples = []
    while len(Samples) < NumSamples:
        samp = choice(SADs) #Randomly choose sample
        '''for i in Samples:
                if sum(samp) == sum(i):
                        break'''
        Samples.append(samp)
    print 'Samples', Samples
    return Samples

###################################################################           

SADs = read_csv('/Users/Nathan_Hillis/Desktop/Data/Sample_data.csv') # Will have to be changed to data location

Ns = get_N(SADs) #Get N
Ss = get_S(SADs) #Get S

Samples = get_samples(SADs, 6) #Number of samples to use
print 'Number of Samples', len(Samples)

PredSAD = get_predx(Samples, 100) #Get predicted SAD for the sample, second input is number of times to run simlognorm
print 'Predicted Samples Number', len(PredSAD)

#graph_SAD(PredSAD, 'PredSAD') # Graph Predicted SAD
#graph_SAD(Samples, 'ObsSAD') #Graph Observed SADs, Plot is coming out wrong

print 'Ns = ', Ns
print 'Ss = ', Ss
print 'LogNorm Prediction = ', PredSAD