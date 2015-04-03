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


''' DESCRIPTION:
    This code obtains observed SADs, predicted SADs from various random fraction
    models, & writes the data to a file, with different files for each model.

    Each results file will has these rows: date, site, species, obs, pred '''



########### PATHS & ADDITIONAL IMPORTS #########################################

mydir = os.path.expanduser("~/GitHub/SADModels/")
data = os.path.expanduser("~/data") # a general path to a data directory

sys.path.append(mydir + "tools")
from AverageShape import AvgShape

sys.path.append(mydir + 'Models/')
import Models

########### END ################################################################



########### FUNCTIONS ##########################################################

def import_obs_data(input_filename):
    # Inspired by a function in mete_sads.py script used for White et al. (2012)

    data = np.genfromtxt(input_filename, dtype = "S15, S15, S15, f8, f8", 
    names = ['site', 'date', 'species', 'obs'], delimiter = "    ") #Error is returning here
    # complete the line above & ensure the delimiter is correct
    return data


def get_predx(SADs, sample_size):

    '''This function obtains predicted forms of the empirical SADs and writes them to seperate ObsPred files '''


    SADModels = ['SimBrokenStick', 'SimLogNormInt',
                    'SimpleRandomFraction', 'SimParetoInt']

    for model in SADModels:
        count = 0
        print 'Writing ' + model

        with open(mydir + '/Results/' + model + '.txt', 'w') as OUT:
            for sad in SADs:

                N = sum(sad) # Find Total Abundance
                S = len(sad) # Find number of species

                if N > 10**6 or S < 10: continue
                if max(sad) < 2: continue

                if model == 'SimBrokenStick':
                    prdSADs = Models.SimBrokenStick(N, S, sample_size)

                elif model == 'SimLogNormInt':
                    prdSADs = Models.SimLogNormInt(N, S, sample_size)

                elif model == 'SimpleRandomFraction':
                    prdSADs = Models.SimpleRandomFraction(N, S, sample_size)

                elif model == 'SimParetoInt':
                    prdSADs = Models.SimParetoInt(N, S, sample_size)

                if len(prdSADs) > 10: 
                    if len(prdSADs) < 20: print "Small sample size:", len(prdSADs)

                    prdSAD = AvgShape(prdSADs)

                    #Get average shape of the SAD from a set of simulated SADs
                    for i, pred in enumerate(prdSAD):
                        print>>OUT, date, site, species, obs, pred

                #need to print something for failed SADs
                count += 1
                print count

            print model + ': Done'
            OUT.close()




def get_samples(SADs, NumSamples):
    '''A function to pull samples from a large data set.
    Need to do this so that same SAD is not selected twice.s'''

    Samples = []

    while len(Samples) < NumSamples:

        samp =choice(SADs) #Randomly choose sample
        SADs.remove(samp)
        Samples.append(samp)

    print 'Samples', Samples
    return Samples

########### END FUNCTIONS ######################################################


########### FUNCTION CALLS #####################################################

ObsSADs = import_obs_data('/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt')
pred = get_predx(ObsSADs, 100)
