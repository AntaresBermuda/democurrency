import streamlit as st

st.title("The ledger")

ledger = pd.read_csv("ledger.csv")

st.dataframe(ledger)
st.write(ledger.shape)
