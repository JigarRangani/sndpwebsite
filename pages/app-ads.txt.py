import streamlit as st

st.set_page_config(
    page_title="app-ads.txt", page_icon=":page_facing_up:"
)  # Set page title and icon

st.title("app-ads.txt")

with open("app-ads.txt", "r") as f:
    file_content = f.read()
st.code(file_content, language="txt") 