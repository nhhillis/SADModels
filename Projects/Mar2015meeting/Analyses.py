import csv
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
import math
import sys
import os

mydir = os.path.expanduser("~/GitHub/SADModels/") # A general file path; this means that:
# 1.) You will need to create a GitHub directory in your home directory
# 2.) Move SADModels into the GitHub directory


sys.path.append(mydir + "Analysis")

from AverageShape import AvgShape

sys.path.append(mydir + 'Models/')
import Models

sys.path.append(mydir + '/Projects/Mar2015meeting/functions.py')

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


