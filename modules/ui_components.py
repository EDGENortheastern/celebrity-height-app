import streamlit as st  # to create UI elements

def show_header():
    """Displays the main app title and caption.

    This function does not return anything.
    It directly writes UI elements to the Streamlit page.
    """
    st.set_page_config(page_title="Celebrity Height Comparison", page_icon="📏")
    st.title("📏 Celebrity Height Comparison")
    st.caption("Compare your height with famous celebrities — just for fun!")
