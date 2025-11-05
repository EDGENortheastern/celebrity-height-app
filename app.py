import pandas as pd # for handling data in DataFrames
import streamlit as st # for building the web app interface
from modules.ui_components import show_header  # to use the header function from modules
from modules.user_input import get_user_height # to use input box from get_user_height
import plotly.express as px  #  for interactive charts and visualisations

show_header() 
height = get_user_height()
st.write(f"Your height: {height} cm")