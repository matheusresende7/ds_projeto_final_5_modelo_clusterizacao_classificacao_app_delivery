import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



def boxplots( # Função para criar gráficos boxplot
    df, # Passando o df como parâmetro da função
    columns, # Passando as colunas como parâmetro da função
): 
    columns = columns # Passando as colunas que vão ser usadas para criar os boxplots

    fig, axs = plt.subplots( # Criando a figura para colocar os gráficos de boxplots
        nrows=1, # Definindo o número de linhas
        ncols=3, # Definindo o número de colunas
        figsize=(12,4), # Definindo o tamanho da figura
        tight_layout=True # Definindo o layout dos gráficos
    )

    for i, column in enumerate(columns): # Criando uma estrutura de repetição para criar cada um dos boxplots
        sns.boxplot( # Criando o boxplot
            y=column, # Passando a coluna de referência para criar o boxplot
            data=df, # Passando o dataframe para criar o boxplot
            ax=axs[i], # Passando a posição do gráfico dentro da plotagem do matplotlib
        )
        axs[i].set_title(f'Boxplot - {column}', fontsize=12)  # Adiciona um título para cada boxplot
        axs[i].set_ylabel('') # Removendo o título do eixo Y

    plt.show() # Exibindo os boxplots



    