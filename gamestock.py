from tracemalloc import start
from matplotlib import ticker
import streamlit as st
import yfinance as yf
import pandas as pd 
import datetime


st.set_page_config(
    # emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    page_icon="🐶",
    page_title="곽선생 Streamlit :sunglasses:",
    layout="wide",
)


with st.sidebar:

    st.markdown(""" ## 게임주 종목 검색 """)

    tickers ={'웹젠': '069080.KS', 
            '엔씨소프트': '036570.KS',
            }

    reversed_ticker = dict(map(reversed,tickers.items()))

    dropdown = st.multiselect('select',tickers.keys())

    start = st.date_input('Start', value=pd.to_datetime('2023-01-01'))

    end = st.date_input('End',value=pd.to_datetime('today'))




# tickers =('TSLA','AAPL','MSFT','BTC-USD','ETH-USD','005930.KS')



if len(dropdown) > 0 :
    for i in dropdown:
        # df = yf.download(tickers[i],start,end)['Adj Close']   
        df = yf.download(tickers[i],start,end)['Adj Close']
        st.title(reversed_ticker[tickers[i]])

        # st.write("## raw")  
        # df

        
        st.write("## Chart")  
        st.line_chart(df)
        
