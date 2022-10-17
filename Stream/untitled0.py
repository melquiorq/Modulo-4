# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:18:09 2022

@author: bande
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dtf = pd.read_csv(r'C:\Users\bande\OneDrive\Documentos\GitHub\Modulo-4\Stream\Port_Data.csv')
labels = dtf['Country'].value_counts().head().index
valor = dtf['Country'].value_counts().head().values
fig, ax=plt.subplots()
ax.pie(valor, labels=labels, autopct='%1.2f%%')
plt.show()