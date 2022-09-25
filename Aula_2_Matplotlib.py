# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:02:03 2022

@author: bande
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

mpg = sns.load_dataset('mpg')

## 1 - Verificar se a base de dados possui valores nulos. Para as linhas com valores nulos, deletar as mesmas. Ao final da questão verificar se a base de dados ficou com 392 registros e 9 colunas.
print(mpg.isnull().sum())
mpg.dropna(inplace=True)
print(mpg.shape)

## 2 - Qual a quantidade de carros por origem?
mpg['origin'].value_counts()
x = mpg['origin'].value_counts().index
y = mpg['origin'].value_counts().values
print(plt.bar(x,y));

## 3 - Qual a proporção de carros por origem
print(plt.pie(y, labels=(x), autopct=('%1.2f%%')))

## 4 - Qual a média da potência dos carros por origem

mpg.groupby(['origin']).mean()['horsepower']
x=mpg.groupby(['origin']).mean()['horsepower'].index
y=mpg.groupby(['origin']).mean()['horsepower'].values
print(plt.bar(x,y));

## 5 - Qual a correlacão da potência com a aceleração cos carros?

print(plt.scatter('horsepower','acceleration' , data=mpg));


## 6 - Qual a correlacão da potência com a aceleração dos carros, dando destaque para as origens com cores diferentes?

print(plt.scatter('horsepower','acceleration',data=mpg[mpg['origin']=='usa'],c='green', label='usa'))
print(plt.scatter('horsepower','acceleration',data=mpg[mpg['origin']=='europe'],c='black',label='europe'))
print(plt.scatter('horsepower','acceleration',data=mpg[mpg['origin']=='japan'],c='blue',label='japan'))










