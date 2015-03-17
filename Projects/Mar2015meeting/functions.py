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

sys.path.append(mydir + "tools")
from AverageShape import AvgShape

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


#Working now, need to make sure data is in Unicode (UTF-8)
#This was causing the problem

def get_ObsSADs():
    DATA = '/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt'
    mydict = {}
    count = 0
    with open(DATA) as i:
        for d in i:
            count += 1
            print count
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


###################################################################
'''Gets predicted average SAD for sample'''

def get_predx(SADs, sample_size): #Inserted model in here so the model could be specified
    prdSADs=[]#list of predicted SLN average SADs 
    count = 0
    for sad in SADs:
        count += 1
        print 'pred -', count
        N = sum(sad)
        S = len(sad)
        prdSAD = AvgShape(Models.SimLogNormInt(N, S, sample_size)) #Get average shape of predicted SAD
        prdSADs.append(prdSAD)
    return prdSADs
        

###################################################################
'''Function to pull samples from large data set.
Need to do this so that same SAD is not selected twice.'''

def get_samples(SADs, NumSamples):

    Samples = []

    while len(Samples) < NumSamples:
        
        samp =choice(SADs) #Randomly choose sample
        SADs.remove(samp)
        Samples.append(samp)

    print 'Samples', Samples
    return Samples
###################################################################

OBS = get_ObsSADs()
print 'OBS ', OBS[0]
sample = get_samples(OBS, 10)
pred = get_predx(sample, 100)
print pred