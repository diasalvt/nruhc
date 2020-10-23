import pandas as pd

def get_churn_data(url = 'https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv', flag=False):
    if flag:
        return (url[12] + url[23] + url[14] + url[13] + url[14]).upper()

    return pd.read_csv(url)
