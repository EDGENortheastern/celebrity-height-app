import pandas as pd # for handling data in DataFrames
import streamlit as st # for building the web app interface
from modules.ui_components import show_header  # to use the header function from modules
from modules.user_input import get_user_height # to use input box from get_user_height
from modules.chart_builder import build_chart  # 📊 the chart-building function from the module

show_header() 
height = get_user_height()
st.write(f"Your height: {height} cm")

celebs_df = pd.read_csv("celebs_height.csv")
user_row = pd.DataFrame({"Name": ["You"], "Height_cm": [height]})
celebs_df = pd.concat([celebs_df, user_row], ignore_index=True)
celebs_df = celebs_df.sort_values(by="Height_cm", ascending=False).reset_index(drop=True)

fig = build_chart(celebs_df)
st.plotly_chart(fig, use_container_width=True)

st.success("✅ Chart loaded")