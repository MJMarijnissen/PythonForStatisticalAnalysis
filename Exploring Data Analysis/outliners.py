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
#Rejection of 1-D outliners based on standard distribution and Z-score

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

#%%
#Rejection of 2-D outliners based on multivariate normal

from scipy.stats import multivariate_normal as mn

mean, cov = np.mean(d2,axis=0), np.cov(d2.T)
good = mn(mean, cov).pdf(d2) > 0.01 /100

plt.scatter(d2[good, 0], d2[good, 1], s=2, label="Good", color="#4CAF50")
plt.scatter(d2[~good, 0], d2[~good, 1], s=2, label="Bad", color="#F44336")
plt.legend()

#%%
#Rejection of curve outliners using polyfit

xs, ys = d3.T
p = np.polyfit(xs, ys, deg=5)
ps = np.polyval(p, xs)

plt.plot(xs, ys, ".", label = "Data")
plt.plot(xs, ps, label = "Bad poly fit")
plt.legend()

x, y = xs.copy(), ys.copy()
for i in range(5):
    p = np.polyfit(x, y, deg=5)
    ps = np.polyval(p,x)
    good = y- ps <3 #no negative outliners, no need for abs
    
    x_bad, y_bad, = x[~good], y[~good]
    x, y = x[good], y[good]
    
    plt.plot(x, y, ".", label ="Used Data")
    plt.plot(x, np.polyval(p,x), label=f"Poly fit {i}")
    plt.plot(x_bad, y_bad, ".", label="Not used Data")
    plt.legend()
    plt.show()
    
    if (~good).sum() == 0:
        break
    
#%%
#Rejection of 2-D outliners using automated sklearn

from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.01)
good = lof.fit_predict(d2) == 1

plt.scatter(d2[good, 0], d2[good, 1], s=2, label="Good", color="#4CAF50")
plt.scatter(d2[~good, 0], d2[~good, 1], s=2, label="Bad", color="#F44336")
plt.legend()