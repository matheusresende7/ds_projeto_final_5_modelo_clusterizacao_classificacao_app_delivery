import sys

import joblib as jb
import pandas as pd
import streamlit as st

sys.path.append('..')
import params.consts as consts



model_classification = jb.load(consts.MODEL_CLASSIFICATION_JOBLIB) 

st.title('Modelo de Previsão') 

st.subheader('Prevendo a resposta da 6ª campanha') 

Education = st.selectbox('Escolaridade:', ['Graduation', 'PhD', 'Master', 'Basic', '2 Cycle'], index = None, placeholder = 'Selecione uma opção...')
Marital_Status = st.selectbox('Estado civil:', ['Single', 'Partner'], index = None, placeholder = 'Selecione uma opção...')
Children = st.select_slider('Filhos:', options = list(range(0, 6)))
Age = st.select_slider('Idade:', options = list(range(18, 71)))
Income = st.number_input('Renda:')
Recency = st.number_input('Frequência de compras:')
Complain = st.radio('Já reclamou?', ['Não', 'Sim'], index = None,)
Days_Since_Enrolled = st.number_input('Dias como cliente:')
NumDealsPurchases = st.number_input('Número de compras com desconto:')
NumWebVisitsMonth = st.number_input('Número de visitas ao site:')
NumTotalPurchases = st.number_input('Número de compras:')
MntRegularProds = st.number_input('Gasto com produtos regulares:')
MntGoldProds = st.number_input('Gasto com produtos gold:')
AcceptedCmpTotal = st.select_slider('Quantidade de campanhas aceitas:', options = list(range(0, 6)))
Cluster = st.radio('Cluster:', [0, 1, 2], index = None)

HasChildren = 1 if Children > 0 else 0
AgeGroup = AgeGroup = '18-30' if 18 <= Age <= 30 else '31-45' if 31 <= Age <= 45 else '46-60' if 46 <= Age <= 60 else '61+'
Complain = 1 if Complain == 'Sim' else 0
Years_Since_Enrolled = int(Days_Since_Enrolled // 365)
MntTotal = MntRegularProds + MntGoldProds
HasAcceptedCmp = 1 if AcceptedCmpTotal > 0 else 0

button = st.button('FAZER PREVISÃO', type = 'primary', use_container_width = True) 

if button: 

    try: 
        
        data = pd.DataFrame({ 
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

        prediction = model_classification.predict(data) 
        
        if prediction == 1: 

            st.success(f'Esse cliente DEVE aceitar a 6ª campanha.')

        elif prediction == 0: 

            st.warning(f'Esse cliente NÃO DEVE aceitar a 6ª campanha.')

    except Exception as error: 
        
        st.error(f'Ocorreu o seguinte erro durante a previsão: "{error}\n\nEntre em contato com o suporte para obter ajuda.')