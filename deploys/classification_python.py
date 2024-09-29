# Importando as bibliotecas
import sys
sys.path.append('..')
import pandas as pd
import params.consts as consts
import joblib as jb

model_classification = jb.load(consts.MODEL_CLASSIFICATION_JOBLIB) # Carregando o modelo 

df = pd.read_csv(consts.DATASET_DEPLOY_CLASSIFICATION, sep=';') # Lendo o dataset a ser previsto

predictions = model_classification.predict(df) # Fazendo as previsões com o modelo

df['Response'] = predictions # Criando uma coluna para armazenar as previsões

df.to_csv(consts.DATASET_DEPLOYED_CLASSIFICATION, index=False) # Salvando o dataset com as previsões