import streamlit as st
import pandas as pd
import base64
import os

st.title("The ledger")

df = pd.read_csv("ledger.csv")

# Check for query parameters
query_params = st.experimental_get_query_params()
download_requested = query_params.get("download", ["false"])[0].lower() == "true"

if download_requested:
    # Convert DataFrame to CSV
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    # Set response as raw CSV
    st.write(csv_buffer.getvalue())
else:
    # Normal app functionality
    st.title("DataFrame Sharing Example")
    st.write("To request the DataFrame, add `?download=true` to the URL.")
    st.write("Here is the DataFrame preview:")
    st.dataframe(df)
