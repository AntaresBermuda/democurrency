import streamlit as st
import pandas as pd
import os

st.title("The ledger")

# Read the ledger CSV
df = pd.read_csv("ledger.csv")

# Save the CSV to a static file in a predefined location
static_file_path = "static_ledger.csv"
df.to_csv(static_file_path, index=False)

# Create a static download link
static_download_link = f'<a href="{static_file_path}" download>Download ledger</a>'

# Render the static download link
st.markdown(static_download_link, unsafe_allow_html=True)

st.markdown("### View ledger")
st.dataframe(df)
