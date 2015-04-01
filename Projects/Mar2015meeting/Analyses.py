import csv
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
import math
import sys
import os
from scipy import stats
import matplotlib.pyplot as plt


''' DESCRIPTION:
    This code obtains observed SADs, predicted SADs from various random fraction
    models, & writes the data to a file, with different files for each model.

    Each results file will has these rows: date, site, species, obs, pred '''



########### PATHS & ADDITIONAL IMPORTS #########################################

mydir = os.path.expanduser("~/GitHub/SADModels/")
sys.path.append(mydir + '/tools')
import OneToOne

########### END ################################################################



########### FUNCTIONS ##########################################################

def import_obs_pred_data(input_filename):
    # TAKEN FROM THE mete_sads.py script used for White et al. (2012)

    data = np.genfromtxt(input_filename, dtype = "S15, S15, S15, f8, f8",
                names = ['date','site','species','obs','pred'], delimiter = " ")

    # ensure the delimiter is correct
    return data

def fig1(SADModels):
    """ This function generates a 2x2 figure of Obs vs. Pred heat maps.
    Each of the four subplots reveals the results for a single model.
    This function also generates the modified coefficient of determination,
    i.e., r-squared, around the 1-to-1 line. """

    OneToOne.plot_obs_pred_sad(SADModels, data_dir='~/data/')
    # Yes, that's all. done.
    # Be sure to look over the function in OneToOne.py, you'll need to do small modifications

    return


def fig2(SADModels):
    """ This function generates a single figure of kernel density curves.
    Each curve represents the pdf for p-values resulting from a 2-tailed
    Kolmogorov-Smirnov test. """




def fig3(SADModels):
    """ This function generates a 2x2 figure, with these subplots:
    1. r-squared vs. N
    2. r-squard vs. S
    3. r-squared vs. N/S (i.e. average abundance)
    4. ...
    """



########### END FUNCTIONS ######################################################



########### LOOP THROUGH OBS-PRED FILES AND ANALYZE RESULTS ####################
SADModels = ['SimBrokenStick', 'SimLogNormInt', 'SimpleRandomFraction',
                            'SimParetoInt']

fig1(SADModels)
fig2(SADModels)
fig3(SADModels)
