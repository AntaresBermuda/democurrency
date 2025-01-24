import streamlit as st
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

# Initialize FastAPI
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# FastAPI endpoint
@app.get("/download/ledger")
async def download_csv():
    return FileResponse(
        "ledger.csv",
        media_type="text/csv",
        filename="ledger.csv"
    )

# Streamlit UI
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

# Display API information
st.markdown("""
### API Access
The CSV can be programmatically accessed at: `http://localhost:8000/download/ledger`
""")
