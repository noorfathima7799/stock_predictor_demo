import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Simple Stock Price Viewer")

symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")
start = st.date_input("Start Date", pd.to_datetime("2018-01-01"))
end = st.date_input("End Date", pd.to_datetime("2023-01-01"))

if st.button("Fetch and View"):
    data = yf.download(symbol, start=start, end=end)

    if data.empty:
        st.error("No data found.")
    else:
        st.success("Data Loaded!")

        # Compute SMA
        data["SMA_10"] = data["Close"].rolling(window=10).mean()

        # Drop rows with NaN (from rolling)
        plot_data = data[["Close", "SMA_10"]].dropna()

        # Check again after drop
        if plot_data.empty:
            st.warning("Not enough data to calculate SMA. Try a longer date range.")
        else:
            st.dataframe(plot_data.tail())
            st.line_chart(plot_data)
