from __future__ import division
import sys

import numpy as np
import matplotlib.pyplot as plt
sys.path.append('Models/')
import Models 
sys.path.append('tools/')
import HeatMap
sys.path.append('Analysis/')
from AverageShape import PlotAvgShape



""" Right now, this is basically just the code from Fig1.py that makes Figure 1.
    We need to change it and use it to make Figure 2. """




N = 1000
S = 100
sample_size = 100


fig = plt.figure()
title = 'log(%N)'


""" 1. The Broken Stick Model constrained by N and S """
ax = fig.add_subplot(3, 3, 1)
RACsample = Models.SimBrokenStick(N, S, sample_size, rel=True)

fig = HeatMap.RACHeatMap(fig, RACsample)
fig = PlotAvgShape(fig, RACsample)

plt.title('Broken Stick', fontsize = 13)
plt.xlabel('Rank')
#plt.ylabel('Abundance')
plt.ylabel(title)

print 'finished broken stick\n'



""" 2. The Log-normal (75/25) constrained by N and S """
ax = fig.add_subplot(3, 3, 2)
RACsample = Models.SimLogNormFloat(N, S, sample_size, rel=True)

fig = HeatMap.RACHeatMap(fig, RACsample)
fig = PlotAvgShape(fig, RACsample)

plt.title('Log Normal', fontsize = 13)
plt.xlabel('Rank')
#plt.ylabel('Abundance')
plt.ylabel(title)

print 'finished lognormal\n'



""" 3. Pareto (80/20) constrained by N and S """
ax = fig.add_subplot(3, 3, 4)
RACsample = Models.SimParetoFloat(N, S, sample_size, rel=True)

fig = HeatMap.RACHeatMap(fig, RACsample)
fig = PlotAvgShape(fig, RACsample)

plt.title('Pareto', fontsize = 13)
plt.xlabel('Rank')
#plt.ylabel('Abundance')
plt.ylabel(title)

print 'finished Pareto\n'



""" 4. Random fraction constrained by N and S """
ax = fig.add_subplot(3, 3, 5)
RACsample = Models.Sample_SimpleRandomFraction(N, S, sample_size, rel=True)

fig = HeatMap.RACHeatMap(fig, RACsample)
fig = PlotAvgShape(fig, RACsample)

plt.title('Random Fraction', fontsize = 13)
plt.xlabel('Rank')
#plt.ylabel('Abundance')
plt.ylabel(title)

print 'finished random fraction\n'


""" 5. The Dominance Preemption constrained by N and S, allowing decimals """
ax = fig.add_subplot(3, 3, 7)
RACsample = Models.DomPreFloat(N, S, sample_size, rel=True)

fig = HeatMap.RACHeatMap(fig, RACsample)
fig = PlotAvgShape(fig, RACsample)

plt.title('Dominance Preemption', fontsize = 13)
plt.xlabel('Rank')
#plt.ylabel('Abundance')
plt.ylabel(title)

print 'finished dominance preemption (decimals)\n' 



""" 6. The Dominance Decay constrained by N and S, allowing decimals """
ax = fig.add_subplot(3, 3, 8)
RACsample = Models.DomDecayFloat(N, S, sample_size, rel=True)

fig = HeatMap.RACHeatMap(fig, RACsample)
fig = PlotAvgShape(fig, RACsample)

plt.title('Dominance Decay', fontsize = 13)
plt.xlabel('Rank')
#plt.ylabel('Abundance')
plt.ylabel(title)

print 'finished Dominance decay float\n'



""" Additional figure functions """
plt.subplots_adjust(wspace=0.8, hspace=0.8)
#fig.suptitle('N = '+str(N)+', S = '+str(S)) 
plt.savefig('figures/Heat_N='+str(N)+'_S='+str(S)+'.png', transparent=True, dpi=600, pad_inches = 0.1)
#plt.show()