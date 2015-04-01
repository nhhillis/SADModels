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
sys.path.append(mydir + '/Projects/Mar2015meeting/functions.py')

########### END ################################################################



########### FUNCTIONS ##########################################################

def import_obs_pred_data(input_filename):
    # TAKEN FROM THE mete_sads.py script used for White et al. (2012)

    data = np.genfromtxt(input_filename, dtype = "S15, S15, S15, f8, f8",
    names = ['date','site','species','obs','pred'], delimiter = " ")

    # ensure the delimiter is correct
    return data


########### END FUNCTIONS ######################################################



########### LOOP THROUGH OBS-PRED FILES AND ANALYZE RESULTS ####################
SADModels = ['SimBrokenStick', 'SimLogNormInt', 'SimpleRandomFraction',
                            'SimParetoInt']

for model in SADModels:
    ct = 0
    print 'Analyzing Obs vs. Pred for ' + model

    SADdata(mydir + '/Results/' + model + '.txt')

        with open(mydir + '/Results/' + model + '.txt', 'w') as OUT:
            for sad in SADs:
