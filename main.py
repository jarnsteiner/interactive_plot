from src import load_data
from src import zones
import plotly.graph_objects as go




def main():
    
    data = load_data.load_activity("data/activity.csv")

    mittelwert, maximum = load_data.get_stats(data)
    
    print(f"Mittelwert: {mittelwert}, Maximum: {maximum}")

    #zones.plot_zones(data)
    x=[1, 2, 3, 4]
    y=[10, 15, 8, 20]
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x = x,
            y = y,
            mode="lines"
            )
        )  
    fig.show()










     







if __name__ == "__main__":
    main() 