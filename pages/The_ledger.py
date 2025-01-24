import streamlit as st
import pandas as pd
import os

st.title("The ledger")

df = pd.read_csv("ledger.csv")

# Save the file to a known location in the Streamlit app directory
STATIC_DIR = "static"
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)
    
# Save the CSV to the static directory
static_file_path = os.path.join(STATIC_DIR, "ledger.csv")
df.to_csv(static_file_path, index=False)

# Create a static download URL using Streamlit's file download component
download_path = f"/app/{STATIC_DIR}/ledger.csv"  # This will be the static path

st.markdown(f"""
### Download Options:
1. Direct file path: `{download_path}`
2. Using Python:
```python
import pandas as pd
df = pd.read_csv('{download_path}')
```
""")

# Display the data
st.markdown("### View ledger")
st.dataframe(df)

print("Static file path created at: " + static_file_path)
