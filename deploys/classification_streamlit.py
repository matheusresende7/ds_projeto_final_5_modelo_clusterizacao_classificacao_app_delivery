import sys
sys.path.append('..')
import pandas as pd
import params.consts as consts
import joblib as jb
import streamlit as st

model_classification = jb.load(consts.MODEL_CLASSIFICATION_JOBLIB) # Carregando o modelo

st.title('Modelo de Previsão') # Definindo o título do site

st.subheader('Prevendo a resposta da 6ª campanha') # Definindo o subtítulo do site

# Obtendo os valores dos campos inseridos pelo usuário
Education = st.selectbox('Escolaridade:', ['Graduation', 'PhD', 'Master', 'Basic', '2 Cycle'], index=None, placeholder='Selecione uma opção...',)
Marital_Status = st.selectbox('Estado civil:', ['Single', 'Partner'], index=None, placeholder='Selecione uma opção...',)
Children = st.select_slider('Filhos:', options=list(range(0, 6)))
Age = st.select_slider('Idade:', options=list(range(18, 71)))
Income = st.number_input('Renda:')
Recency = st.number_input('Frequência de compras:')
Complain = st.radio('Já reclamou?', ['Não', 'Sim'], index=None,)
Days_Since_Enrolled = st.number_input('Dias como cliente:')
NumDealsPurchases = st.number_input('Número de compras com desconto:')
NumWebVisitsMonth = st.number_input('Número de visitas ao site:')
NumTotalPurchases = st.number_input('Número de compras:')
MntRegularProds = st.number_input('Gasto com produtos regulares:')
MntGoldProds = st.number_input('Gasto com produtos gold:')
AcceptedCmpTotal = st.select_slider('Quantidade de campanhas aceitas:', options=list(range(0, 6)))
Cluster = st.radio('Cluster:', [0, 1, 2], index=None,)

# Calculando os demais campos com base nos valores dos campos inseridos pelo usuário
HasChildren = 1 if Children > 0 else 0
AgeGroup = AgeGroup = '18-30' if 18 <= Age <= 30 else '31-45' if 31 <= Age <= 45 else '46-60' if 46 <= Age <= 60 else '61+'
Complain = 1 if Complain == 'Sim' else 0
Years_Since_Enrolled = int(Days_Since_Enrolled // 365)
MntTotal = MntRegularProds + MntGoldProds
HasAcceptedCmp = 1 if AcceptedCmpTotal > 0 else 0

button = st.button('FAZER PREVISÃO', type='primary', use_container_width=True) # Criando o botão para fazer a previsão

if button: # Criando as ações ao apertar o botão

    try: # Tratando erros ao apertar o botão
        
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

        prediction = model_classification.predict(data) # Armazenando a respota do modelo em uma variável
        
        if prediction == 1: # Exibindo uma mensagem de sucesso caso o cliente deva aceitar a campanha
            st.success(f'Esse cliente DEVE aceitar a 6ª campanha.')
        elif prediction == 0: # Exibindo um aviso caso o cliente não deva aceitar a campanha
            st.warning(f'Esse cliente NÃO DEVE aceitar a 6ª campanha.')

    except Exception as error: # Exibindo uma mensagem com o erro que ocorreu
        st.error(f'Ocorreu o seguinte erro durante a previsão: "{error}\n\nEntre em contato com o suporte para obter ajuda.')