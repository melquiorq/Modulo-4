# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 20:29:20 2022

@author: Melk, Dalmir , Williarde
"""
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


def app():
    
    from PIL import Image
    
    ##Add imagem
    image =Image.open(r'C:\Users\bande\OneDrive\Documentos\GitHub\Modulo-4\Stream\logo.jpg')
    
    ##Levando imagem para a aplicação
    st.image(image, caption='2022')
        
    ## Add titulo na aplicação
    st.title('TECNICAS DE PROGRAMAÇÃO II')
    
    ## Colorindo texto Courier
    color = '<p style="font-family:Georgia Bold; color:Blue; font-size: 20px;"><b>************************** PROJETO FINAL **************************</b></p>'
    ## Add subtitulo
    st.markdown(color, unsafe_allow_html=True)
    ## Add upload de arquivo
    upload = st.file_uploader('Carregar DataFrame desejado')
    if upload is not None:
        data = upload.getvalue()
        ##Carregando data Frame
        dt = pd.read_csv(upload)
        ## Colorindo texto
        color = '<p style="font-family:Georgia Bold; color:Black; font-size: 20px;"><b>Dimensão do DataFrame</b></p>'
        ## Add texto na página 
        st.markdown(color, unsafe_allow_html=True)
        ## Add informações basicas 
        st.write('Número de linhas: ',dt.shape[0], 'Número de colunas: ', dt.shape[1] )
        ##Tratando o DataFrame
        dt_1 = dt.isnull().sum()[dt.isnull().sum()>0].reset_index()
        dt_2 = (dt.isnull().sum()/len(dt)*100).reset_index()
        dt_final = dt_1.merge(dt_2, how='inner', on='index', )
        dt_final.rename(columns={'index':'informações','0_x': 'Nulos', '0_y': 'Percentual'},inplace = True)
        ## Colorindo texto
        color = '<p style="font-family:Georgia Bold; color:Black; font-size: 20px;"><b>Informações básicas do Data Frame</b></p>'
        ## Add texto na página
        st.markdown(color, unsafe_allow_html=True)
        ## Add RadioBox 
        radio_B1 = st.radio('Marque a opção desejada', ('Info','Describe', 'Head'))
        ## Configurando botões RadioBox
        if radio_B1 == 'Info': 
            st.dataframe({ 'Non-Null Count': dt.count(),'Dtype': list(map(str,dt.dtypes))})
            ##st.write(dt.info())
            
        elif radio_B1 == 'Describe':
            st.write(dt.describe())
        else:
            st.write(dt.head())
        ##Criando figura do gráfico
        if st.checkbox('Exibir dados Nulos'):
            st.write(dt_final.head())
        if st.checkbox('Exibir gráfico de percentual de nulos'):
            ##Criando figura do gráfico
            fig, ax = plt.subplots()
            ## Criando o gráfico
            sns.barplot(data=dt_final, x=dt_final['Nulos'], y=dt_final['Percentual']);
            ## Levando o gráfico para aplicação
            st.pyplot(fig)
        ## Colorindo e formatando texto
        color = '<p style="font-family:Georgia Bold; color:Black; font-size: 20px;"><b>Análise de Gráficos</b></p>'
        ## Add texto na página 
        st.markdown(color, unsafe_allow_html=True)
        
        ##RadioBox para escolha do Gráfico desejado
        radio_B2 = st.radio('Escolha o tipo de dados', ('Numéricos','Todos'))
        
        if radio_B2 == 'Numéricos': 
            coluna1 = st.selectbox('Selecione a primeira coluna', list(dt.select_dtypes(include='number').columns))
            coluna2 = st.selectbox('Selecione a segunda coluna', list(dt.select_dtypes(include='number').columns))
            fig = px.scatter(data_frame=dt, x=coluna1, y=coluna2, color=coluna1)
            st.plotly_chart(fig)
        else:
            coluna1 = st.selectbox('Selecione a primeira coluna', list(dt.select_dtypes(exclude='number').columns))
            fig = px.bar(data_frame=dt, x=coluna1, color=coluna1)
            st.plotly_chart(fig)
  
        if st.checkbox('Apresentar Gráfico de percentual'):
                coluna3 = st.selectbox('Selecione a coluna para análise', list(dt.select_dtypes(exclude='number').columns))
                labels = dt[coluna3].value_counts().head(10).index
                valor = dt[coluna3].value_counts().head(10).values
                fig, ax=plt.subplots()
                plt.pie(valor, labels=labels, autopct='%1.2f%%')
                st.pyplot(fig)
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    app()

