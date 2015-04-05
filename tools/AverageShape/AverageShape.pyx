from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import random


def AvgShape(RACs):
    """ Find the SAD in a random sample with the greatest average commonness
        among its ranked abundance states. This SAD is taken to represent the
        central tendency of the set, based on the SAD shape. """

    if len(RACs) > 500:
        RACs = random.sample(RACs,500)

    N = sum(RACs[0])
    S = len(RACs[0])
    a1 = 0 # SAD mean
    v1 = 0 # SAD variance
    for rac in RACs:
        in_common = []
        ct1 = 0
        for a in rac: # for each rank
            c = 0
            for sad in RACs:
                if a == sad[ct1]:
                    c += 1
            in_common.append(np.log(c))
            ct1 += 1
        a2 = np.mean(in_common)
        v2 = np.var(in_common)
        if a2 > a1:
            a1 = a2
            v1 = v2
            xRAD = rac
        elif a2 == a1:
            if v2 < v1:
                a1 = a2
                v1 = v2
                xRAD = rac

    #percentile_evar = stats.percentileofscore(sample_evar,obs_evar)
    return xRAD




def PlotAvgShape(fig, sampleRACs):

    avgRAC = AvgShape(sampleRACs)
    ranks = range(1, len(avgRAC)+1)
    plt.plot(ranks, np.log(avgRAC), lw=1, color='Lime')
    return fig
