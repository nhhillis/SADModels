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




def SimpsonD(RAC):

    n1 = 0
    N = sum(RAC)
    for n in RAC:
        n1 += n * (n-1)

    D = n1/(N*(N-1))
    SD = 1 - D
    return SD


def SimpsonE(RAC):
    D = SimpsonD(RAC) + 1
    D = 1/D
    return D/len(RAC) #Evenness (Magurran 2004)


def Berger_Parker(sad):
    return max(sad)/sum(sad)


def Singletons(sad):
    singletons = sad.count(1)
    return 100*(singletons/len(sad))


def ShannonsH(sad):
    H = 0
    for i in sad:
        p = i/sum(sad)
        H += p*np.log(p)
    return H*-1.0


def Pielous(sad):
    H = Shannons_H(sad)
    S = len(sad)
    return H/np.log(S)


def simplest_gini(x):
        """Return computed Gini coefficient of inequality. This function was found at http://econpy.googlecode.com/svn/trunk/pytrix/utilities.py """

        #note: follows basic formula
        #see: `calc_gini2`
        #contact: aisaac AT american.edu

        x = sorted(x)  # increasing order
        n = len(x)
        G = sum(xi * (i+1) for i,xi in enumerate(x))
        G = 2.0*G/(n*sum(x)) #2*B
        return G - 1 - (1./n)


def gini_sample(SADs):
    """ Compute Gini's coefficient for each macrostate in a random sample """
    Gs = []
    for sad in SADs:
        G = simplest_gini(sad)
        Gs.append(G)
    return Gs


def Mcintosh_evenness(SAD):
    S = len(SAD)
    N = sum(SAD)
    sum_n = 0
    for n in SAD: sum_n += n**2
    U = np.sqrt(sum_n)
    E = (N - U)/(N - (N/np.sqrt(S)))
    return E


def pielous_evenness(SAD):
    S = len(SAD)
    N = float(sum(SAD))
    H = 0
    for p in SAD:
        H += -(p/N)*np.log(p/N)
    J = H/np.log(S)
    return J


def NHC_evenness(SAD):
    SAD.sort()
    SAD.reverse()
    x_list = range(1,len(SAD)+1)
    y_list = np.log(SAD)
    slope,intercept,r_value,p_value,std_err = stats.linregress(x_list, y_list)

    if slope > 0.0:
        evar = e_var(SAD)
        print slope, p_value, evar
    return slope


def Heips_evenness(SAD):
    S = len(SAD)
    N = float(sum(SAD))
    H = 0.0
    for p in SAD:
        H += -(p/N)*np.log(p/N)
    H = (np.exp(H) - 1)/(S - 1)
    return H


def simpsons_dom(SAD):
    D = 0.0
    N = sum(SAD)
    S = len(SAD)

    for x in SAD:
        D += x*(x-1)
    D = 1 - (D/(N*(N-1)))

    return D


def simpsons_evenness(SAD):
    D = 0.0
    N = sum(SAD)
    S = len(SAD)

    for x in SAD:
        D += (x*x) / (N*N)

    E = (1/D)/S
    if E > 1.0:
        print 'Simpsons violation',E
        print N,S, SAD
        sys.exit()

    return E



def EQ_evenness(SAD):

    SAD.sort()
    SAD.reverse()

    S = len(SAD)
    y_list = list(np.log(SAD))
    x_list = []
    for rank in range(1,S+1):
        x_list.append(rank/S)
    slope, intercept, rval, pval, std_err = stats.linregress(x_list, y_list)

    Eq = -2/np.pi*np.arctan(slope)
    return Eq



def e_var(SAD):
    P = np.log(SAD)
    S = len(SAD)
    X = 0
    for x in P:
        X += (x - np.mean(P))**2/S
    evar = 1 - 2/np.pi*np.arctan(X)
    return(evar)



def get_skews(_list):
    skews = []
    for i in _list:
        skews.append(stats.skew(i))

    return skews



def get_modal(_list):

    """ Finds the mode from a kernel density function across a sample """
    exp_mode = 0.0
    density = gaussian_kde(_list)
    n = len(_list)
    xs = np.linspace(min(_list),max(_list),n)
    density.covariance_factor = lambda : .001
    density._compute_covariance()
    D = [xs,density(xs)]
    d = 0
    maxd = 0.0
    while d < len(D[1]):
        if D[1][d] > maxd:
            maxd = D[1][d]
            exp_mode = D[0][d]
        d += 1
    return exp_mode


def get_kdens(_list, kernel=.5):
    """ Finds the kernel density function across a sample of SADs """
    density = gaussian_kde(_list)
    n = len(_list)
    xs = np.linspace(min(_list),max(_list),n)
    #xs = np.linspace(0.0,1.0,n)
    density.covariance_factor = lambda : kernel
    density._compute_covariance()
    D = [xs,density(xs)]
    return D
