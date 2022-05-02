# -*- coding: utf-8 -*-
"""
Created on Mon May  2 11:24:26 2022

@author: Kuba
"""

import pandas as pd
import numpy as np

df = pd.read_csv("Diabetes.csv")

df = df.fillna(0)
#df.dropna()

df2 = df[["Glucose", "BMI", "Age", "Outcome"]]

print(df2.describe())

#deleting all rows that have 0 in them (~ inverses the relation): 
df3 = df2.loc[~(df2[df2.columns[:-1]] == 0).any(axis=1)]

print(df3.describe())