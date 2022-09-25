import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')


## 1 - Criar um gráfico com a biblioteca Pandas que mostre a quantidade de pessoas por cidade de embarque, coluna embark_town no dataset.
print(titanic['embark_town'].value_counts().plot.bar(rot=0))

##2 - Criar um gráfico com a biblioteca Pandas que mostre a quantidade de pessoas por cidade de embarque, coluna embark_town no dataset separados pelo sexo, coluna sex no dataset.
print(pd.get_dummies(titanic, columns=(['sex'])).groupby(['embark_town']).sum()[['sex_female','sex_male']].plot.bar(rot=0))

## 3 - Criar um gráfico com a biblioteca Pandas que mostre o percentual pelo sexo das pessoas no Titanic.
print(titanic['sex'].value_counts().plot.pie(autopct='%1.2f%%', wedgeprops={'width': .5}));

## 4 - Criar um gráfico com a biblioteca Pandas que mostre os outliers da idade das pessoas no Titanic, coluna age no dataset.
print(titanic['age'].plot.box())

## 5 - Criar um gráfico com a biblioteca Pandas que mostre os outliers da tarifa de embarque das pessoas no Titanic, coluna fare no dataset.
print(titanic['fare'].plot.box())

## 6 - Criar um gráfico com a biblioteca Pandas que mostre a distribuição de idades das pessoas no Titanic, coluna age no dataset.
print(titanic['age'].plot.hist())

## 7 - Criar um gráfico com a biblioteca Pandas que mostre a distribuição de idades das pessoas no Titanic, coluna age no dataset separados por sexo em dois gráficos.
print(titanic[['age','sex']].dropna().reset_index().pivot('index','sex', 'age').plot.hist(subplots=True))

