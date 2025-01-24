import streamlit as st
import pandas as pd
import base64
import os
import io

st.title("The ledger")

df = pd.read_csv("ledger.csv")

# Helper function to create a downloadable link
def get_download_link(dataframe):
    csv_buffer = io.StringIO()
    dataframe.to_csv(csv_buffer, index=False)
    b64 = base64.b64encode(csv_buffer.getvalue().encode()).decode()
    return f"data:text/csv;base64,{b64}"

# Provide the download link
st.write("To download the DataFrame programmatically, use the code below:")
download_url = get_download_link(df)
st.code(f"""
import pandas as pd
import requests

url = "{download_url}"
content = requests.get(url).content
df = pd.read_csv(io.StringIO(content.decode("utf-8")))
print(df)
""", language="python")
