# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:09:09 2022

@author: Kuba
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

df_original = pd.read_csv("Diabetes.csv")
print(df_original.head())

#Data prep
cols = [c for c in df_original.columns if c not in ["Pregnancies", "Outcome"]]
df = df_original.copy()
df[cols] = df[cols].replace({0: np.NaN})
#pandas will ignore NaNs in mean ect. calculations