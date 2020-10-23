import pandas as pd

def get_churn_data(url = 'https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv'):

    return pd.read_csv(url)
