import pandas as pd
import seaborn as sns
import numpy as np
import math
import array

exoplanets = pd.read_csv("/Users/sushruth/Desktop/ASDRP/DataSetExoplanets.csv")
print(exoplanets)
for i in range(0,3971):
    luminosity = 10**(exoplanets.loc[i,'st_lum'])
    boltzmann  = 1.380649*10**-23
    
