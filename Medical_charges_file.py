# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 13:05:11 2020

@author: anushka singh
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("insurance.csv")
data.head()
data.info()

#Checking for the null values
data.isnull().sum()
data.age.value_counts()

 

