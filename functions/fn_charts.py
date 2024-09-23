import os
import sys
sys.path.append('..')
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import CenteredNorm, ListedColormap
from matplotlib.cm import ScalarMappable
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import params.consts as consts



os.environ["OMP_NUM_THREADS"] = "9" # Alterando essa variável de ambiente para evitar erros equivocados



# --------------------------------------------------GRÁFICOS INDIVIDUAIS---------------------------------------------------------------------



def boxplot( # Função para criar gráficos boxplot
    dataframe, # Passando o dataframe como parâmetro da função
    column, # Passando as colunas como parâmetro da função
    hue_column = None, # Passando o hue como parâmetro da função
):
    
    if isinstance(column, list) and len(column) == 1: # Verificando se a lista contém apenas 1 item, se tiver converter para string
        column = str(column[0])
    
    ax = sns.boxplot( # Criando o boxplot
        data=dataframe, # Passando o dataframe para criar o boxplot
        x=hue_column, # Passando a coluna x que permite criar comparações em relação a alguma variável (geralmente categórica)
        y=column, # Passando a coluna de referência para criar o boxplot
        hue=hue_column, # Passando a hue column
        showmeans=True, # Exibindo a média no boxplot, através de um triângulo verde
    )
    ax.set_title(f'Boxplot - {column}') # Adicionando título para cada subplot
    ax.set_xlabel('') # Removendo o título do eixo x
    ax.set_ylabel('') # Removendo o título do eixo y

    plt.show() # Exibindo a figura com os gráficos



def heatmap( # Função para criar gráfico heatmap
    dataframe, # Passando o dataframe como parâmetro da função
):
    
    fig, ax = plt.subplots( # Criando a figura
        figsize=(8,8) # Definindo o tamanho da figura
    )

    sns.heatmap( # Criando o heatmap
        dataframe, # Passando o dataframe para o heatmap
        annot=True, # Exibindo o valores no gráfico
        ax=ax, # Posicionando o gráfico na figura
        fmt='.1f', # Definindo o formato dos valores do gráfico
        cmap='coolwarm_r', # Definindo a escala de cores
        annot_kws={"size": 6}, # Definindo a fonte dos textos no gráfico
    )
    ax.set_title('Heatmap') # Adicionando título para o gráfico
    ax.set_xticklabels(ax.get_xticklabels(), fontsize=6) # Ajustando a fonte dos títulos do eixo x
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=6) # Ajustando a fonte dos títulos do eixo y

    colorbar = ax.collections[0].colorbar # Armazenando em uma variável a barra de cores
    colorbar.ax.tick_params(labelsize=6) # Ajustando a fonte da barra de cores

    plt.show() # Exibindo a figura com o gráfico



def barplot( # Função para criar gráfico barplot
    dataframe, # Passando o dataframe como parâmetro da função
    column, # Passando a column como parâmetro da função
    halfrange, # Passando o halfrange como parâmetro da função
    title = None, # Passando o title como parâmetro da função
):
    
    cmap = 'coolwarm_r' # Definindo a paleta de cores
    cnorm = CenteredNorm(
        vcenter=0, # Definindo o centro do gráfico
        halfrange=halfrange # Definindo o máximo de valores do gráfico
    )
    smap = ScalarMappable(norm=cnorm, cmap=cmap) # Criando uma mapa de cores

    listed_colors = ListedColormap([smap.to_rgba(x) for x in column]).colors # Armazenando o gradiente de cores em uma variável
    
    fig, ax = plt.subplots( # Criando a figura
        figsize=(14,4) # Definindo o tamanho da figura
    )

    b = sns.barplot( # Criando o gráfico
        x=dataframe.index, # Definindo o valor de x
        y=column, # Definindo o valor de y
        hue=dataframe.index, # Definindo o valor de hue
        palette=listed_colors, # Definindo a paleta de cores
        legend=False, # Desligando a legenda
    )
    b.tick_params(axis='x', rotation=90) # Girando os títulos do eixo x em 90°
    b.set_title(f'Barplot - {title}') # Definindo o título
    b.set_xlabel('') # Removendo o título do eixo x
    b.set_ylabel('Correlation') # Definindo o título do eixo y

    plt.show() # Exibindo a figura com o gráfico



# --------------------------------------------------LISTA DE GRÁFICOS------------------------------------------------------------------------



def boxplots( # Função para criar listas de gráficos boxplots
    dataframe, # Passando o dataframe como parâmetro da função
    columns, # Passando as colunas como parâmetro da função
    hue_column = None, # Passando o hue como parâmetro da função
    num_cols = 3, # Passando o número de colunas como parâmetro da função
    height_figsize = 5, # Passando a altura do figsize como parâmetro da função
):

    num_cols = num_cols # Definindo o número de gráficos por linha, ou seja, as quantidade de colunas
    total_columns = len(columns) # Definindo o total de colunas do dataset
    num_rows = math.ceil(total_columns / num_cols) # Calculando quantas linhas serão necessárias

    fig, axs = plt.subplots( # Criando a figura com os subplots
        nrows=num_rows, # Passando o número de linhas da figura
        ncols=num_cols, # Passando o número de colunas da figura
        figsize=(20, height_figsize*num_rows), # Definindo o tamanho da figura
        tight_layout=True, # Definindo o layout mais justo dos gráficos
    )

    if total_columns == 1: # Se houver apenas um gráfico, axs é um único objeto, então convertemos para uma lista para indexar uniformemente
        axs = [axs]
    elif num_rows == 1: # Se só há uma linha de gráficos, achatamos o array para 1D
        axs = axs.flatten() 

    axs = axs.flatten() if num_rows > 1 else axs # Garantindo que axs seja sempre 1D

    for i, column in enumerate(columns): # Criando a estrutura de repetição para criar os gráficos
        row = i // num_cols # Definindo o índice da linha
        col = i % num_cols # Definindo o índice da coluna

        sns.boxplot( # Criando o boxplot
            data=dataframe, # Passando o dataframe para criar o boxplot
            x=hue_column, # Passando a coluna x que permite criar comparações em relação a alguma variável (geralmente categórica)
            y=column, # Passando a coluna de referência para criar o boxplot
            hue=hue_column, # Passando a hue column
            ax=axs[i], # Passando a posição do gráfico dentro da plotagem do matplotlib
            showmeans=True, # Exibindo a média no boxplot, através de um triângulo verde
        )
        axs[i].set_title(f'Boxplot - {column}') # Adicionando título para cada subplot
        axs[i].set_xlabel('') # Removendo título do eixo x
        axs[i].set_ylabel('') # Removendo título do eixo y


    if total_columns % num_cols != 0: # Removendo subplots vazios (se houver um número ímpar de colunas)
        for subplot in range(total_columns, num_rows * num_cols): # Criando a estrutura de repetição para remover os subplots vazios (em um range do total de colunas até o último subplot previsto)
            fig.delaxes(axs[subplot]) # Removendo o subplot

    plt.show() # Exibindo a figura com os gráficos



def histplots( # Função para criar listas de gráficos histplots
    dataframe, # Passando o dataframe como parâmetro da função
    columns, # Passando as colunas como parâmetro da função
    hue_column = None, # Passando o hue como parâmetro da função
    num_cols = 3, # Passando o número de colunas como parâmetro da função
    height_figsize = 5, # Passando a altura do figsize como parâmetro da função
    alpha = 0.5, # Passando o alpha como parâmetro da função
    kde=False, # Passando o kde como parâmetro da função
):

    num_cols = num_cols # Definindo o número de gráficos por linha, ou seja, as quantidade de colunas
    total_columns = len(columns) # Definindo o total de colunas do dataset
    num_rows = math.ceil(total_columns / num_cols) # Calculando quantas linhas serão necessárias

    fig, axs = plt.subplots( # Criando a figura com os subplots
        nrows=num_rows, # Passando o número de linhas da figura
        ncols=num_cols, # Passando o número de colunas da figura
        figsize=(20, height_figsize*num_rows), # Definindo o tamanho da figura
        tight_layout=True, # Definindo o layout mais justo dos gráficos
    )

    if total_columns == 1: # Se houver apenas um gráfico, axs é um único objeto, então convertemos para uma lista para indexar uniformemente
        axs = [axs]
    elif num_rows == 1: # Se só há uma linha de gráficos, achatamos o array para 1D
        axs = axs.flatten() 

    axs = axs.flatten() if num_rows > 1 else axs # Garantindo que axs seja sempre 1D

    for i, column in enumerate(columns): # Criando a estrutura de repetição para criar os gráficos
        row = i // num_cols # Definindo o índice da linha
        col = i % num_cols # Definindo o índice da coluna

        sns.histplot( # Criando o histograma
            data=dataframe, # Passando o dataframe para criar o gráfico
            x=column, # Passando as colunas para criar o gráfico
            hue=hue_column, # Definindo o parâmetro hue (legenda)
            kde=kde, # Exibindo o KDE
            alpha=alpha, # Definindo a transparência do gráfico
            ax=axs[i] # Posicionando o gráfico em seu devido subplot dentro da figura
        )
        axs[i].set_title(f'Histplot - {column}') # Adicionando título para cada subplot
        axs[i].set_xlabel('') # Removendo título do eixo x
        axs[i].set_ylabel('') # Removendo título do eixo y


    if total_columns % num_cols != 0: # Removendo subplots vazios (se houver um número ímpar de colunas)
        for subplot in range(total_columns, num_rows * num_cols): # Criando a estrutura de repetição para remover os subplots vazios (em um range do total de colunas até o último subplot previsto)
            fig.delaxes(axs[subplot]) # Removendo o subplot

    plt.show() # Exibindo a figura com os gráficos



def elbow_silhouette( # Função para criar os gráficos de Elbow Method e Silhouette Method
    dataframe, # Passando o dataframe como parâmetro da função
    range_k=(2, 11), # Passando o range de intervalos de clusters como parâmetro da função (vai de 2 a 10, pois 11 é exclusive)
):

    fig, axs = plt.subplots( # Criando a figura com os subplots
        nrows=1, # Passando o número de linhas da figura
        ncols=2, # Passando o número de colunas da figura
        figsize=(15, 5), # Definindo o tamanho da figura
        tight_layout=True # Definindo o layout mais justo dos gráficos
    )

    elbow = {} # Criando um dicionário para armazenar os valores de inércia (usados no Método do Cotovelo) para cada valor de K
    silhouette = [] # Criando uma lista para armazenar os valores da pontuação de silhueta para cada valor de K

    k_range = range(*range_k) # Descompactando o range

    for value in k_range: # Criando uma estrutura de repetição para percorrer cada valor de K e criar um modelo K-Means
        kmeans = KMeans( # Criando um modelo K-Means para cada valor de K
            n_clusters=value, # Passando o valor de K
            random_state=consts.RANDOM_STATE, # Definindo o random state
            n_init=10 # Definindo a quantidade de vezes que o algoritmo será executado
        )
        kmeans.fit(dataframe) # Ajustando o modelo aos dados
        elbow[value] = kmeans.inertia_ # Calculando e armazenado a inércia

        labels = kmeans.labels_ # Armazenando os valores de kmeans em uma variável
        silhouette.append(silhouette_score(dataframe, labels)) # Calculando o valor da silhueta

    sns.lineplot( # Criando o gráfico de Elbow Method
        x=list(elbow.keys()), # Passando os valores de X
        y=list(elbow.values()), # Passando os valores de Y
        ax=axs[0] # Passando a posição do gráfico na figura
    )
    axs[0].set_xlabel("Inertia") # Definindo o título do gráfico na posição 0
    axs[0].set_title("Elbow Method") # Definindo o título do eixo X na posição 0

    sns.lineplot( # Criando o gráfico de Silhouette Method
        x=list(k_range), # Passando os valores de X
        y=silhouette, # Passando os valores de Y
        ax=axs[1] # Passando a posição do gráfico na figura
    )
    axs[1].set_xlabel("Silhouette Score") # Definindo o título do eixo X na posição 0
    axs[1].set_title("Silhouette Method") # Definindo o título do gráfico na posição 1

    plt.show() # Exibindo a figura com os gráficos