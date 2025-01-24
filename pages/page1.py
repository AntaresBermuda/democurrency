import streamlit as st
import pandas as pd
import base64
import os

st.title("The ledger")

df = pd.read_csv("ledger.csv")

df
