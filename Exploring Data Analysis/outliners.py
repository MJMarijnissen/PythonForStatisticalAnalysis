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