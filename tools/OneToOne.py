#!/usr/bin/env sage -python
from __future__ import division
import sys
import os

mydir = os.path.expanduser("~/Users/Nathan_Hillis/GitHub/SADModels")
sys.path.append(mydir)

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid.inset_locator import inset_axes

sys.path.append(mydir + "/tools/") # You'll need to change this
import macroecotools
import predRADs
import mete


""" Functions to examine observed vs. predicted abundance relationship around
    the one-to-one line.

    These functions were taken from the MIT-licensed public GitHub repository:
    github.com/weecology/white-etal-2012-ecology/blob/master/mete_sads.py
"""



def import_obs_pred_data(input_filename):
    # TAKEN FROM THE mete_sads.py script used for White et al. (2012)

    data = np.genfromtxt(input_filename, dtype = "S15, S15, S15, f8, f8",
                names = ['date','site','species','obs','pred'], delimiter = " ")

    # ensure the delimiter is correct
    return data



def hist_mete_r2(sites, obs, pred):  # TAKEN FROM Macroecotools or the mete_sads.py script used for White et al. (2012)
    """Generate a kernel density estimate of the r^2 values for obs-pred plots"""
    r2s = []
    for site in np.unique(sites):
        obs_site = obs[sites==site]
        pred_site = pred[sites==site]
        r2 = macroecotools.obs_pred_rsquare(obs_site, pred_site)
        r2s.append(r2)

    hist_r2 = np.histogram(r2s, range=(0, 1))
    xvals = hist_r2[1] + (hist_r2[1][1] - hist_r2[1][0])
    xvals = xvals[0:len(xvals)-1]
    yvals = hist_r2[0]
    plt.plot(xvals, yvals, 'k-', linewidth=2)
    plt.axis([0, 1, 0, 1.1 * max(yvals)])



def obs_pred_r2_multi(methods, data_dir= 'Users/Nathan_Hillis/Desktop/Data/'): 
    # TAKEN FROM THE mete_sads.py script
    print 'generating 1:1 line R-square values for dataset(s)'

    for j, method in enumerate(methods):
        obs_pred_data = import_obs_pred_data(data_dir + dataset + '/' + dataset + '_obs_pred.txt')
        obs = ((obs_pred_data["obs"]))
        pred = ((obs_pred_data["pred"]))
        print method,' ', macroecotools.obs_pred_rsquare(np.log10(obs), np.log10(pred))



def plot_obs_pred_sad(SADModels, data_dir='~/data/', radius=2): 
    # TAKEN FROM THE mete_sads.py script used for White et al. (2012)
    # Used for Figure 3 Locey and White (2013)        ########################################################################################

    """Multiple obs-predicted plotter"""
    fig = plt.figure()

    for i, model in enumerate(SADModels):

        fig.add_subplot(2, 2, i+1)

        obs_pred_data = import_obs_pred_data(data_dir +  '/Results/' + model ) 
        site = ((obs_pred_data["site"]))
        obs = ((obs_pred_data["obs"]))
        pred = ((obs_pred_data["pred"]))

        axis_min = 0.5 * min(obs)
        axis_max = 2 * max(obs)

        macroecotools.plot_color_by_pt_dens(pred, obs, radius, loglog=1,
                        plot_obj=plt.subplot(2, 2, i+1))

        plt.plot([axis_min, axis_max],[axis_min, axis_max], 'k-')
        plt.xlim(axis_min, axis_max)
        plt.ylim(axis_min, axis_max)

        plt.tick_params(axis='both', which='major', labelsize=8)
        plt.subplots_adjust(wspace=0.5, hspace=0.3)

        r2 = macroecotools.obs_pred_rsquare(np.log10(obs), np.log10(pred))
        print model, r2

        # Create inset for histogram of site level r^2 values
        axins = inset_axes(ax, width="30%", height="30%", loc=4)
        hist_mete_r2(site, np.log10(obs), np.log10(pred))
        plt.setp(axins, xticks=[], yticks=[])

        plt.title(model)
        #plt.text(1, 2000,  r'$R^2$' + '='+ str(round(r2,3)))
        plt.ylabel('Observed abundance',rotation='90',fontsize=12)
        plt.xlabel('Predicted abundance',fontsize=12)

    plt.savefig(mydir+'/obs_pred_plots.png', dpi=600)#, bbox_inches = 'tight')#, pad_inches=0)
