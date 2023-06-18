import streamlit as st

pageTitle = "Stock Market Analysis"
pageIcon = "📈"
pageLayout = "wide"

st.set_page_config(page_title=pageTitle, page_icon=pageIcon, layout=pageLayout)
st.title(pageTitle + " " + pageIcon)

# ----- DROP DOWN VALUES FOR COMPANY TO SELECT FOR ANALYSIS ------
import sqlite3
import streamlit as st
#import pandas as pd
#import matplotlib.pyplot as plt

# Establish a connection to the SQLite database
conn = sqlite3.connect('df_new.db')
cursor = conn.cursor()
