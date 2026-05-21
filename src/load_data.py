import pandas as pd

def load_activity(data):

    return pd.read_csv(data)

def get_stats(df):

    mittelwert = df["PowerOriginal"].mean()
    maximum = df["PowerOriginal"].max()

    return mittelwert,maximum



   
