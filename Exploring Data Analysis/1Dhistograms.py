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

#%%
#ploting histograms 

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