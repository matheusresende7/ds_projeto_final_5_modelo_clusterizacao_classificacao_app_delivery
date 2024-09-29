import sys
sys.path.append('..')
import pandas as pd
import params.consts as consts
import joblib as jb
import streamlit as st

model_classification = jb.load(consts.MODEL_CLASSIFICATION_JOBLIB)

st.title('Prevendo a resposta da 6ª campanha')

Education = st.selectbox('Escolaridade', ['Graduation', 'PhD', 'Master', 'Basic', '2n Cycle'], index=None, placeholder='Selecione uma opção...',)
Marital_Status = st.selectbox('Estado Civil', ['Single', 'Partner'], index=None, placeholder='Selecione uma opção...',)
Children = st.select_slider('Filhos', options=list(range(0, 6)))
HasChildren = st.number_input('Tem Filhos') #--------------------
Age = st.select_slider('Idade', options=list(range(18, 71)))
AgeGroup = st.text_input('Faixa de Idade') #--------------------
Income = st.number_input('Renda')
Recency = st.number_input('Frequência de Compras')
Complain = st.radio('Já Reclamou?', [0, 1], index=None,)
Days_Since_Enrolled = st.number_input('Dias como Cliente')
Years_Since_Enrolled = st.number_input('Anos como Cliente') #--------------------
NumDealsPurchases = st.number_input('Número de Compras com Desconto')
NumWebVisitsMonth = st.number_input('Número de Visitas ao Site')
NumTotalPurchases = st.number_input('Número de Compras')
MntRegularProds = st.number_input('Gasto com Produtos Regulares')
MntGoldProds = st.number_input('Gasto com Produtos Gold')
MntTotal = st.number_input('Gasto Total') #--------------------
AcceptedCmpTotal = st.select_slider('Quantidade de Campanhas Aceitas', options=list(range(0, 6)))
HasAcceptedCmp = st.radio('Já Aceitou Companhas?', [0, 1], index=None,) #--------------------
Cluster = st.radio('Cluster', [0, 1, 2], index=None,)

button = st.button('PREVER')

if button:
    try:
        
        data = pd.DataFrame({ # Criando um dataset com os dados de entrada
            'Education': [Education], 
            'Marital_Status': [Marital_Status], 
            'Children': [Children], 
            'HasChildren': [HasChildren], 
            'Age': [Age], 
            'AgeGroup': [AgeGroup], 
            'Income': [Income], 
            'Recency': [Recency], 
            'Complain': [Complain], 
            'Days_Since_Enrolled': [Days_Since_Enrolled], 
            'Years_Since_Enrolled': [Years_Since_Enrolled],
            'NumDealsPurchases': [NumDealsPurchases], 
            'NumWebVisitsMonth': [NumWebVisitsMonth], 
            'NumTotalPurchases': [NumTotalPurchases], 
            'MntRegularProds': [MntRegularProds], 
            'MntGoldProds': [MntGoldProds], 
            'MntTotal': [MntTotal], 
            'AcceptedCmpTotal': [AcceptedCmpTotal], 
            'HasAcceptedCmp': [HasAcceptedCmp], 
            'Cluster': [Cluster]
        })

        # Prevendo a resposta
        prediction = model_classification.predict(data)
        if prediction == 1:
            st.success('Esse cliente deve aceitar a 6ª campanha.')
        elif prediction == 0:
            st.success('Esse cliente não deve aceitar a 6ª campanha.')

    except Exception as error:
        st.error(f'Ocorreu o seguinte erro durante a previsão: {error}.')