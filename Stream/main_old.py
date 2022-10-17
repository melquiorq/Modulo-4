############################################
# Construindo uma aplicação com streamlit  #
#                                          #
# instalação: pip install streamlit        #
#                                          #
# executar: streamlit run main.py          #
#                                          #
# Prof: Tiago Dias                         #
############################################

# importar bibliotecas
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# função principal da aplicação
def app():
    # titulo da aplicação
    st.title('Técnicas de Programação II Python')
    # sub titulo da aplicação
    st.subheader('Aprendendo o Framework Streamlit')
    # ler arquivo csv
    df = pd.read_csv('mpg.csv')
    # adicionar texto na página
    st.markdown('Dimensão da **Base de Dados**')
    # escrever informações do dataset
    st.write('Número de observações', df.shape[0], 'Número de colunas', df.shape[1])
    # adicionar texto na página
    st.markdown('Primeiros registros da **Base de Dados**')
    # exibindo as primeiras linhas do dataframe
    st.dataframe(df.head())
    # adicionar texto na página
    st.markdown('Gráfico de **Barras**')
    # exibindo um gráfico de barras seaborn
    fig, ax = plt.subplots()
    # criando um gráfico de barras
    sns.barplot(data=df, x='origin', y='horsepower', ax=ax)
    # levando o gráfico para a aplicação
    st.pyplot(fig)
    # adicionar texto na página
    st.markdown('Gráfico de **Barras Duplo**')
    # criando o gráfico duplo para entender o ax
    fig, ax = plt.subplots(1,2)
    # fig [[ax0] [ax1]]
    sns.barplot(data=df, x='origin', y='horsepower', ax=ax[0])
    sns.barplot(data=df, x='origin', y='horsepower', ax=ax[1])
    st.pyplot(fig)
    # adicionar texto na página
    st.markdown('Gráfico de **Barras Quadruplo**')
    # criando o gráfico quadruplo para entender o ax
    fig, ax = plt.subplots(2,2)
    # fig [[ax00] [ax01] [ax10] [ax11]]
    sns.barplot(data=df, x='origin', y='horsepower', ax=ax[0][0])
    sns.barplot(data=df, x='origin', y='horsepower', ax=ax[1][0])
    sns.barplot(data=df, x='origin', y='horsepower', ax=ax[0][1])
    sns.barplot(data=df, x='origin', y='horsepower', ax=ax[1][1])
    st.pyplot(fig)
    # adicionar texto na página
    st.markdown('Gráfico de **Barras Plotly**')
    # criando um gráfico de barras no plotly
    fig = px.bar(data_frame=df, x='origin').update_layout(template='presentation')
    # levando o grafico para a aplicação
    st.plotly_chart(fig)
    # adicionar texto na página
    st.markdown('Gráfico de **Dispersão Seaborn**')
    # criando um gráfico de dispersão
    fig, ax = plt.subplots()
    # gerando o gráfico no seaborn
    sns.scatterplot(data=df, x='mpg', y='weight', hue='origin', ax=ax)
    # levando o gráfico para a aplicação
    st.pyplot(fig)
    # adicionar texto na página
    st.markdown('Gráfico de **Dispersão Plotly**')
    # gerando o gráfico no plotly
    fig = px.scatter(data_frame=df, x='mpg', y='weight', color='origin')
    # levando o gráfico para a aplicação
    st.plotly_chart(fig)
    # colocar um check box para o usuário
    if st.checkbox('Gerar dados estatísticos'):
        # criar um selectbox com as colunas do dataframe
        coluna = st.selectbox('Selecione uma coluna', list(df.select_dtypes(include='number').columns))
        # calculos de medida de tendencia central com a coluna seleciona pelo usuário
        media = df[coluna].mean()
        mediana = df[coluna].median()
        moda = df[coluna].mode().max()
        # exibindo os cálculos na tela com write
        st.write('media:', media)
        st.write('mediana:', mediana)
        st.write('moda:', moda)
        # criar botão para gerar dados em um dataframe
        if st.button('Gerar dataframe estatístico'):
            # exibindo dados do dataframe após ação do botão
            st.dataframe({'Valor': {'1 - media': media,
                                    '2 - mediana': mediana,
                                    '3 - moda': moda}})
        # Input de texto do usuário
        texto = st.text_input('Digite o seu nome!!! Você chegou ao final da aplicação!!!')
        # Escrevendo o texto do usuário na tela
        if texto:
            st.write('Obrigado', texto, 'volte sempre!!!')

# chamada para executar a aplicação principal
if __name__ == '__main__':
    app()

