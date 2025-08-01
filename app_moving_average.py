import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Simple Stock Price Viewer")

symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime("2018-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("2023-01-01"))

if st.button("Fetch and Predict"):
    data = yf.download(symbol, start=start_date, end=end_date)
    if data.empty:
        st.error("No data found.")
    else:
        st.success("Data Loaded!")
        data['SMA_10'] = data['Close'].rolling(window=10).mean()
        st.line_chart(data[['Close', 'SMA_10']])
        st.write(data.tail())
