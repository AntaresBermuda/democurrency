import streamlit as st
import pandas as pd

st.title("The ledger")

ledger = pd.read_csv("ledger.csv")

st.dataframe(ledger.style.set_properties(**{'max-width': '200px'}))
st.dataframe(ledger.style.set_properties(**{'min-width': '200px'}))

st.dataframe(ledger)
