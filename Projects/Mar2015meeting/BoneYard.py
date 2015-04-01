import csv
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
import math
import sys
import os
from scipy import stats

mydir = os.path.expanduser("~/GitHub/SADModels/")

sys.path.append(mydir + '/Projects/Mar2015meeting/functions.py')


'''This file will -
        1. Get empirical SADs
        2. Get predicted SADs
        3. Write empirical and predicted SADs to a file (obs_pred.txt)'''

#################################################################
#Working on importing txt. file but getting ValueError: invalid literal for int() with base 10: ''
# needs to be moved to functions
import os
import numpy as np

mydir = os.path.expanduser("/GitHub/SADModels/")
path = ('/Users/Nathan_Hillis/Desktop/Data')

datafile = path + ('/66_data.txt')
num_lines = sum(1 for line in open(datafile))
print num_lines

'''Data = open(datafile, 'r')
SadData = [x.split("\t") for x in Data]

print SadData'''

'''SADs=[]
for line in SadData:
    SAD = map(int, line)
    SADs.append(SAD)

print SAD'''


def get_ObsSADs():

    """ This function gets sads from a file.

    Use a more general file path: data + 'YR_66_v2.txt' """

    DATA = '/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt'
    mydict = {}
    count = 0
    with open(DATA) as i:
        for d in i:
            count += 1
            print count
            if d.strip():
                d = d.split()
                species = d[0]
                abundance = int(d[3])
                if abundance > 0:
                    if species in mydict:
                        mydict[species].append(abundance)
                    else:
                            mydict[species] = [abundance]
    SADs = []
    SADlist = mydict.items()
    for tup in SADlist:
        SAD = tup[1]
        if len(SAD) >= 1:
            SAD.sort()
            SAD.reverse()
            SADs.append(SAD)
    return SADs


def combine():
    with open('/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt') as f1, open(mydir + "/Results/BrokenStickPred.txt") as f2, open(mydir + '/Results/BSObsPred.txt', 'w') as bsop:
        for fst, snd in izip(f1, f2):
            bsop.write('{0} {1}\n'.format(fst.rstrip(), snd.rstrip()))

    with open('/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt') as f1, open(mydir + "/Results/SimLogNormPred.txt") as f2, open(mydir + '/Results/SLNObsPred.txt', 'w') as slnop:
        for fst, snd in izip(f1, f2):
            slnop.write('{0} {1}\n'.format(fst.rstrip(), snd.rstrip()))

    with open('/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt') as f1, open(mydir + '/Results/ParetoPred.txt') as f2, open(mydir + '/Results/ParObsPred.txt', 'w') as paop:
        for fst, snd in izip(f1, f2):
            paop.write('{0} {1}\n'.format(fst.rstrip(), snd.rstrip()))

    with open('/Users/Nathan_Hillis/Desktop/Data/YR_66_v2.txt') as f1, open(mydir + '/Results/RandFractPred.txt') as f2, open(mydir + '/Results/RandFracObsPred.txt', 'w') as rfop:
        for fst, snd in izip(f1, f2):
            rfop.write('{0} {1}\n'.format(fst.rstrip(), snd.rstrip()))
