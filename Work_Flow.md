# Project Work flow: 3 files

## Models.py

### Functions: 
* list of models

### Notes:  
* This file already exists, just need to add tests to make sure it runs smoothly

## ObsPred.py
### Functions:
* Get SAD
* Get Prediction
* Write ObsPred file

### Notes: 
* Needs work but basics are there
* 	Pilot_Study.py ...

## Analysis.py
### Functions:
* Read ObsPred text files   
* Compare observed SADs to predicted SADs:
	
	Code for Kolmogorov–Smirnov test:  
	scipy.stats.ks_2samp(data1, data2)
	
	Code for Chi Squared:  
	scipy.stats.chisquare(f_obs, f_exp=None, ddof=0, axis=0)
	
	Code for evenness, diversity and dominance  
	found in indices file
	
### Notes: 
Should just require simple lines of code to run tests