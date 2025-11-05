import streamlit as st  # 🌐 Used to build web apps with Python
import plotly.express as px  # 📊 For creating interactive charts and visualisations
import pandas as pd  # 🧮 For data analysis and manipulation

def build_chart(df: pd.DataFrame):
    """Creates and returns a Plotly bar chart figure."""
    fig = px.bar(
        df,
        x="Name",
        y="Height_cm",
        color="Name",
        title="Height Comparison",
        text="Height_cm"
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(showlegend=False)
    return fig