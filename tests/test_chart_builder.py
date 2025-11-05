import pandas as pd # data analysis
from modules.chart_builder import build_chart # chart builder
import plotly.graph_objects as go # to get chat type

def test_build_chart_returns_figure():
    """Ensure build_chart returns a Plotly Figure with correct data."""
    df = pd.DataFrame({
        "Name": ["Tom Cruise", "Zendaya", "You"],
        "Height_cm": [172, 178, 165]
    })
    
    fig = build_chart(df)
    assert isinstance(fig, go.Figure)


    x_values = [x for trace in fig.data for x in trace.x]
    y_values = [y for trace in fig.data for y in trace.y]

    assert x_values == df["Name"].tolist(), "X-axis names should match input data"
    assert y_values == df["Height_cm"].tolist(), "Y-axis values should match input data"
