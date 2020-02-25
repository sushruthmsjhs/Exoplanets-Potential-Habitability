import pandas as pd
import math
import array
import numpy as np
exoplanet = pd.read_csv("/Users/sushruth/Desktop/ASDRP/DataSetExoplanets.csv")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(exoplanet)
for i in range(0,3972):
    time  = exoplanet.loc[i, 'pl_orbper']*365*3600*24
    distance = exoplanet.loc[i, 'pl_orbsmax']
    G = 6.67*10**-11
    mass = 4*math.pi**2*distance**3 / G /(time**2)
    print(mass)
