# Data
DIM_CUSTOMERS_RAW = '../data/01_resource/dim_customers_raw.csv'
DIM_CALENDER_RAW = '../data/01_resource/dim_calender_raw.csv'

DATASET_RAW_PANDAS = '../data/01_resource/dataset_raw_pandas.csv'
DATASET_RAW_PYSPARK = '../data/01_resource/dataset_raw_pyspark'

DATASET_RAW_COMPRESSED_PANDAS = '../data/02_bronze/dataset_raw_compressed_pandas.csv.gz'
DATASET_RAW_COMPRESSED_PYSPARK = '../data/02_bronze/dataset_raw_compressed_pyspark'

DATASET_CLEAN_PANDAS = '../data/03_silver/dataset_clean_pandas.parquet'
DATASET_CLEAN_PYSPARK = '../data/03_silver/dataset_clean_pyspark'

DATASET_CLUSTERED_PANDAS = '../data/03_silver/dataset_clustered_pandas.parquet'
DATASET_CLUSTERED_PYSPARK = '../data/03_silver/dataset_clustered_pyspark'

DATASET_MODELS_METRICS_PANDAS = '../data/04_gold/dataset_models_metrics_pandas.csv'
DATASET_MODELS_METRICS_PYSPARK = '../data/04_gold/dataset_models_metrics_pyspark'

DATASET_MODEL_GROWTH_PANDAS = '../data/04_gold/dataset_model_growth_pandas.csv'
DATASET_MODEL_GROWTH_PYSPARK = '../data/04_gold/dataset_model_growth_pyspark'

DATASET_COMPARING_METRICS_PANDAS = '../data/04_gold/dataset_comparing_metrics_pandas.csv'
DATASET_COMPARING_METRICS_PYSPARK = '../data/04_gold/dataset_comparing_metrics_pyspark'

# Models
GRID_SEARCH_CLASSIFICATION_PANDAS_JOBLIB = '../models/grid_search_classification_pandas.joblib'
GRID_SEARCH_CLASSIFICATION_PYSPARK_JOBLIB = '../models/grid_search_classification_pyspark.joblib'

MODEL_CLASSIFICATION_PANDAS_JOBLIB = '../models/model_classification_pandas.joblib'
MODEL_CLASSIFICATION_PYSPARK_JOBLIB = '../models/model_classification_pyspark.joblib'

MODEL_CLASSIFICATION_PANDAS_PKL = '../models/model_classification_pandas.pkl'
MODEL_CLASSIFICATION_PYSPARK_PKL = '../models/model_classification_pyspark.pkl'

# Deploy
DATASET_DEPLOY_CLASSIFICATION = '../deploys/dataset_deploy_classification.csv'
DATASET_DEPLOYED_CLASSIFICATION = '../deploys/dataset_deployed_classification.csv'

# Reports
EDA_0 = '../reports/eda_0.html'
EDA_1 = '../reports/eda_1.html'

# Values
RANDOM_STATE = 42