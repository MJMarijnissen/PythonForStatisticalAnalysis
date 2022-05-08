# -*- coding: utf-8 -*-
"""
Created on Sun May  8 18:34:10 2022

@author: Kuba
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

d1 = np.loadtxt("example_1.txt")
d2 = np.loadtxt("example_2.txt")
print(d1.shape, d2.shape)

dataset = pd.DataFrame({
    "value": np.concatenate((d1,d2)),
    "type": np.concatenate((np.ones(d1.shape), np.zeros(d2.shape)))
    })


#%% PLOTTING HISTOGRAMS 

#divide number of bins based on the data whilst assuring both datasets have the
#same ammount of bins: 
    
bins = np.linspace(min(d1.min(), d2.min()), max(d1.max(), d2.max()), 50)
plt.hist(d1, bins = bins, label="D1")
plt.hist(d2, bins = bins, label="D2")
plt.legend()
plt.ylabel("Counts")
plt.show()

#histograms not filled below:
plt.hist(d1, bins = bins, label="D1", density=True, histtype="step", lw=3)
#add density=True to get probability on Y-axis
plt.hist(d2, bins = bins, label="D2", density=True, histtype="step", ls=":")
plt.legend()
plt.ylabel("Probability")
plt.show()

#histograms stacked (easer when overlapping):
plt.hist([d1, d2], bins = bins, label="Stacked", density=True, alpha=0.5)
plt.legend()
plt.ylabel("Probability")
plt.show()
#can also use histtype="barstacked" but it clutters the image a lot

#%% BEE SWARM PLOTS

sb.swarmplot(x="type", y="value", data=dataset, size=2)
plt.show()

#%% BOX PLOTS

sb.boxplot(x="type", y="value", data=dataset, whis=2.0)
#whis controls the interquartile range that dictates the cutoff point for outliners
sb.swarmplot(x="type", y="value", data=dataset, size=2, color="k", alpha=0.3)
plt.show()

#%% VIOLIN PLOTS

sb.violinplot(x="type", y="value", data=dataset, inner="quartile", bw=0.1)
#inner adds quartiles, bw is the smoothing parameter
sb.swarmplot(x="type", y="value", data=dataset, size=2, color="k", alpha=0.3)
plt.show()

#%% EMPIRICAL CUMULATIVE DISTRIBUTION FUNCTIONS

#cdf can be achieved by sorting data from smalest to largest
sd1 = np.sort(d1)
sd2 = np.sort(d2)
#maden an exacter approx below, so it doesn't start from 0 (avoid weird  
#behaviour at 0th and 1st percentile)
cdf = np.linspace(1/d1.size, 1, d1.size)

plt.plot(sd1, cdf, label="D1 CDF")
plt.plot(sd2, cdf, label="D2 CDF")
plt.hist(d1, bins = bins, label="D1 hist", density=True, histtype="step", alpha=0.3)
plt.hist(d2, bins = bins, label="D2 hist", density=True, histtype="step", alpha=0.3)
plt.legend()
plt.show()
