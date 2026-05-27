import pandas as pd

def load_activity(data):
    df = pd.read_csv(data)
    df["Time"] = range(len(df))
    return df

def get_stats(df):

    mittelwert = df["PowerOriginal"].mean()
    maximum = df["PowerOriginal"].max()

    return mittelwert,maximum


    

   
