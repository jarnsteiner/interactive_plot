from src import load_data
from src import zones_data
import plotly.graph_objects as go
import streamlit as st



def main():
    
    df = load_data.load_activity("data/activity.csv")
    #print(df)
    W_mid, W_max = load_data.get_stats(df)

    st.title("Herzfrequenz")

    max_hr = user_input()
    #print(max_hr)
    #print(f"Mittelwert: {W_mid}, Maximum: {W_max}")

    
    #zones.plot_zones(data)
    # x=[1, 2, 3, 4]
    # y=[10, 15, 8, 20]
    
    fig = go.Figure()
    fig2 = go.Figure()
    fig.add_trace(
        go.Scatter(
            x = df["Time"],
            y = df["HeartRate"],
            mode="lines",
            line=dict(smoothing = 1.3, color="red"),
            line_shape="spline",
            name= "Heartrate"
            )
        )
    
    fig2.add_trace(
        go.Scatter(
            x = df["Time"],
            y = df["PowerOriginal"],
            mode="lines",
            line=dict(smoothing = 1.3, color="blue"),
            line_shape="spline",
            name= "PowerOrigin"
            )
        ) 
    fig.update_layout(
        width=800,
        height=500,
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white")
    )
    fig2.update_layout(
        width=800,
        height=500,
        plot_bgcolor="black",
        paper_bgcolor="black",
        font=dict(color="white")
    )
    zones =zones_data.zones_rect(max_hr)

    for lower, upper, color in zones:
        fig.add_hrect(
            y0=lower,
            y1=upper,
            fillcolor=color,
            opacity=0.25,
            line_width=0
            )


    st.plotly_chart(fig)
    st.title("Power")
    st.text("Maxpower = "+str(W_max)+ " Midpower = "+ str(W_mid))
    st.plotly_chart(fig2)
    st.title("Zeiten in den Zonen")
    st.table(zones_data.zone_summary(df, max_hr))

def user_input():

    max_hr = st.number_input(
        "Bitte geben sie Ihre Maximale Herzfrequenz ein:",
        min_value=120,
        max_value=270,
        value=200
    )

    return max_hr


if __name__ == "__main__":
    main() 