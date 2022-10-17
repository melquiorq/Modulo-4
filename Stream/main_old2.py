# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:20:49 2022

@author: bande
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st



def app():
    
    ## Add titulo na Página da aplicação
    st.title('TECNINCAS DE PROGRAMAÇÃO II EM PYTHON')
    ## Add um subtitulo na página da aplicação
    st.subheader('Apresentação de análise de dados ')
    ## Lear o arquivo do dataframe
    dtf = pd.read_csv(r'C:\Users\bande\OneDrive\Documentos\GitHub\Modulo-4\Stream\mpg.csv')
    ## Add texto na página da aplicação
    st.markdown('EXIBINDO DADOS INICIAIS DO DATA FRAME')
    ## Carrgando data Frame na aplicação
    st.dataframe(dtf.head())
    ## Colorindo texto 
    color = '<p style="font-family:Courier; color:Red; font-size: 20px;"><b>****** EXIBINDO GRÁFICO DE BARRAS ******</b></p>'
    ## Add texto na página da aplicação
    st.markdown(color, unsafe_allow_html=True)
    ## Criando figura do plot. 
    fig, ax = plt.subplots()
    ## Criando o gráfico
    sns.barplot(data=dtf,x='origin', y='horsepower', hue='origin', ax=ax)
    ## Levando gráfico para aplicação
    st.pyplot(fig)
    ## Colorindo texto
    color = '<p style="font-family:Courier; color:Red; font-size: 20px;"><b>****** EXIBINDO GRÁFICO DE BARRAS DUPLO ******</b></p>'
    ## Add texto na base
    st.markdown(color, unsafe_allow_html=True)
    ## Criando figura do plot    
    fig, ax = plt.subplots(1,2)
    ## Criando o gráfico
    sns.barplot(data=dtf, x='origin', y='horsepower', hue='origin', ax=ax[0])
    sns.barplot(data=dtf, x='origin', y='horsepower', hue='origin', ax=ax[1])
    ##Levando gráfico para aplicação
    st.pyplot(fig)
    ## Colorindo texto
    color = '<p style="font-family:Courier; color:Red; font-size: 20px;"><b>****** EXIBINDO GRÁFICO DE BARRAS QUADRUPLO ******</b></p>'
    ## Add texto na página
    st.markdown(color, unsafe_allow_html=True)
    ## Criando figura do plot. 
    fig, ax = plt.subplots(2,2)
    ## Criando os gráficos 
    sns.barplot(data=dtf, x='origin', y='horsepower', hue='origin', ax=ax[0][0])
    sns.barplot(data=dtf, x='origin', y='mpg', hue='origin', ax=ax[0][1])
    sns.barplot(data=dtf, x='origin', y='horsepower', hue='origin', ax=ax[1][0])
    sns.barplot(data=dtf, x='origin', y='horsepower', hue='origin', ax=ax[1][1])
    ## Levando gráficos para a aplicação
    st.pyplot(fig)
    ## Colorindo texto
    color = '<p style="font-family:Courier; color:Red; font-size: 20px;"><b>****** EXIBINDO GRÁFICO DE BARRAS PLOTLY ******</b></p>'
    ## Add texto na página
    st.markdown(color, unsafe_allow_html=True)
    ## Criando o gráfico
    fig = px.bar(data_frame=dtf, x='origin',y='mpg',color='origin').update_layout(template='plotly_dark')
    ## Levando o gráfico para a aplicação
    st.plotly_chart(fig)
    
    dtf['media_mpg'] = dtf['mpg'].sum()/dtf['mpg']
    dtf.head()
       
    
    
if __name__ == '__main__':
    app()