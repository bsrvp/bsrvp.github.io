# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:15:31 2020

@author: srvpr
"""

import numpy as np
import scipy as sp
import pandas as pd
from matplotlib import pyplot as plt

DO = pd.read_csv('http://bsrvp.github.io/data/DOData.csv')
Nut = pd.read_excel('http://bsrvp.github.io/data/NutAverage.xlsx')
Phy = pd.read_excel('http://bsrvp.github.io/data/PhytoBiomass.xlsx')

Nut['DIN'] = Nut['NH4-N'] + Nut['NO2-N'] + Nut['NO3-N']
Nut['DON'] = Nut['TN'] - Nut['DIN']

Nut.iloc[:,1:6].plot.area()

Nut.iloc[:,1:6].plot.box()

Phy['Others'] = Phy.iloc[:,3] - Phy.iloc[:,1] - Phy.iloc[:,2]

Phy.iloc[:,1:6].plot()

DOC = DO.iloc[:,1]
Cyano = Phy.iloc[:,1]
Chloro = Phy.iloc[:,2]
NH4 = Nut.iloc[:,1]
NO3 = Nut.iloc[:,2]

plt.figure()
plt.scatter(DOC, NH4)

plt.figure()
plt.scatter(DOC, NO3)
