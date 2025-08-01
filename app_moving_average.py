import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Simple Stock Price Viewer")

# Inputs
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")
start = st.date_input("Start Date", pd.to_datetime("2018-01-01"))
end = st.date_input("End Date", pd.to_datetime("2023-01-01"))

# Run when button clicked
if st.button("Fetch and Predict"):
    data = yf.download(symbol, start=start, end=end)

    if data.empty:
        st.error("No data found.")
    else:
        st.success("Data Loaded!")

        # Compute 10-day simple moving average
        data["SMA_10"] = data["Close"].rolling(window=10).mean()

        # Show last rows
        st.dataframe(data.tail())

        # Plot
        st.line_chart(data[["Close", "SMA_10"]])
