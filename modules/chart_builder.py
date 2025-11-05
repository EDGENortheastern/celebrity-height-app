import streamlit as st  # 🌐 Used to build web apps with Python
import plotly.express as px  # 📊 For creating interactive charts and visualisations
import pandas as pd  # 🧮 For data analysis and manipulation

def build_chart(df: pd.DataFrame):
    """Creates and returns a Plotly bar chart figure with custom hover labels."""
    fig = px.bar(
        df,
        x="Name",
        y="Height_cm",
        color="Name",
        text="Height_cm",
        title="📏 Celebrity Height Comparison Chart",
        hover_data={"Name": True, "Height_cm": False},  
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Height: %{y} cm<extra></extra>",  
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        title={
            'text': "📏 Celebrity Height Comparison",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Name",
        yaxis_title="Height (cm)",
        showlegend=False,
        margin=dict(l=40, r=40, t=80, b=120)
    )
    tickvals = df["Name"].tolist()
    ticktext = [f"<span style='color:red; font-weight:bold'>{n}</span>" if n == "You" else n for n in df["Name"]]
    fig.update_xaxes(tickvals=tickvals, ticktext=ticktext)
    return fig
