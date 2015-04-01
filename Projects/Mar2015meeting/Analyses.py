import csv
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
import math
import sys
import os
from scipy import stats

mydir = os.path.expanduser("~/GitHub/SADModels/")

sys.path.append(mydir + '/Projects/Mar2015meeting/functions.py')




def import_obs_pred_data(input_filename):
    # TAKEN FROM THE mete_sads.py script used for White et al. (2012)

    data = np.genfromtxt(input_filename, dtype = "S15, S15, S15, f8, f8",
    names = ['date','site','species','obs','pred'], delimiter = " ")

    # ensure the delimiter is correct
    return data
