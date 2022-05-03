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


#%%
#Rejection of outliners based on standard distribution and Z-score

mean, std = np. mean(d1), np.std(d1)
z_score = np.abs((d1-mean)/std)
threshold = 3
good = z_score < threshold

print(f"Rejection {(~good).sum()} points")
from scipy.stats import norm
print(f"z_score of 3 corresponds to a prob of {100*2*norm.sf(threshold):0.2f}%")
visual_scatter = np.random.normal(size=d1.size)
plt.scatter(d1[good], visual_scatter[good], s=2, label="Good", color="#4CAF50")
plt.scatter(d1[~good], visual_scatter[~good], s=2, label="Bad", color="#F44336")
plt.legend()