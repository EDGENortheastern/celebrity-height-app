import pandas as pd # for handling data in DataFrames
import streamlit as st # for building the web app interface
from modules.ui_components import show_header  # to use the header function from modules
from modules.user_input import get_user_height # to use input box from get_user_height
from modules.chart_builder import build_chart  # 📊 the chart-building function from the module

show_header() 
height = get_user_height()
st.write(f"Your height: {height} cm")

celebs_df = pd.read_csv("celebs_height.csv")

fig = build_chart(celebs_df)
st.plotly_chart(fig, use_container_width=True)

st.success("✅ Chart generated successfully")