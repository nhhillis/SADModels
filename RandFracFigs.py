from __future__ import division
import sys
import Models 
sys.path.append('/Users/Nathan_Hillis/SADModels/tools/')
import HeatMap
import matplotlib.pyplot as plt

N = 1000
S = 50
sample_size = 200

fig = plt.figure()

ax = fig.add_subplot(3,2,1)
BrkStk = Models.SimBrokenStick(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, BrkStk)

ax = fig.add_subplot(3,2,2)
DPI = Models.DomPreInt(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, DPI)

ax = fig.add_subplot(3,2,3)
DPF = Models.DomPreFloat(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, DPF)

ax = fig.add_subplot(3,2,4)
SLN = Models.SimLogNorm(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, SLN)

ax = fig.add_subplot(3,2,5)
SP = Models.SimPareto(N, S, sample_size, integer=False)
fig = HeatMap.RACHeatMap(fig, SP)

ax = fig.add_subplot(3,2,6)
SRF = Models.Sample_SimpleRandomFraction(N, S, sample_size)
fig = HeatMap.RACHeatMap(fig, SRF)

plt.show()