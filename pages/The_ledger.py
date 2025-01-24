import streamlit as st
import pandas as pd
import base64

st.title("The ledger")

# Load the CSV file
df = pd.read_csv("ledger.csv")

# Create a download button using Streamlit's built-in functionality
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(df)
st.download_button(
    label="Download ledger as CSV",
    data=csv,
    file_name='ledger.csv',
    mime='text/csv',
)

# Display the data
st.markdown("### View ledger")
st.dataframe(df)
