import yfinance as yf
import streamlit as st
import pandas as pd


#Define the ticket symbol
tickerSymbol1 = "GOOGL"
tickerSymbol2 = "AAPL"

#get data on this ticker
tickerdata1 = yf.Ticker(tickerSymbol1)
tickerdata2 = yf.Ticker(tickerSymbol2)

#get the historical data of this ticker
tickerDf1 = tickerdata1.history(period = "1d", start = "2010-5-31", end = "2022-06-17")
tickerDf2 = tickerdata2.history(period = "1d", start = "2010-5-31", end = "2022-06-17")
#Open High Low Close Volume Dividends Stock Splits

st.write("""
# Simple Stock Price Application

Shown are the stock closing price and volume of Google
""")

st.line_chart(tickerDf1.Close)
st.line_chart(tickerDf1.Volume)

st.write("""
Shown are the stock closing price and volume of Apple
""")
st.line_chart(tickerDf2.Close)
st.line_chart(tickerDf2.Volume)