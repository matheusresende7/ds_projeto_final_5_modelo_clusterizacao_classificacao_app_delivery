import pandas as pd

def describe(df): # Função para otimizar a exibição dos dados no describe
    with pd.option_context(
        'display.float_format', '{:.2f}'.format, # Formatando os dados com 2 casas decimais
        'display.max_columns', None # Removendo a limitação de visualização de apenas 20 colunas
    ):
        display(df.describe()) # Exibindo o describe dos dados