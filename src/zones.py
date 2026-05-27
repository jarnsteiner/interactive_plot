import pandas as pd

def zones(df,max_hr):

    grenzen = [0, 0.60, 0.70, 0.80, 0.90, 1.01]

    data = df.copy()

    data["zone"] = pd.cut(
        data["heart_rate"],
        bins = [i * max_hr for i in grenzen],
        labels = [1, 2, 3, 4, 5]

    ).astype("Int64")

    return data 

def zone_summary(data):
    summary = data.groupby("zone").agg({
        "power": "mean",
        "zone": "count"
    })

    summary.columns = ["avg_power", "seconds"]

    return summary


