from src import load_data
from src import zones
import plotly.graph_objects as go




def main():
    
    df = load_data.load_activity("data/activity.csv")
    #print(df)
    mittelwert, maximum = load_data.get_stats(df)
    
    print(f"Mittelwert: {mittelwert}, Maximum: {maximum}")

    #zones.plot_zones(data)
    # x=[1, 2, 3, 4]
    # y=[10, 15, 8, 20]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x = df["Time"],
            y = df["HeartRate"],
            mode="lines"
            )
        )  
    fig.show()


if __name__ == "__main__":
    main() 