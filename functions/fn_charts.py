import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



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
        tight_layout=True # Definindo o layout dos gráficos
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