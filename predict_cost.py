import joblib



import pandas as pd

# create a Pandas DataFrame with input data
X = pd.DataFrame({
    'col1': ['area'],
    'col2': ['location'],
    'col3': ['status'],
    'col4': ['bedroom']
})
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
Le= preprocessing.LabelEncoder()
# define the column transformer
ct = ColumnTransformer(transformers=[
    ('cat', Le(), ['col2','col3'])
])
_transformed = ct.fit_transform(X)
def predict(data):
    lr = joblib.load('rentpred.sav')
    return lr.predict(data)
    rt = joblib.load('label_encoder.sav')
    return lr.predict(data)
    t = joblib.load('scaler.sav')
    return lr.predict(data)
