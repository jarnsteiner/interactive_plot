import pandas as pd

def zones_rect(max_hr):

    zone = [
    (0.5 * max_hr, 0.6 * max_hr, "lightgreen"),
    (0.6 * max_hr, 0.7 * max_hr, "green"),
    (0.7 * max_hr, 0.8 * max_hr, "yellow"),
    (0.8 * max_hr, 0.9 * max_hr, "orange"),
    (0.9 * max_hr, 1.0 * max_hr, "red")
    ]

    return zone 

def zone_summary(df, max_hr):
    grenzen = [0, 0.60, 0.70, 0.80, 0.90, 1.01]

    data = df.copy()

    data["zone"] = pd.cut(
        data["HeartRate"],
        bins = [i * max_hr for i in grenzen],
        labels = [1, 2, 3, 4, 5]

    ).astype("Int64")

    summary = data.groupby("zone").agg({
        "PowerOriginal": "mean",
        "zone": "count"
    })

    summary.columns = ["Power", "Zeit"]

    return summary

# test_data = pd.DataFrame({
#     "heart_rate": [100, 120, 140, 160, 180, 190],
#     "power": [90, 110, 150, 200, 220, 250]
# })

# data = zones(test_data, 190)

# print(data)