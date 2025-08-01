import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Simple Stock Price Viewer")

# 1. Get user inputs
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")
start = st.date_input("Start Date", pd.to_datetime("2018-01-01"))
end = st.date_input("End Date", pd.to_datetime("2023-01-01"))

if st.button("Fetch and View"):
    # 2. Download stock data
    data = yf.download(symbol, start=start, end=end)

    if data.empty:
        st.error("No data found. Please check the symbol or date range.")
    else:
        st.success("Data Loaded!")

        # 3. Calculate Moving Average
        data["SMA_10"] = data["Close"].rolling(window=10).mean()

        # 4. Reset index for proper plotting
        data = data.reset_index()

        # 5. Drop rows with NaN
        plot_data = data[["Date", "Close", "SMA_10"]].dropna()

        # 6. Display last few rows
        st.subheader("📋 Latest Data")
        st.dataframe(plot_data.tail())

        # 7. Plot line chart using Altair for full control
        import altair as alt

        chart = alt.Chart(plot_data).transform_fold(
            ['Close', 'SMA_10'],
            as_=['Metric', 'Price']
        ).mark_line().encode(
            x='Date:T',
            y='Price:Q',
            color='Metric:N'
        ).properties(
            width=700,
            height=400,
            title=f"{symbol.upper()} - Closing Price vs 10-Day SMA"
        )

        st.altair_chart(chart, use_container_width=True)

