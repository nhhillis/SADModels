from __future__ import division
import math
#This code calculates diversity and Evenness
#This code is in the beginning stages 
#Simpson's index = D = sum(ni[ni-1])/(N[N-1])
######Steps######
#Select each species as n, for each n multiply n * n-1
#sum all n(n-1) then divide by N(N-1)
#D = Simpson's Index
#SD = Simpson's index of Diversity
#Evns = Simpson's measure of Evenness

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


def PielouEven(RAC): #Based on Smith and Wilson 1996
    RAC1 = [float(i) for i in RAC]
    D = SimpsonD(RAC1) + 1
    lnD = math.log(1/D)
    lnS = math.log(len(RAC1))
    return lnD/lnS #returning Negative Values at the moment

RAC = [10,1,1,1]  
print PielouEven(RAC)
