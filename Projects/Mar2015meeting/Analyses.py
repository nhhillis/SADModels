import csv
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
import math
import sys
import os
from scipy import stats
from scipy.stats import gaussian_kde
import matplotlib.pyplot as plt


''' DESCRIPTION:
    This code generates 3 figures:
        Fig. 1 - This function generates a 2x2 figure of Obs vs. Pred heat maps.
                    Each of the four subplots reveals the results for a single model.
                    This function also generates the modified coefficient of determination,
                    i.e., r-squared, around the 1-to-1 line.
        Fig. 2 - This function generates a single figure of kernel density curves.
                    Each curve represents the pdf for p-values resulting from a 2-tailed
                    Kolmogorov-Smirnov test. 
        Fig. 3 - This function generates a 2x2 figure, with these subplots:
                    1. r-squared vs. N
                    2. r-squard vs. S
                    3. r-squared vs. N/S (i.e. average abundance)
                    4. ...''' 



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
    
    
def get_kdens(_list):
    """ Finds the kernel density function across a sample of SADs """
        # TAKEN FROM THE feasible_functions.py script used for White et al. (2013)

    density = gaussian_kde(_list)
    n = len(_list)
    #xs = np.linspace(min(_list),max(_list),n)
    xs = np.linspace(0.0,1.0,n)
    density.covariance_factor = lambda : 0.5
    density._compute_covariance()
    D = [xs,density(xs)]
    return D
        
        
def fig1(SADModels):
    """ This function generates a 2x2 figure of Obs vs. Pred heat maps.
    Each of the four subplots reveals the results for a single model.
    This function also generates the modified coefficient of determination,
    i.e., r-squared, around the 1-to-1 line. """

    OneToOne.plot_obs_pred_sad(SADModels, data_dir = mydir + '/Results/')
    # Be sure to look over the function in OneToOne.py, you'll need to do small modifications

    return

def fig2(SADModels):
    '''Heat map'''
    x = []
    y = []
    
    for RAC in SLN: #Placing SLN RAC values into lists
        y.extend(np.log(RAC))
        x.extend(range(len(RAC)))
    
    
    plt.plot(np.log(ObsRAC), color='0.3', lw=3, alpha = 0.6)
    
    plt.hexbin(x, y, mincnt=1, gridsize = 40, bins = 'log', cmap=plt.cm.jet) #Generating Heat Map for SLN RAC
        
    plt.xlim(0, S + 5)
    plt.xlabel('Rank in abundance', fontsize=16)
    plt.ylabel('log(abundance)', fontsize=16)
    
    
    plt.savefig('/Users/Nathan_Hillis/Desktop/IRB_Project/All_Site_N='+str(N)+'_S='+str(S)+'.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
    plt.show()


def fig3(SADModels):
    """ This function generates a single figure of kernel density curves.
    Each curve represents the pdf for p-values resulting from a 2-tailed
    Kolmogorov-Smirnov test. """
     
        


def fig4(SADModels):
    """ This function generates a 2x2 figure, with these subplots:
        One subplot for each model:
            r-squared vs. N
            list of r-squared values and list of Ns
            plotted against each other
    """
    
def fig5(SADModels):
    '''Compare



########### END FUNCTIONS ######################################################



########### LOOP THROUGH OBS-PRED FILES AND ANALYZE RESULTS ####################
SADModels = ['SimBrokenStick', 'SimLogNormInt', 'SimpleRandomFraction',
                            'SimParetoInt']

fig1(SADModels)
#fig2(SADModels)
#fig3(SADModels)
