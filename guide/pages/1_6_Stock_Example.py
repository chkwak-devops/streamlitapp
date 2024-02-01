import streamlit as st
import yfinance as yf
import datetime
import FinanceDataReader as fdr

from utils import show_code


def mapping_demo():
    

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

    code = stock_data.get(stock) 

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



title_name = "주식정보 조회 예시"
st.set_page_config(page_title=f'''{title_name}''', page_icon="🌍")
st.markdown(f'''# {title_name}''')
st.markdown("___")

mapping_demo()


show_code(mapping_demo)
