# -*- coding: utf-8 -*-
"""
Created on Mon May  2 12:11:27 2022

@author: Kuba
"""

import numpy as np
import matplotlib.pyplot as plt

d1 = np.loadtxt("outlier_1d.txt")
d2 = np.loadtxt("outlier_2d.txt")
d3 = np.loadtxt("outlier_curve.txt")
print(d1.shape,d2.shape)

#created data points with contamination
plt.scatter(d1, np.random.normal(7, 0.2, size=d1.size), s=1, alpha=0.5)
plt.scatter(d2[:,0],d2[:,1])
plt.show()
plt.plot(d3[:,0],d3[:,1])