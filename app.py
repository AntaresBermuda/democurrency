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
