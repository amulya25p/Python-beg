import yfinance as yf
import streamlit as st
import pandas as pd

#creating the app header
st.write("""
# Simple stock price app

Shown are the stock closing price and stock at google

""")

tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d', start='2001-1-1', end='2010-1-1')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)


st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)