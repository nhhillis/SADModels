from __future__ import division
import csv
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
import math
import sys
import os
from scipy import stats
from itertools import izip

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

#Working now, need to make sure .text data is in Unicode (UTF-8)
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
                abundance = int(d[3])
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
'''This function is working with the small samples that I am using.  Need to run with entire dataset, 
but it will take a while'''

def get_predx(SADs, sample_size): #Removed Dom Pre Int, need to check for bugs
    
    SADModels = ['SimBrokenStick', 'SimLogNormInt', 'SimParetoInt', 'Sample_SimpleRandomFraction']
    
    for model in SADModels:
        
        if model == 'SimBrokenStick':
            print 'Writing Broken Stick Pred'
            count = 0            
            
            with open(mydir + "/Results/BrokenStickPred.txt", "w") as BS:
                for sad in SADs:
                    N = sum(sad) # Find Total Abundance
                    S = len(sad) # Find number of species
                    
                    prdSAD = AvgShape(Models.SimBrokenStick(N, S, sample_size)) #Get average shape of predicted SAD 
                    for i in prdSAD:
                            BS.write("%s\n" % i)
                        
                        #count += 1
                       # print count
                    
            print 'Broken Stick Pred Done'
            BS.close() 
                
     
                
        if model == 'SimLogNormInt':
            print 'Writing Sim Log Norm Pred'
            count = 0            
           
            with open(mydir + "/Results/SimLogNormPred.txt", "w") as SLN:
                for sad in SADs:
                    if len(sad) <= 1:
                        sad.remove(sad)
                        print 'SLN fail', sad # remove fail number from list
                    N = sum(sad) # Find Total Abundance
                    S = len(sad) # Find number of species
                 
                    prdSAD = AvgShape(Models.SimLogNormInt(N, S, sample_size)) #Get average shape of predicted SAD
                    
                    for i in prdSAD:
                            SLN.write("%s\n" % i)
                 
                    count += 1
                    print count
            print 'SimLogNorm Pred Done'
            SLN.close() 
                
                
                
        if model == 'Sample_SimpleRandomFraction':
            print 'Writing Simple Random Fraction Pred'
            count = 0            
           
            with open(mydir + "/Results/RandFractPred.txt", "w") as RF:
                for sad in SADs:
                    if len(sad) <= 1:
                        sad.remove(sad)
                        print 'RF fail', sad
                    N = sum(sad) # Find Total Abundance
                    S = len(sad) # Find number of species
                   
                    prdSAD = AvgShape(Models.Sample_SimpleRandomFraction(N, S, sample_size)) #Get average shape of predicted SAD
                                    
                    for i in prdSAD:
                            RF.write("%s\n" % i)
                   
                    count += 1
                    print count
            print 'Sample Rand Fract Pred Done'
            RF.close() 


        if model == 'SimParetoInt':
            print 'Writing Pareto Pred'
            count = 0            
           
            with open(mydir + "/Results/ParetoPred.txt", "w") as Par:
                for sad in SADs:
                    if len(sad) <= 1:
                        sad.remove(sad)
                        print 'Pareto fail', sad                    
                    N = sum(sad) # Find Total Abundance
                    S = len(sad) # Find number of species
               
                    prdSAD = AvgShape(Models.SimParetoInt(N, S, sample_size)) #Get average shape of predicted SAD
                    for i in prdSAD:
                        Par.write("%s\n" % i)
               
                    count += 1
                    print count
            print ' Pareto Pred Done'
            Par.close() 

###################################################################
'''This function will combine the predicted SADs to the Observed. The resulting file should 
be structured as follows: Site, Date, Species, Obs Ab, Pred Ab.'''

def combine():
    with open('/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt') as f1, open(mydir + "/Results/BrokenStickPred.txt") as f2, open(mydir + '/Results/BSObsPred.txt', 'w') as bsop:
        for fst, snd in izip(f1, f2):
            bsop.write('{0} {1}\n'.format(fst.rstrip(), snd.rstrip()))
            
    with open('/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt') as f1, open(mydir + "/Results/SimLogNormPred.txt") as f2, open(mydir + '/Results/SLNObsPred.txt', 'w') as slnop:
        for fst, snd in izip(f1, f2):
            slnop.write('{0} {1}\n'.format(fst.rstrip(), snd.rstrip()))
            
    with open('/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt') as f1, open(mydir + '/Results/ParetoPred.txt') as f2, open(mydir + '/Results/ParObsPred.txt', 'w') as paop:
        for fst, snd in izip(f1, f2):
            paop.write('{0} {1}\n'.format(fst.rstrip(), snd.rstrip()))
            
    with open('/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt') as f1, open(mydir + '/Results/RandFractPred.txt') as f2, open(mydir + '/Results/RandFracObsPred.txt', 'w') as rfop:
        for fst, snd in izip(f1, f2):
            rfop.write('{0} {1}\n'.format(fst.rstrip(), snd.rstrip()))
            
###################################################################
'''Function to pull samples from large data set.
Need to do this so that same SAD is not selected twice.s'''

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
#sample = get_samples(OBS, 1)
pred = get_predx(OBS, 10)
combine()