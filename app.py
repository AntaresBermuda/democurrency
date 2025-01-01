import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import calendar as cal
import seaborn as sns
from dateutil.relativedelta import relativedelta
import time

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🏠",
    layout="wide",
)

st.title("Welcome to the Home Page")
st.write("This is the main page of the app. Use the sidebar to navigate.")


from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat, PrivateFormat, NoEncryption

# Generate RSA keys
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Create a transaction
def create_transaction(sender, recipient, amount, private_key):
    transaction_data = f"{sender} -> {recipient}: {amount}"
    transaction_bytes = transaction_data.encode('utf-8')
    
    # Sign the transaction
    signature = private_key.sign(
        transaction_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH,
        ),
        hashes.SHA256(),
    )
    return transaction_data, signature

# Verify a transaction
def verify_transaction(transaction_data, signature, public_key):
    transaction_bytes = transaction_data.encode('utf-8')
    try:
        public_key.verify(
            signature,
            transaction_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        return True
    except Exception as e:
        return False

st.print(generate_keys())
