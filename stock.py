import streamlit as st
import FinanceDataReader as fdr
import datetime
import time

# Finance Data Reader
# https://github.com/financedata-org/FinanceDataReader

st.set_page_config(
    # emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    page_icon="🐶",
    page_title="곽선생 Streamlit :sunglasses:",
    layout="wide",
)

with st.sidebar:

    st.markdown(""" ## 게임주 종목 검색 """)


    option = ['069080', '078340', '225570', '036570']

    stock_data = {'웹젠': '069080', 
      '컴투스': '078340', 
      '넥슨게임즈': '225570', 
      '엔씨소프트': '036570'
      }

    stock = st.selectbox(
        '조회할 주식을 선택해 주세요',
        # option,  
        list(stock_data.keys()), 
        index=0
    )


    date = st.date_input(
        "조회 시작일을 선택해 주세요",
        datetime.datetime(2023, 1, 1)
    )



    # code = st.text_input(
    #     '종목코드', 
    #     value='',
    #     placeholder='종목코드를 입력해 주세요'
    # )

code = stock_data.get(stock) 

st.title(f"{stock} 종목 챠트 조회")


if stock and code:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'Close']

    print(data)     

    tab1, tab2 = st.tabs(['차트', '데이터'])

    with tab1:    
        st.line_chart(data)

    with tab2:
        st.dataframe(df.sort_index(ascending=False))

    with st.expander('컬럼 설명'):
        st.markdown('''
        - Open: 시가
        - High: 고가
        - Low: 저가
        - Close: 종가
        - Adj Close: 수정 종가
        - Volumn: 거래량
        ''')
