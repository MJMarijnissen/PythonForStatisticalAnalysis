# -*- coding: utf-8 -*-
"""
Created on Mon May  2 11:24:26 2022

@author: Kuba
"""

import pandas as pd
import numpy as np

df = pd.read_csv("Diabetes.csv")

#Getting rid of N/A values:
df = df.fillna(0)
#df.dropna()

df2 = df[["Glucose", "BMI", "Age", "Outcome"]]

print(df2.describe())

#deleting all rows that have 0 in them (~ inverses the relation): 
df3 = df2.loc[~(df2[df2.columns[:-1]] == 0).any(axis=1)]

print(df3.describe())

#Exploring data

print(df3.groupby("Outcome").mean())
#agg takes in dictionairy that allows to change which values are taken
print(df3.groupby("Outcome").agg({"Glucose": "mean", "BMI": "median"}))
#when given list it will show both values: 
print(df3.groupby("Outcome").agg(["mean", "median"]))

#Dividing data

postive = df3.loc[df3["Outcome"] == 1]
negative = df3.loc[df3["Outcome"] == 0]

print(postive.shape,negative.shape)

#Exporting data

df3.to_csv("clean_diabetes.csv", index=False)