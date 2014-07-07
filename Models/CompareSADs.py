import sys

mydir = '/Users/lisalocey/Desktop/SADModels'
sys.path.append(mydir)
import RandFrac


""" This script does whatever... 


    generates a figure that either compares different models
    or compares models to data
    or compares data to data
    
    """


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



