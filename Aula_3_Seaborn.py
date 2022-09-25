import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

## 1 - Qual o valor médio da gorjeta de acordo com o dia da semana?
sns.barplot(data=tips, x='day', y='tip')

## 2 - Qual a soma das gorjetas por turno do dia, observando os fumantes e não fumantes?
sns.barplot(data=tips, x='time', y='tip', hue='smoker', estimator=sum)


## 3 - Crie uma coluna calculada com o valor da gorjeta por pessoa. Em seguida crie dois gráficos, um com o valor médio da gorjeta de acordo com a quantidade de pessoas da conta e outro com o valor médio da gorjeta individual também de acordo com a quantidade de pessoas da conta.
tips['gorjxpessoa']= tips['tip']/tips['size']

##A)
sns.barplot(data=tips, x='size',y='gorjxpessoa' )

##B)
sns.barplot(data=tips, x='size', y='tip')

## 4 - Qual a relação do valor total da conta com o valor da gorjeta?
sns.scatterplot(data=tips, x='total_bill', y='tip')

## 5 - Qual público dá maior quantidade de gorjetas:

    ## A) Homens ou mulheres?
    ## B) Fumantes ou não fumantes?'''
## A)
sns.countplot(data=tips, y='sex')
## B)
sns.countplot(data=tips, y='smoker')

## 6 - Quando temos a maior e a menor soma de gorjetas:
    
    ## A) Qual dia da semana?
    ## B) Qual turno do dia??
    
## A) 
sns.barplot(data=tips, x='day', y='tip', estimator=sum)

## B) 
sns.barplot(data=tips, x='time', y='tip', estimator=sum)

