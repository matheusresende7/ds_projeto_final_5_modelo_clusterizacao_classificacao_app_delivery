import math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



# --------------------------------------------------GRÁFICOS INDIVIDUAIS---------------------------------------------------------------------



def pairplots( # Função para criar gráficos pairplots
    df, # Passando o df como parâmetro da função
    columns, # Passando as colunas como parâmetro da função
    hue = None, # Passando o hue como parâmetro da função
    alpha = 0.5, # Passando o alpha como parâmetro da função
    corner = True, # Passando o corner como parâmetro da função
):
    
    analysis_columns = columns.copy() + [hue] # Adicionando a coluna hue as colunas que vão ser analisadas
    
    sns.pairplot( # Criando o gráfico pairplots
        df[analysis_columns], # Passando as colunas que serão usadas nos pairplots
        diag_kind="kde", # Definindo o tipo curva
        hue=hue, # Definindo o parâmetro hue (legenda)
        plot_kws=dict(alpha=alpha), # Definindo a transparência da plotagem dos gráficos
        corner=corner, # Definindo o pairplots apenas na parte espelhada inferior
    )



# --------------------------------------------------LISTA DE GRÁFICOS------------------------------------------------------------------------



def boxplots( # Função para criar gráficos boxplot
    df, # Passando o df como parâmetro da função
    columns, # Passando as colunas Y como parâmetro da função
    x = None # Passando as colunas X como parâmetro da função
): 
    columns = columns # Passando as colunas que vão ser usadas para criar os boxplots

    fig, axs = plt.subplots( # Criando a figura para colocar os gráficos de boxplots
        nrows=1, # Definindo o número de linhas
        ncols=3, # Definindo o número de colunas
        figsize=(12,4), # Definindo o tamanho da figura
        tight_layout=True # Definindo o layout mais justo dos gráficos
    )

    for i, column in enumerate(columns): # Criando uma estrutura de repetição para criar cada um dos boxplots
        sns.boxplot( # Criando o boxplot
            x=x, # Passando a coluna x que permite criar comparações em relação a alguma variável (geralmente categórica)
            y=column, # Passando a coluna de referência para criar o boxplot
            data=df, # Passando o dataframe para criar o boxplot
            ax=axs[i], # Passando a posição do gráfico dentro da plotagem do matplotlib
            showmeans=True, # Exibindo a média no boxplot, através de um triângulo verde
        )
        axs[i].set_title(f'Boxplot - {column}', fontsize=12)  # Adiciona um título para cada boxplot
        axs[i].set_ylabel('') # Removendo o título do eixo Y

    plt.show() # Exibindo os boxplots



def histplots( # Função para criar gráficos histplots
    df, # Passando o df como parâmetro da função
    hue = None, # Passando o hue como parâmetro da função
    num_cols = 3, # Passando o número de colunas como parâmetro da função
    alpha = 0.5, # Passando o alpha como parâmetro da função
    kde=False, # Passando o kde como parâmetro da função
):

    num_cols = num_cols # Definindo o número de gráficos por linha, ou seja, as quantidade de colunas
    total_columns = len(df.columns) # Definindo o total de colunas do dataset
    num_rows = math.ceil(total_columns / num_cols) # Calculando quantas linhas serão necessárias

    fig, axs = plt.subplots( # Criando a figura com os subplots
        nrows=num_rows, # Passando o número de linhas da figura
        ncols=num_cols, # Passando o número de colunas da figura
        figsize=(20, 5*num_rows), # Definindo o tamanho da figura
        tight_layout=True, # Definindo o layout mais justo dos gráficos
    )

    for i, column in enumerate(df.columns): # Criando a estrutura de repetição para criar os gráficos
        row = i // num_cols # Definindo o índice da linha
        col = i % num_cols # Definindo o índice da coluna

        sns.histplot( # Criando o histograma
            data=df, # Passando o dataframe para criar o gráfico
            x=column, # Passando as colunas para criar o gráfico
            hue=hue, # Definindo o parâmetro hue (legenda)
            alpha=alpha, # Definindo a transparência do gráfico
            kde=kde, # Exibindo o KDE
            ax=axs[row, col] # Posicionando o gráfico em seu devido subplot dentro da figura
        )
        axs[row, col].set_title(f'Histplot - {column}') # Adicionando título para cada subplot
        axs[row, col].set_xlabel('') # Removendo título do eixo x
        axs[row, col].set_ylabel('') # Removendo título do eixo y


    if total_columns % num_cols != 0: # Removendo subplots vazios (se houver um número ímpar de colunas)
        for subplot in range(total_columns, num_rows * num_cols): # Criando a estrutura de repetição para remover os subplots vazios (em um range do total de colunas até o último subplot previsto)
            fig.delaxes(axs.flatten()[subplot]) # Removendo o subplot

    plt.show() # Exibindo a figura com os gráficos