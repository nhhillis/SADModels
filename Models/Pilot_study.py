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

sys.path.append(mydir + 'Models/')
import Models 

'''This code will obtain observed and predicted SADs(1000) for each model.  Then create a new 
file for each model that contains Survey Date, Site, Species, Observed AB and average Predicted AB.

- As of now, need to call model functions instead of copying them (fixed this)
- Need to add check in getsample() that keeps it from drawing same SAD (Remove SAD from list once selected)
- Set up data so that it will work properly
- Pull data in without CSV module'''

###################################################################   
'''Function to read in a .CSV file and to reorder for SAD''' # this will not be needed

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
        prdSAD = AvgShape(Models.SimLogNormInt(N, S, sample_size)) #Get average shape of SLN
        prdSADs.append(prdSAD)
        #print prdSAD
        
    return prdSADs

###################################################################

'''Function to obtain N from SADs in sample''' # Not sure if this is needed but I am leaving it in

def get_N(SADs):#Returns the Ns for the sample
    N = []
   
    while len(N) < len(SADs):
        for sad in SADs:
            N.append(sum(sad))
   
    return N

###################################################################
'''Function to obtain S from SADs in sample''' # Not sure if this is needed but I am leaving it in 

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

#Samples = get_samples(SADs, 6) #Number of samples to use (Add check against redundent SADs)


PredSAD = get_predx(SADs, 100) #Get predicted SAD for the sample, second input is number of times to run simlognorm

print 'Predicted Samples Number = ', len(PredSAD)
print("\n") 
print 'Number of ObsSADs = ', len(SADs)
print("\n") 
print 'Ns = ', Ns, 
print("\n") 
print 'Ss = ', Ss
print("\n") 
print 'LogNorm Prediction = ', PredSAD
print("\n") 
print 'Observed SADs = ', SADs