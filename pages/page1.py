import streamlit as st
import pandas as pd

st.title("The ledger")

ledger = pd.read_csv("ledger.csv")

st.dataframe(ledger)
st.write(ledger.shape)
