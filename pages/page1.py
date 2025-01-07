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

# Create the download button
with open(temp_file_path, "rb") as file:
    st.download_button(
        label="Download Ledger CSV",
        data=file,
        file_name="ledger.csv",
        mime="text/csv",
    )

# Remove the temporary file after download
os.remove(temp_file_path)
