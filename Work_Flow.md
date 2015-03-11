# Housekeeping
## README.md 
Needs to be updated, reviewed, edited for accuracy and completeness

## Folders 
**Models folder**  
There are 11 files. There should be 2: 

* models.py: contains functions for the models
* test.py: contains function that test model code

**Projects folder**  
There should be a folder named "Projects". This can contain code from your IRB project, etc.

**Tools folder:** 
Included files provided by KJL, either coded or provided through Weecology GitHub repos.

# Project Work flow (3 files)
## File 1: models.py

**Location:** Models folder  

**Functions:**  
* list of models

**Notes:**  
* This file already exists
* Need to add test.py file to make sure that functions in models.py run *correctly*


## File 2: obs_pred.py
**Location:** Analysis folder  

**Functions:**  

* Get empirical SADs
* Get predicted SADs
* Write empirical and predicted SADs to a file (obs_pred.txt)

**Notes:**  

* Needs work but basics are there...borrow from Pilot_Study.py


## File 3: analysis.py
**Location:** Projects folder  
**Functions:**

* Read ObsPred text files   
* Compare observed SADs to predicted SADs:

Code needed:

	One-to-one plots: This is in the Analysis folder -KL.
	
	Kolmogorov–Smirnov test (two-tailed):  
	scipy.stats.ks_2samp(data1, data2)
	
	Chi-squared:  
	scipy.stats.chisquare(f_obs, f_exp=None, ddof=0, axis=0)
	
	Metrics: evenness, diversity, dominance, skewness (rarity)
	All are found within Indices.py (provided by KJL)
	
### Notes: 
Should just require simple lines of code to run tests