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


# Create a form using st.form
with st.form("Sentiment Analysis Form"):
    # Select distinct dates from the table
    cursor.execute("SELECT DISTINCT Date FROM df_new_table")
    dates = [row[0] for row in cursor.fetchall()]

    # Filter options for date range and company name
    selected_start_date = st.selectbox("Select Start Date", dates)
    selected_end_date = st.selectbox("Select End Date", dates)
    cursor.execute("SELECT DISTINCT Company_Name FROM df_new_table")
    companies = [row[0] for row in cursor.fetchall()]
    selected_company = st.selectbox("Select Company", companies)

    # Add a submit button to the form
    submit_button = st.form_submit_button("Submit")

# Filter the data based on the selected date range and company name
query = f"SELECT Summary_Sentiment_Label, COUNT(*) FROM df_new_table WHERE Date >= '{selected_start_date}' AND Date <= '{selected_end_date}' AND Company_Name = '{selected_company}' GROUP BY Summary_Sentiment_Label"
cursor.execute(query)
sentiment_counts = cursor.fetchall()

# Get the closing values for the selected date range and company name
closing_values_query = f"SELECT DISTINCT Date, closing_value FROM df_new_table WHERE Date >= '{selected_start_date}' AND Date <= '{selected_end_date}' AND Company_Name = '{selected_company}'"
cursor.execute(closing_values_query)
closing_values = cursor.fetchall()

# Display the results in Streamlit
st.write("Sentiment Analysis Results:")
st.write("Company:", selected_company)
st.write("Date Range:", selected_start_date, "to", selected_end_date)
st.write("Sentiment Counts:")
for sentiment_label, count in sentiment_counts:
    st.write(sentiment_label, ":", count)
st.write("Closing Values:")
for date, value in closing_values:
    st.write(date, ":", value)
    
