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
    """ This function generates a single figure of kernel density curves.
    Each curve represents the pdf for p-values resulting from a 2-tailed
    Kolmogorov-Smirnov test. """
    
    def kdens_full_feasibles(N,S):
        # TAKEN FROM THE feasible_functions.py script used for White et al. (2013)
        '''Working on this.  Just have copied it over at this point'''
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        parts = get_all_partitions(N,S)
        Evars = Evars_sample(parts) # This could be a sample based on another metric (above)
        D = get_kdens(Evars)
        plt.xlim(0.0, 1.0)
        plt.plot(D[0],D[1],color='black',lw=5)
        parts = get_all_partitions(N,S+10)
        Evars = Evars_sample(parts) # This could be a sample based on another metric (above)
        D = get_kdens(Evars)
        plt.xlim(0.0, 1.0)
        plt.plot(D[0],D[1],color='gray',lw=5)
        plt.axvline(x=0.673,ymin=0,ymax=10,color='black',ls='--',lw=3) # plot a vertical line at the mode
        plt.setp(ax, xticks=[0.2,0.6,1.0],yticks=[0,2,4,6])
        for tick in ax.yaxis.get_major_ticks():
            tick.label.set_fontsize(15)
        for tick in ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(15)
        plt.savefig('Figure3.png', dpi=400, pad_inches=0) 
        





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
#fig2(SADModels)
#fig3(SADModels)
