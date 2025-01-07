import streamlit as st
import pandas as pd

st.title("The ledger")

ledger = pd.read_csv("ledger.csv")

st.dataframe(ledger.style.set_properties(**{'max-width': '2px'}))

import streamlit as st
import base64

# Generate or load your file content
file_content = "Hello, this is the content of your file!"
file_name = "example.txt"

# Encode the file content as base64
b64 = base64.b64encode(file_content.encode()).decode()

# Create a link that downloads the file
href = f'<a href="data:file/txt;base64,{b64}" download="{file_name}">Click here to download the file</a>'
st.markdown(href, unsafe_allow_html=True)
