import streamlit as st

pageTitle = "Stock Market Analysis"
pageIcon = "😊📈"
pageLayout = "wide"

st.set_page_config(page_title=pageTitle, page_icon=pageIcon, layout=pageLayout)
st.title(pageTitle + " " + pageIcon)

# ----- DROP DOWN VALUES FOR COMPANY TO SELECT FOR ANALYSIS ------
import sqlite3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
closing_values_query = f"SELECT Date, closing_value FROM df_new_table WHERE Date >= '{selected_start_date}' AND Date <= '{selected_end_date}' AND Company_Name = '{selected_company}'"
cursor.execute(closing_values_query)
closing_values = cursor.fetchall()

# Calculate the sentiment analysis based on the counts
positive_count = 0
neutral_count = 0
negative_count = 0

for sentiment_label, count in sentiment_counts:
    if sentiment_label == "positive":
        positive_count = count
    elif sentiment_label == "neutral":
        neutral_count = count
    elif sentiment_label == "negative":
        negative_count = count

# Determine the action based on sentiment counts
if positive_count > neutral_count and positive_count > negative_count:
    action = "Hold"
elif neutral_count > positive_count and neutral_count > negative_count:
    action = "Sell"
elif negative_count > positive_count and negative_count > neutral_count:
    action = "Buy"
else:
    action = "No Action"

# Display the results in Streamlit
st.write("Sentiment Analysis Results:")
st.write("Company:", selected_company)
st.write("Date Range:", selected_start_date, "to", selected_end_date)
st.write("Sentiment Counts:")
for sentiment_label, count in sentiment_counts:
    st.write(sentiment_label, ":", count)
st.write("Action:", action)
#st.write("Closing Values:")
#for date, value in closing_values:
    #st.write(date, ":", value)
##########################################################################################    
# Create a DataFrame from the closing values
#df_closing_values = pd.DataFrame(closing_values, columns=["Date", "Closing Value"])
#df_closing_values["Date"] = pd.to_datetime(df_closing_values["Date"])

# Create a line plot using Matplotlib to display the closing values over time
#fig, ax = plt.subplots(figsize=(10, 6))
#ax.plot(df_closing_values["Date"], df_closing_values["Closing Value"], color="blue", linewidth=2)

# Set the plot labels and title
#ax.set_xlabel("Date")
#ax.set_ylabel("Closing Value")
#ax.set_title("Closing Values for {} - {}".format(selected_start_date, selected_end_date))

# Set the x-axis ticks and labels
#ax.xaxis.set_major_locator(plt.MaxNLocator(6))
#ax.xaxis.set_tick_params(rotation=45, labelsize=8)

# Set the y-axis ticks and labels
#ax.yaxis.set_tick_params(labelsize=8)

# Add gridlines
#ax.grid(True, linestyle="--", linewidth=0.5)

# Display the graph in Streamlit
#st.pyplot(fig)

#################################################################################################

# Close the connection
conn.close()

#company = ["Maruti", "Mahindra & Mahindra", "Tata Motors"]
#stockData = {
   # "Maruti": {
        #"OPEN": 7500,
        #"HIGH": 8000,
        #"LOW": 7490,
        #"CLOSE": 7600
    #},
    #"Mahindra & Mahindra": {
        #"OPEN": 500,
        #"HIGH": 530,
        #"LOW": 490,
        #"CLOSE": 600
    #},
    #"Tata Motors": {
        #"OPEN": 750,
        #"HIGH": 800,
        #"LOW": 749,
        #"CLOSE": 760
    #}
#}

