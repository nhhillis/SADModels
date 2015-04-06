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

        Fig. 2 - This function generates a 2x2 figure of 4 subplots, where each
                 subplot uses the same combination of total abundance (N) and
                 species richness (S) to reveal a heat map of 1,000 random RACs
                 for a particular model. The predicted form the RAC based on
                 finding the form in the random sample that overlaps the greatest
                 with all other forms, as in Locey and White (2013).

        Fig. 3 - This function generates a 2x2 figure of Obs vs. Pred heat maps.
                 Each of the four subplots reveals the results for a single model.
                 This function also generates the modified coefficient of
                 determination, i.e., r-squared, around the 1-to-1 line.

        Fig. 4 - (Note to Nathan: If possible, you could generate this figure
                 in powerpoint using previously made figures, and then save the
                 powerpoint slide as a .png file.) Otherwise,...

                 This function generates a 1x2 plot (1 row, 2 columns):
                 Subplot 1.) Broken Stick (i.e. geometric distribution) heatmap,
                 predicted form, and then the predicted form based on Ken's code
                 or using the prediction for the most likely RAC given N and S,
                 i.e., from mete.py

        Fig. 5 - This function generates a 2x2 figure, for R2 vs. N for each
                 model.


        Fig. 6 - (Maybe not for meeting if there isn't time)
                 A figure of kernel density curves. Each curve represents the
                 pdf for p-values resulting from a 2-tailed Kolmogorov-Smirnov
                 test.

'''

########### PATHS & ADDITIONAL IMPORTS #########################################

mydir = os.path.expanduser("~/GitHub/SADModels/")
sys.path.append(mydir + '/tools')
import OneToOne

sys.path.append(mydir + "/tools/macroecotools")
import macroecotools

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
    """ This function generates a 2x2 figure of Obs vs. Pred heat maps.
    Each of the four subplots reveals the results for a single model.
    This function also generates the modified coefficient of determination,
    i.e., r-squared, around the 1-to-1 line. """

    OneToOne.plot_obs_pred_sad(SADModels, data_dir = mydir + '/Results/')
    # Be sure to look over the function in OneToOne.py, you'll need to do small modifications

    return



def fig4(SADModels):

    """ Fig. 4 - (Note to Nathan: If possible, you could generate this figure
        in powerpoint using previously made figures, and then save the
        powerpoint slide as a .png file.) Otherwise,...

        This function generates a 1x2 plot (1 row, 2 columns):
        Subplot 1.) Broken Stick (i.e. geometric distribution) heatmap,
        predicted form, and then the predicted form based on Ken's code
        or using the prediction for the most likely RAC given N and S,
        i.e., from mete.py """



    return




def fig5(SADModels):
    """ This function generates a 2x2 figure, with these subplots:
        One subplot for each model:
            r-squared vs. N
            list of r-squared values and list of Ns
            plotted against each other
    """
    fig = plt.figure()

    for i, model in enumerate(SADModels):

        fig.add_subplot(2, 2, i+1)

        obs_pred_data = import_obs_pred_data(mydir + '/Results/' + model + '.txt')
        obs = ((obs_pred_data["obs"]))
        pred = ((obs_pred_data["pred"]))
        site = ((obs_pred_data["site"]))

        obs_data = []
        pred_data = []

        for sites in np.unique(site):
            obs_data.append(obs[sites==site])
            pred_data.append(pred[sites==site])

        Ns = []
        r2s = []

        for j, sad in enumerate(obs_data):

            r2 = macroecotools.obs_pred_rsquare(np.array(sad), np.array(pred_data[j]))
            r2s.append(r2)
            N = sum(sad) # Find Total Abundance
            Ns.append(N)

        plt.scatter(Ns, r2s, color='0.3', label=model) # label is for the legend
        plt.xlabel('Total Abundance', fontsize=8)
        plt.ylabel('Rsquared Value', fontsize=8)
        
        if model == 'SimBrokenStick':
            plt.title("Broken Stick R^2 v N", fontsize = 10)

        elif model == 'SimLogNormInt':
            plt.title("Log Norm R^2 v N", fontsize = 10)

        elif model == 'SimpleRandomFraction':
            plt.title("Random Fraction R^2 v N", fontsize = 10)

        elif model == 'SimParetoInt':
            plt.title("Pareto Int R^2 v N", fontsize = 10)

        print model + ': Done'

    
        # insert code to plot a legend
    plt.savefig('/Users/Nathan_Hillis/GitHub/SADModels/Results/R2vN.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
    plt.show()
    return



def fig6(SADModels):
    """ This function generates a single figure of kernel density curves.
    Each curve represents the pdf for p-values resulting from a 2-tailed
    Kolmogorov-Smirnov test. """

    return



########### END FUNCTIONS ######################################################



########### LOOP THROUGH OBS-PRED FILES AND ANALYZE RESULTS ####################
SADModels = ['SimBrokenStick', 'SimLogNormInt', 'SimpleRandomFraction',
                            'SimParetoInt']

#fig1(SADModels)
#fig2(SADModels)
fig3(SADModels)
#fig5(SADModels)
