from __future__ import division # import this module if you do ANY mathematics

import sys   # this module does this ...
import csv   # saving RAC_samples as csv file not sure how to determine where it saves yet
             # the csv module might not be necessary

username = 'lisalocey'
mydir = '/Users/'+ username + '/Desktop/SADModels/'

sys.path.append(mydir)
import tools
sys.path.append(mydir + 'Models/')
import BrokenStick, RandFrac


""" Code in this file will be used to examine SADs of different models. Right
    now it's a bit of a shambles, largely because Ken is messing with stuff.
    But that's the way the cookie self-organizes into a sentient being. """


RAC_samples = simple_random_fraction(N, S, sample_size)


RAC_mean = [sum(x)/len(x) for x in itertools.izip(*RAC_samples)] #find mean for the lists in lists
sample_RAC = [RAC_samples]
print sample_RAC


out=open('sample_RAC.csv','wb')
output=csv.writer(out)
for row in sample_RAC:
    output.writerow(row)
out.close()


RAC_hist = plt.hist(RAC_mean, bins=1000) #attempt to plot as histogram (not coming out right)
plt.title("RAC_Mean")
plt.show(RAC_hist)

RAC_plot = plt.plot(RAC_mean) # plots RAC mean
plt.ylabel('RAC')
plt.show()

print RAC_samples
print RAC_mean


N = 100
S = 4
size = 10


# 1. import some data from CBC files
# 2. get all N, S combinations
# 3. get expected RAC for each



algorithm = 'simple random fraction'
expected_RAC = RandFrac.get_expectedRAC(N, S, size, algorithm )

figure = plt.figure(1,2,1)
RandFrac.get_heat(fig)


print expected_RAC


rand_sample = RandFrac.get_sample(...)

# below are function and such to do something with rand_sample...plot, compare,
# etc. 



