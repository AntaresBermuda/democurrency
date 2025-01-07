import streamlit as st
import pandas as pd
import base64
import os

st.title("The ledger")

ledger = pd.read_csv("ledger.csv")

st.dataframe(ledger.style.set_properties(**{'max-width': '2px'}))

csv = ledger.to_csv(index=False)

# Encode the CSV string as base64
b64 = base64.b64encode(csv.encode()).decode()

# Create a downloadable link for the CSV
file_name = "data.csv"
href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">Download CSV File</a>'
st.markdown(href, unsafe_allow_html=True)


# Save the CSV to a temporary file
temp_file_path = 'temp_ledger.csv'
with open(temp_file_path, 'w') as f:
    f.write(csv)

# Provide the download link
href = f'<a href="files/{temp_file_path}" download>Click here to download the ledger</a>'
st.markdown(href, unsafe_allow_html=True)

# Optionally, clean up the temporary file after a while (if needed)
os.remove(temp_file_path)
