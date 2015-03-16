from __future__ import division
import csv
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
import math
import sys
import os
from scipy import stats

mydir = os.path.expanduser("~/GitHub/SADModels/") # A general file path; this means that:
# 1.) You will need to create a GitHub directory in your home directory
# 2.) Move SADModels into the GitHub directory

sys.path.append(mydir + "Analysis")

#from AverageShape import AvgShape

sys.path.append(mydir + 'Models/')
import Models

'''This code will do the following
1. Obtain observed SADs for ...
2. For each observed SAD, obtain predicted SADs for each model.
3. Write data to an "obs_pred.txt" file; with a different file for each model
    Each obs_pred.txt file will have these rows: Date, Site, Species, ObsAb, PredAB
'''

'''
- As of now, need to call model functions instead of copying them (fixed this)
- Add test functions, e.g. check that the same SAD isn't drawn twice; sample w/out replacement
- Set up data so that it will work properly --yes, but needs clarification
- read observed sad data from .txt or .csv files.
'''

###################################################################
'''Gets obsSAD from data set'''

#Use dictionaries and loop


#Based on KJL code, working now to make it run

def get_ObsSADs():
    DATA = '/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt'
    mydict = {}
    with open(DATA) as i:
        for d in i:
            if d.strip():
                d = d.split()
                species = d[0]
                abundance = float(d[3])
                if abundance > 0:
                    if species in mydict:
                        mydict[species].append(abundance)
                    else:
                            mydict[species] = [abundance]
    SADs = []
    SADlist = mydict.items()
    for tup in SADlist:
        SAD = tup[1]
        if len(SAD) >= 1:
            SAD.sort()
            SAD.reverse()
            SADs.append(SAD)
    return SADs
print get_ObsSADs()

###################################################################
'''Gets predicted average SAD for sample'''

'''def get_predx(SADs, sample_size, model): #Inserted model in here so the model could be specified
    prdSADs=[]#list of predicted SLN average SADs

    for sad in SADs:
        N = sum(sad)
        S = len(sad)
        prdSAD = AvgShape(Models.model(N, S, sample_size)) #Get average shape of predicted SAD
        prdSADs.append(prdSAD)
        
        #What foll
        if model == 'SimBrokenStick':  #Think this might be the best way
            predRAD = 
            
        elif model == 'DomPreInt':
            predRAD = 
            
        elif model == 'DomPreFloat':
            predRAD = 
            
        elif model == 'SimLogNormInt':
            predRAD = 
        
        elif model == 'SimLogNormFloat':
            predRAD = 
        
        elif model == 'SimParetoFloat':           
            predRAD = 
        
        elif model == 'SimParetoInt':
            predRAD = 
        
        elif model == 'Sample_SimpleRandomFraction':
            predRAD = 
        
        elif model == 'DomDecayFloat':
            predRAD = 
        
        elif model == 'DomDecayInt':
            predRAD = 

    return prdSADs
'''
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
