# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 21:02:40 2022

@author: Kuba
"""

import numpy as np
import pickle 
import pandas as pd

filename = "load.csv"

cols = None
data = []
with open(filename) as f:
    for line in f.readlines():
        vals = line.replace("\n",'').split(",")
        if cols is None:
            cols = vals
        else:
            data.append([float(x)for x in vals])
            
d0 = pd.DataFrame(data, columns=cols)
d0.head()