import csv
import numpy as np
from random import randrange, choice
import matplotlib.pyplot as plt
import sys
import os

mydir = os.path.expanduser("~/GitHub/SADModels/")
sys.path.append(mydir + 'Models/')
import Models
sys.path.append(mydir + '/tools')
import HeatMap
sys.path.append(mydir + '/tools/AverageShape')
import AverageShape
##################################################################

'''This is finding predicted SADs for the world bird populations.
Well it was a nice try but I ran out of memory.'''

SADModels = ['SimBrokenStick', 'SimLogNormInt', 'SimpleRandomFraction',
                            'SimParetoInt']
N = 400000
S = 100
sample_size = 1000
fig = plt.figure()

for i, model in enumerate(SADModels):

        fig.add_subplot(2, 2, i+1)

        if model == 'SimBrokenStick':
                    prdSADs = Models.SimBrokenStick(N, S, sample_size)
                    HeatMap.RACHeatMap(fig, prdSADs)
                    plt.plot(np.log(AverageShape.AvgShape(prdSADs)), color = 'lime', label = 'Predicted', lw = 2)
                    
        elif model == 'SimLogNormInt':
                    prdSADs = Models.SimLogNormInt(N, S, sample_size)
                    HeatMap.RACHeatMap(fig, prdSADs)
                    plt.plot(np.log(AverageShape.AvgShape(prdSADs)), color = 'lime', label = 'Predicted', lw = 2)
                    
        elif model == 'SimpleRandomFraction':
                    prdSADs = Models.SimpleRandomFraction(N, S, sample_size)
                    HeatMap.RACHeatMap(fig, prdSADs)
                    plt.plot(np.log(AverageShape.AvgShape(prdSADs)), color = 'lime', label = 'Predicted', lw = 2)
                    
        elif model == 'SimParetoInt':
                    prdSADs = Models.SimParetoInt(N, S, sample_size)
                    HeatMap.RACHeatMap(fig, prdSADs)
                    plt.plot(np.log(AverageShape.AvgShape(prdSADs)), color = 'lime', label = 'Predicted', lw = 2)



        plt.title(model +'_WorldBirds')
        
        plt.text(10, 8, 'N =' + str(N) + ', S =' + str(S) + ', Sample Size' + str(sample_size), fontsize = 8)
        leg = plt.legend(loc=1,prop={'size':8})
        leg.draw_frame(False)
        plt.xlim(0, S + 2)
        plt.xlabel('Rank in abundance', fontsize=12)
        plt.ylabel('log(abundance)', fontsize=12)
            

plt.savefig('/Users/Nathan_Hillis/GitHub/SADModels/projects/Mar2015meeting/BigNumbers/BigNumbers_HeatMap.png', dpi=600, bbox_inches = 'tight', pad_inches=0.03)
plt.show()