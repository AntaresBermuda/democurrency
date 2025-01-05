import streamlit as st
import pickle

st.title("The ledger")

with open("ledger.pkl", "rb") as f:
    ledger = pickle.load(f)

st.dataframe(ledger)
st.write(ledger.shape)
