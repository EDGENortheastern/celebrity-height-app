import streamlit as st  # to create the input box

def get_user_height() -> int:
    """Displays an input box and returns the user's height in cm."""
    user_height = st.number_input(
        label="Enter your height (cm):",
        min_value=100,
        max_value=220,
        step=1,
        value=170
    )
    return user_height
