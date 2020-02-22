# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:15:31 2020

@author: srvpr
"""

import numpy as np
import scipy as sp
from scipy import optimize, stats, linspace, polyfit, interpolate
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

Days = Nut.iloc[:,0]
DOC = DO.iloc[:,1]
Cyano = Phy.iloc[:,1]
Chloro = Phy.iloc[:,2]
NH4 = Nut.iloc[:,1]
NO3 = Nut.iloc[:,3]

DOint = interpolate.interp1d(Days, DOC, kind='cubic')
TotDays = np.linspace(1,364,364)
plt.figure()
plt.plot(Days, DOC, 'ro', TotDays, DOint(TotDays), '--g')

def f(x,a,b):
    return a*x+b

popt, cov = optimize.curve_fit(f, Nut.iloc[:,4], DOC)

plt.figure()
plt.plot(Nut.iloc[:,4], DOC, 'ro', Nut.iloc[:,4], f(Nut.iloc[:,4], *popt), '--g')

(a_s, b_s, r, tt, stderr) = stats.linregress(Nut.iloc[:,4], DOC)
xDOC = np.polyval([a_s, b_s], Nut.iloc[:,4])

plt.figure()
plt.plot(Nut.iloc[:,4], DOC, 'ro', Nut.iloc[:,4], xDOC, '--g')