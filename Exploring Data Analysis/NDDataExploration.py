# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:09:09 2022

@author: Kuba
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
from chainconsumer import ChainConsumer

df_original = pd.read_csv("Diabetes.csv")
print(df_original.head())
df3 = pd.read_csv("height_weight.csv")

#Data prep
cols = [c for c in df_original.columns if c not in ["Pregnancies", "Outcome"]]
df = df_original.copy()
df[cols] = df[cols].replace({0: np.NaN})
#pandas will ignore NaNs in mean ect. calculations
m = df3["sex"] == 1
params = ["height", "weight"]
male = df3.loc[m, params].values
female = df3.loc[~m, params].values

#%% SCATTER MATRIX

df2=df.dropna()
colors = df2["Outcome"].map(lambda x: "#44d9ff" if x else "#f95b4a")
pd.plotting.scatter_matrix(df, figsize=(7,7), color=colors)

#%% SCATTER PLOT

plt.scatter(df3.loc[m,"height"], df3.loc[m,"weight"], s=1, label="Male")
plt.scatter(df3.loc[~m,"height"], df3.loc[~m,"weight"], s=1, label="Female")
plt.xlabel("height")
plt.ylabel("weight")
plt.legend()
plt.show()

#%% CORRELATION MATRIX

#can also be achieved with: 
#print(df.corr())
sb.heatmap(df.corr(), annot=True, cmap="viridis", fmt="0.2f")

#%% 2D Histograms

plt.hist2d(x="height", y="weight", data=df3, bins=20, cmap="magma")
plt.xlabel("height")
plt.ylabel("weight")
plt.show()

#%% KDE Plots

sb.kdeplot(x="height", y="weight", data=df3, cmap="viridis")
#use bw=tuple to affect the Gaussian plot smoothing for x and y
plt.hist2d(x="height", y="weight", data=df3, bins=20, cmap="magma", alpha=0.3)
plt.xlabel("height")
plt.ylabel("weight")
plt.show()

sb.kdeplot(x="height", y="weight", data=df3, cmap="viridis", shade=True)
plt.show()

#%% USING CHANCONSUMER

#plots 2 contours: 68 percent confidence interval and 95 percent conf. int.
c=ChainConsumer()
c.add_chain(male, parameters=params, name="Male", kde=1.0, color="b")
c.add_chain(female, parameters=params, name="Female", kde=1.0, color="r")
c.configure(contour_labels="confidence", usetex=False)
c.plotter.plot(figsize=2.0)

c.plotter.plot_summary(figsize=2.0)