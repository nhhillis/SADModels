from __future__ import division
import math
import numpy as np
import scipy
from scipy import stats


def GetAvgVar(RACsample):
    
    VARs = []
    
    for RAC in RACsample:
        VARs.append(np.var(RAC))
    
    avgVar = np.mean(VARs)
    
    return avgVar
        


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
 
    
   
       
def BergerP(RAC):
    return max(RAC)/sum(RAC)



def ShannonH(RAC): 
    totab = sum(RAC)
    H = 0
    for v in RAC:
       H += (v / totab) * np.log(v/totab)
    H = -H
    return H
    
def ShannonEven(RAC): #Based on Smith and Wilson 1996
    return ShannonH(RAC)/np.log(len(RAC))
    
        
            
#### functions for calculating stats for lists of RACs (curves) and SADs (histograms)                    
def GetAvgEvenness(RACsample):
    
    EVs = []
    
    for RAC in RACsample:
        EV = SimpsonE(RAC)
        EVs.append(EV)
    
    avgVar = np.mean(EVs)
    
    return avgVar         
             

def GetAvgSkew(RACsample):
    
    Skews = []
    for RAC in RACsample:
        Skews.append(stats.skew(RAC))
    
    avgSk = np.mean(Skews)
    return avgSk
    
 
def GetAvgDominance(RACsample):
    
    Doms = []
    for RAC in RACsample:
        Doms.append(BergerP(RAC))
    
    avgDom = np.mean(Doms)
    return avgDom
                      

def GetAvgDiversity(RACsample):
    
    SimpDs = []
    for RAC in RACsample:
        SimpDs.append(SimpsonD(RAC))
    
    AvgSimpD = np.mean(SimpDs)
    return AvgSimpD
                                                                           
                            