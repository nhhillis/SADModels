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

mydir = os.path.expanduser("~/GitHub/SADModels/")
data = os.path.expanduser("~/data") # a general path to a data directory

sys.path.append(mydir + "tools")
from AverageShape import AvgShape

sys.path.append(mydir + 'Models/')
import Models

'''This code obtains observed SADs, predicted SADs from various random fraction
models, and writes the data to a file, with a different results file for each model
Each results file will have these rows: Date, Site, Species, ObsAb, PredAB

- Add test functions, e.g. check that the same SAD isn't drawn twice, i.e.,
sampling w/out replacement '''


def import_obs_pred_data(input_filename):
    # TAKEN FROM THE mete_sads.py script used for White et al. (2012)

    data = np.genfromtxt(input_filename, dtype = "S15, S15, S15, f8, f8",
    names = ['date','site','species','obs','pred'], delimiter = " ")

    # ensure the delimiter is correct
    return data


def import_obs_data(input_filename):
    # TAKEN FROM THE mete_sads.py script used for White et al. (2012)

    data = np.genfromtxt(input_filename, dtype = "S15, S15, S15, f8, f8",
    names = ['species', ..., ..., 'obs'], delimiter = " ")
    # complete the line above & ensure the delimiter is correct
    return data


###################################################################
'''Gets predicted average SAD for sample'''
'''This function is working with the small samples that I am using.  Need to run with entire dataset,
but it will take a while'''

def get_predx(SADs, sample_size): #Removed Dom Pre Int, need to check for bugs

    SADModels = ['SimBrokenStick', 'SimLogNormInt', 'Sample_SimpleRandomFraction', 'SimParetoInt']

    for model in SADModels:

        if model == 'SimBrokenStick':
            print 'Writing Broken Stick Pred'
            count = 0

            with open(mydir + "/Results/BrokenStickPred.txt", "w") as BS:
                for sad in SADs:
                    N = sum(sad) # Find Total Abundance
                    S = len(sad) # Find number of species
                    # add if statement to make sure that not iterating over empty list (failed Sads)

                    prdSAD1 = Models.SimBrokenStick(N, S, sample_size) #Get average shape of predicted SAD

                    if len(prdSAD1) > 0:
                        prdSAD = AvgShape(prdSAD1)#getting a list index out of range error here
                        #Must be from the blank list of the failed SAD
                        for i in prdSAD:
                            BS.write("%s\n" % i)

                    #need to print something for failed SADs




                    count += 1
                    print count

            print 'Broken Stick Pred Done'
            BS.close()



        if model == 'SimLogNormInt':
            print 'Writing Sim Log Norm Pred'
            count = 0

            with open(mydir + "/Results/SimLogNormPred.txt", "w") as SLN:
                for sad in SADs:

                    N = sum(sad) # Find Total Abundance
                    S = len(sad) # Find number of species

                    prdSAD1 = Models.SimLogNormInt(N, S, sample_size) #Get average shape of predicted SAD

                    if len(prdSAD1) > 0:
                        prdSAD = AvgShape(prdSAD1)#getting a list index out of range error here
                        #Must be from the blank list of the failed SAD
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

                    N = sum(sad) # Find Total Abundance
                    S = len(sad) # Find number of species

                    prdSAD1 = Models.Sample_SimpleRandomFraction(N, S, sample_size) #Get average shape of predicted SAD

                    if len(prdSAD1) > 0:
                        prdSAD = AvgShape(prdSAD1)
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
                    N = sum(sad) # Find Total Abundance
                    S = len(sad) # Find number of species

                    prdSAD1 = Models.SimParetoInt(N, S, sample_size) #Get average shape of predicted SAD

                    if len(prdSAD1) > 0:
                        prdSAD = AvgShape(prdSAD1)
                        for i in prdSAD:
                            Par.write("%s\n" % i)

                    count += 1
                    print count
            print ' Pareto Pred Done'
            Par.close()


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

ObsSADs = import_obs_data('/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt')
#sample = get_samples(OBS, 1)
pred = get_predx(ObsSADs, 100)
