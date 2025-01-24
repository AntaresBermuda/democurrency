import streamlit as st
import pandas as pd
import base64  # Import base64 for encoding the file data
import os

st.title("The ledger")

# Read the ledger CSV
df = pd.read_csv("ledger.csv")

# Save the CSV to a static file
static_file_path = "static_ledger.csv"
df.to_csv(static_file_path, index=False)

# Serve the file with a proper MIME type
with open(static_file_path, "rb") as file:
    file_data = file.read()

# Create a downloadable link with a MIME type for CSV
download_link = f'<a href="data:file/csv;base64,{base64.b64encode(file_data).decode()}" download="ledger.csv">Download ledger</a>'

# Render the download link
st.markdown(download_link, unsafe_allow_html=True)
st.write(download_link)

st.markdown("### View ledger")
st.dataframe(df)
