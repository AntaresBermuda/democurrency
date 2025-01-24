import streamlit as st
import pandas as pd
import base64
import os
import io

st.title("The ledger")

df = pd.read_csv("ledger.csv")

# Helper function to create a downloadable link
def get_clickable_download_link(dataframe, filename="data.csv"):
    csv_buffer = io.StringIO()
    dataframe.to_csv(csv_buffer, index=False)
    b64 = base64.b64encode(csv_buffer.getvalue().encode()).decode()  # Encode as base64
    href = f'<a href="data:text/csv;base64,{b64}" download="{filename}">Click here to download the DataFrame</a>'
    return href

st.markdown("## Download the DataFrame")
st.markdown(get_clickable_download_link(df), unsafe_allow_html=True)

st.write({download_url})

# Provide the Python code for programmatic download
download_url = get_clickable_download_link(df).split('"')[1]  # Extract the `href` value
st.code(f"""
url = "{download_url}"
""", language="python")

df
