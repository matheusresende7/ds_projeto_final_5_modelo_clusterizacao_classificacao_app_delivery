import sys

import joblib as jb
import pandas as pd

sys.path.append('..')
import params.consts as consts



model_classification = jb.load(consts.MODEL_CLASSIFICATION_JOBLIB) 

df = pd.read_csv(consts.DATASET_DEPLOY_CLASSIFICATION, sep = ';') 

predictions = model_classification.predict(df) 

df['Response'] = predictions 

df.to_csv(consts.DATASET_DEPLOYED_CLASSIFICATION, index = False) 