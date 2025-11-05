# import streamlit as st  # 🌐 Used to build web apps with Python
import plotly.express as px  # 📊 For creating interactive charts and visualisations
import pandas as pd  # 🧮 For data analysis and manipulation

def build_chart(df: pd.DataFrame):
    """Creates and returns a Plotly bar chart figure with a highlighted 'You' bar."""
    # Colour bars — red for "You", blue for others
    df["Colour"] = ["red" if name == "You" else "lightblue" for name in df["Name"]]

    fig = px.bar(
        df,
        x="Name",
        y="Height_cm",
        color="Colour",
        text="Height_cm",
        title="📏 Celebrity Height Comparison Chart",
        hover_data={"Name": True, "Height_cm": False},
        color_discrete_map="identity",  # use the exact colours in 'Colour'
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Height: %{y} cm<extra></extra>",
        textposition="outside",
        cliponaxis=False,
    )

    # Add annotation under "You"
    fig.add_annotation(
        x="You",
        y=0,
        text="<b style='color:red;'>You</b>",
        showarrow=False,
        yshift=-30,
        font=dict(color="red", size=14),
    )

    fig.update_layout(
        title=dict(text="📏 Celebrity Height Comparison", x=0.5),
        xaxis_title="Name",
        yaxis_title="Height (cm)",
        showlegend=False,
        margin=dict(l=40, r=40, t=80, b=120),
    )

    return fig