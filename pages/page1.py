import streamlit as st
import pandas as pd
import base64
import os

st.title("The ledger")

ledger = pd.read_csv("ledger.csv")

st.dataframe(ledger.style.set_properties(**{'max-width': '2px'}))

csv = ledger.to_csv(index=False)


st.title("CSV Data API")
st.markdown("### Access CSV Data Programmatically")
st.code("import requests\nresponse = requests.get('http://democurrency.streamlit.app/data.csv')\ndata = response.text", language="python")

# Serve the CSV content
st.markdown("#### CSV Content (Raw)")
st.text(csv)

# Optionally save it as a downloadable link
st.markdown("#### [Download CSV File](data:text/csv;base64,{})".format(csv.encode("utf-8").decode("latin-1")), unsafe_allow_html=True)


# Ensure the file is saved locally
os.makedirs("static", exist_ok=True)
ledger.to_csv("static/shared_data.csv", index=False)

# Generate the file link
st.title("Shared CSV Data")
file_link = "http://your-app-url/static/shared_data.csv"
st.markdown(f"### Download Link: [Shared Data CSV]({file_link})")
