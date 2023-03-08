# %%
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

data = pd.read_csv('../data/telecom-customer-churn.csv')
to_change = [
        'gender', 'Partner', 'Dependents',
        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
]
enc = OrdinalEncoder()
data[to_change] = enc.fit_transform(data[to_change])
data.to_csv('../data/telecom-customer-churn-encoded.csv')

# %%
