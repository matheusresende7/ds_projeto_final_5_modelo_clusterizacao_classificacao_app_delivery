# Ciência de Dados - Projeto Final 5

![Wallpaper](images/illustrations/wallpaper.png)

## Projeto
**Modelos de clusterização e classificação** para segmentação de clientes em campanhas de marketing em uma plataforma de delivery.


## Objetivo
O objetivo do projeto é, a partir dos dados de uma campanha piloto, construir um **modelo de clusterização** para segmentação de clientes em campanhas de marketing em uma plataforma de delivery. <br>

A intenção é que o modelo preveja o comportamento dos consumidores e torne possível aplicá-lo a toda a base de clientes, permitindo que a empresa selecione os clientes que têm maior probabilidade de adquirir a oferta, otimizando assim os resultados das campanhas e tornando-as altamente lucrativas. <br>

E em seguida, construir um **modelo de classificação** de acordo com os resultados obtidos no modelo inicial para fazer a segmentação dos futuros clientes da empresa.


## Descrição
............................


## Metodologia 5W2H
|**Questionamento**       |**Descrição**|
|-------------------------|-------------|
|**What?**<br>O que?      | A partir dos dados de uma campanha piloto, **construir um modelo para segmentação de clientes em campanhas de marketing** |
|**Why?**<br>Por quê?     | O objetivo é que o modelo preveja o comportamento dos consumidores e torne possível aplicá-lo a toda a base de clientes, permitindo que a empresa selecione os clientes que têm maior probabilidade de adquirir a oferta, **otimizando assim os resultados das campanhas e tornando-as altamente lucrativas** |
|**How?**<br>Como?        | O projeto será realizado através da **criação de modelos de clusterização e classificação para a segmentação de clientes** |
|**Where?**<br>Onde?      | Em uma **empresa de delivery** |
|**When?**<br>Quando?     | A data de início do projeto é **01/09/2024**, com um prazo estipulado para conclusão de **30 dias**. Dessa forma, a data prevista para conclusão do projeto é **30/09/2024** |
|**Who?**<br>Quem?        | **Matheus Resende** - Cientista de Dados |
|**How Much?**<br>Quanto? | O investimento estimado para o projeto é de **6.720MU** |


## Referências
- **Repositório do desafio:** https://github.com/ifood/ifood-data-business-analyst-test


## Bibliotecas
- **Matplotlib:** https://matplotlib.org/
- **NumPy:** https://pandas.pydata.org/docs/index.html
- **Pandas:** https://pandas.pydata.org/docs/index.html
- **Scikit-Learn:** https://seaborn.pydata.org/
- **Seaborn:** https://seaborn.pydata.org/


## Estrutura do Projeto
- **.venv/:** Pasta destinada a armazenar o ambiente virtual do projeto se necessário
- **data/:** Pasta destinada a armazenar as versões dos datasets: raw, processed, lean, transformed, entre outros
- **deploys/:** Pasta destinada a armazenar os deploys do projeto, em formatos jupyter notebook, python, executável e streamlit
- **dictionaries/:** Pasta destinada a armazenar os dicionários do projeto: charts, data, datasets, evaluation metrics, feature engineering, models, pipeline e stats
- **docs/:** Pasta destinada a armazenar os arquivos e documentos referentes ao projeto
- **functions/:** Pasta destinada a armazenar arquivos com as funções do projeto: charts, libraries e stats
- **images/:** Pasta destinada a armazenar imagens do projeto: illustrations e outputs
- **models/:** Pasta destinada a armazenar os modelos criados durante o projeto
- **notebooks/:** Pasta destinada a armazenar os notebooks de cada etapa do projeto de ciência de dados
- **params/:** Pasta destinada a armazenar as constantes e variáveis globais do projeto
- **presentations/:** Pasta destinada a armazenar as apresentações do projeto, em PowerPoint e PDF
- **references/:** Pasta destinada a armazenar arquivos com informações do projeto, como markdown tables e cronograma
- **reports/:** Pasta destinada a armazenar relatórios criados durante o projeto
- `.env`: Arquivo para armazenar as variáveis de ambiente sensíveis do projeto, como usuários, senhas, tokens e chaves de API
- `.gitattributes`: Arquivo para configurar o repositório e omitir arquivos sem utilidades da versão final do projeto
- `.gitignore`: Arquivo para ignorar determinados arquivos ao subir o projeto para o Github
- `LICENSE`: Arquivo com a licença do projeto
- `README.md`: Arquivo para resumir e apresentar o projeto
- `requirements.txt`: Arquivo para listar as dependências/bibliotecas necessárias no projeto
- `to_do.txt`: Arquivo para anotar as tarefas pendentes do projeto


## Etapas do Projeto
- **01. Definição do desafio – Challenge:** Essa etapa tem o objetivo de explicar o desafio que será resolvido no projeto. Dentre as etapas estão: objetivo do projeto, descrição do projeto, metodologia 5W2H, referências, bibliotecas, estrutura do projeto, etapas do projeto, dicionários do projeto e cronograma do projeto
- **02. Obtenção dos Dados – Data Sourcing:** Essa etapa tem o objetivo de obter todos os dados que serão utilizados no projeto. Dentre as etapas estão: a obtenção de dados de banco de dados, APIs, web scraping e outras fontes de dados como em formato .csv
- **03. Detalhamento do Projeto – Project Details:** Essa etapa tem o objetivo de visualizar e entender os dados iniciais do projeto. Dentre as etapas estão: geração de relatórios usando o Profile Report e a listagem das ações para tratar os dados
- **04. Tratamento dos Dados – Data Processing:** Essa etapa tem o objetivo de tratar e modelar os dados para as próximas etapas do projeto. Dentre as etapas estão: corrigir o tipo de dados das colunas, tratar colunas com valores vazios, modelar colunas de tempo e idade, mesclar colunas com muitas categorias, unificar colunas semelhantes, criar colunas derivadas de outras, tratar colunas com outliers, tratar colunas com valores únicos, tratar colunas com valores constantes, excluir colunas auxiliares, e por fim gerar um novo relatório usando o Profile Report
- **05. Análise Exploratória – Exploratory Data Analysis (EDA):** Essa etapa tem o objetivo de fazer uma análise geral dos dados para se obter os principais insights do projeto. Dentre as etapas estão: definir as hue columns, gerar uma lista de histogramas e boxplots com base nas hue columns, gerar um mapa de calor com as correlações entre as variáveis, gerar gráficos de barra com as maiores correlações positivas e negativas entre as principais colunas, identificar qualitativamente e quantitativamente os grupos com base nas análises realizadas, e por fim propor sugestões de melhorias e estimar o impacto da aplicação dessas sugestões
- **06. Seleção do Modelo – Model Selection:** Essa etapa tem o objetivo de avaliar entre vários modelos, qual é o modelo tem a melhor performance e que será treinado na próxima etapa. Dentre as etapas estão: a aplicação de etapas do pipeline: pre processing, feature selection, dimensionality reduction, resampling, models e cross validation, e por fim a avaliação das métricas de avaliação dos modelos e a seleção de qual modelo será utilizado no projeto 
- **07. Treinamento do Modelo – Model Training:** Essa etapa tem o objetivo de otimizar os hiperparâmetros no treinamento do modelo definido na etapa anterior. Dentre as etapas estão: a aplicação de etapas do pipeline: pre processing, feature selection, dimensionality reduction, resampling, models, cross validation e hyperparameter tuning, e por fim a comparação das métricas de avaliação do modelo entre como estava antes da otimização de hiperparâmetros e após a otimização
- **08. Deploy em Produção – Deployment:** Essa etapa tem o objetivo de disponibilizar o modelo para uso. Dentre as etapas estão: disponibilização através de um arquivo jupyter notebook, python, arquivo executável e streamlit


### Cronograma do Projeto - Gráfico de Gantt

![Schedule](images/outputs/schedule.png)


## Resultados
...........................