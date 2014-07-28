What I did since we last talked:

1.
I worked on RandFracFigs, Models.py, HeatMap, and other. I added function to Models that finds percent relative abundances. Relative abundance works better for decimals (floats) but doesn’t remove the large disparity between very abundant species and very rare ones. So…

2.
I switched to using the log of the percent abundances, i.e. get the relative abundance of a species, then multiply it by 100, and then log-transform that number. I did this because 1.) using relative abundance makes more sense when abundances can take decimal values and values less than 1.0, and 2.) using relative abundance also produces curves that are so uneven, it is hard to interpret them (as with arithmetic abundance). So I simply find the relative abundance of a species, turn it into a percent by multiplying by 100, and then log transform it. In the end, it produces typical RAC shapes and can be visually interpreted. 

3. 
I created a figures directory and amended RandFracFigs.py to place figures in that directory.

4. 
I beautified the figure that results from RandFracFigs.py

5. 
I added a keyword argument to the model calls. For example…
RACsample = Models.SimBrokenStick(N, S, sample_size, rel=True)  …rel is a variable that instructs SimBrokenStick to produce RACs of log transformed % abundances.

6. I revised AvgShape function in the AverageShape.py file. Because we are allowing decimal values in some cases, ‘overlap’ at ranks is very unlikely because the are many possible decimals values between, say, 1 and 2. So instead of counting ‘overlap’, I changed the code to calculate average differences. We then pick the RAC with the smallest average differences among ranks to all other RACs, and in the case of a tie, we choose the one with the smallest variance in differences among ranks.



