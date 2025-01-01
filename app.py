import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import calendar as cal
import seaborn as sns
from dateutil.relativedelta import relativedelta
import time

st.set_page_config(page_title="League")

st.header("FreqSevModel")
st.subheader("", divider="rainbow")


st.subheader("If you were sent to war, how would you fight your opponents? Pick 3.")

