# -*- coding: utf-8 -*-
"""
Created on Sun May  8 18:34:10 2022

@author: Kuba
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn
import pandas as pd

d1 = np.loadtxt("example_1.txt")
d2 = np.loadtxt("example_2.txt")
print(d1.shape, d2.shape)