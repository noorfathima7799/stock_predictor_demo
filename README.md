# 📈 Stock Predictor Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://stockpredictordemo-erwz5trrs7apzm8he2prbr.streamlit.app/)

A simple Streamlit web app to view historical stock prices and a 10-day Simple Moving Average (SMA) using data from Yahoo Finance.

🔗 **Live Demo**: [Open App](https://stockpredictordemo-erwz5trrs7apzm8he2prbr.streamlit.app/)

---

## 🚀 Features

- 📅 Select date range
- 💼 Choose any stock symbol (e.g., AAPL, TSLA, INFY)
- 📉 See 10-day Simple Moving Average (SMA)
- 📊 Clean chart powered by Altair

---

## 🛠 Built With

- [Streamlit](https://streamlit.io)
- [yfinance](https://github.com/ranaroussi/yfinance)
- [pandas](https://pandas.pydata.org/)
- [Altair](https://altair-viz.github.io/)

---

## 💻 Run Locally

```bash
git clone https://github.com/noorfathima7799/stock_predictor_demo.git
cd stock_predictor_demo
pip install -r requirements.txt
streamlit run app_moving_average.py
