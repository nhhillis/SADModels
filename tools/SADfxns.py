from __future__ import division
import math
import numpy as np
import scipy
from scipy import stats


from __future__ import division
import sys
import numpy as np
from scipy import stats
from scipy.stats import gaussian_kde
import re


def get_SADs(path, dataset):

    minS = 10
    DATA = open(path + '/' + dataset + '.txt','r')
    ct1 = 0
    ct2 = 0
    d = DATA.readline()
    m0 = re.match(r'\A\S*',d).group()
    site_name = str(m0)
    m2 = float(re.findall(r'\S*\S$',d)[0])

    SAD = [float(m2)]
    SADs = []

    for d in DATA:
        ct1+=1
        m1 = re.match(r'\A\S*',d).group()
        if m1 == m0:
            m2 = float(re.findall(r'\S*\S$',d)[0])
            if m2 > 0:
                SAD.append(m2)

        else:
            site_name = m0
            m0 = m1
            if len(SAD) >= minS:
                SAD.sort()
                SAD.reverse()
                SADs.append([site_name, SAD]) # can also append, site_name, len(SAD), and sum(SAD)

                ct2+=1
            SAD = []
            abundance = re.findall(r'\S*\S$',d)[0]

            if abundance > 0:SAD.append(float(abundance))

    #SAD.sort()
    #SAD.reverse()
    #SADs.append(SAD)

    DATA.close()
    SADs.append([site_name, SAD])
    return(SADs)



def get_hottest_SAD(unique_SADs):
    """ Find the SAD in a random sample with the greatest average commonness
        among its ranked abundance states. This SAD is taken to represent the
        central tendency of the set, based on the SAD shape. """

    #if len(unique_SADs) > 500:
        #unique_SADs = random.sample(unique_SADs,500)

    N = sum(unique_SADs[0])
    S = len(unique_SADs[0])
    a1 = 0 # SAD mean
    v1 = 0 # SAD variance
    for rad in unique_SADs:
        in_common = []
        ct1 = 0
        for a in rad: # for each rank
            c = 0
            for sad in unique_SADs:
                if a == sad[ct1]:
                    c += 1
            in_common.append(np.log(c))
            ct1 += 1
        a2 = np.mean(in_common)
        v2 = np.var(in_common, ddof=1)
        if a2 > a1:
            a1 = a2
            v1 = v2
            xRAD = rad
        elif a2 == a1:
            if v2 < v1:
                a1 = a2
                v1 = v2
                xRAD = rad
    #percentile_evar = stats.percentileofscore(sample_evar,obs_evar)
    return xRAD
