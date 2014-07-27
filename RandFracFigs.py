from __future__ import division
import sys
import Models 
sys.path.append('/Users/Nathan_Hillis/SADModels/tools/')

sys.path.append('/Users/lisalocey/Desktop/SADModels/tools/')

import HeatMap
import matplotlib.pyplot as plt



N = 1000
S = 50
sample_size = 200

fig = plt.figure()

""" The Broken Stick Model constrained by N and S """
ax = fig.add_subplot(3, 3, 1)
BrkStk = Models.SimBrokenStick(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, BrkStk)
plt.title('Broken Stick', fontsize = 10)
# plot hottest RAC
plt.xlabel(...
plt.ylabel(...
print 'finished broken stick'


""" The Dominance Preemption constrained by N and S, excluding decimals """
#ax = fig.add_subplot(3, 2, 2)  # Debug me
#DPI = Models.DomPreInt(N, S, sample_size)
#fig = HeatMap.RACHeatMap(fig, DPI)
# plot hottest RAC
#plt.xlabel(...
#plt.ylabel(...
#print 'finished dominance preemption (integers)'


""" The Dominance Preemption constrained by N and S, allowing decimals """
ax = fig.add_subplot(3, 3, 4)
DPF = Models.DomPreFloat(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, DPF)
# plot hottest RAC
plt.xlabel(...
plt.ylabel(...
print 'finished dominance preemption (decimals)'


""" The Log-normal (75/25) constrained by N and S """
ax = fig.add_subplot(3, 3, 5)
SLN = Models.SimLogNorm(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, SLN)
# plot hottest RAC
plt.xlabel(...
plt.ylabel(...
print 'finished lognormal'


""" Pareto (80/20) constrained by N and S """
ax = fig.add_subplot(3, 3, 7)
SP = Models.SimPareto(N, S, sample_size, integer=False)
fig = HeatMap.RACHeatMap(fig, SP)
# plot hottest RAC
plt.xlabel(...
plt.ylabel(...
print 'finished Pareto'


""" Simple random fraction constrained by N and S """
ax = fig.add_subplot(3, 3, 8)
SRF = Models.Sample_SimpleRandomFraction(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, SRF)
# plot hottest RAC
plt.xlabel(...
plt.ylabel(...
print 'finished simple random fraction'



plt.subplots_adjust(wspace=0.4, hspace=0.4) # adjust space between subplots
plt.savefig(...    # save the figure to a file
plt.show()         # display the figure