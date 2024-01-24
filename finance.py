import streamlit as st
import yfinance as yf
from datetime import date, timedelta

# Streamlit 앱의 타이틀 설정
st.title('Real-time Dollar Exchange Rate')

# 사용자로부터 원단위 정보 입력 받기
amount_in_krw = st.number_input('Enter the amount in KRW')

# 실시간 달러 환율 정보 가져오기
end = str(date.today() + timedelta(days=1))
rate_data = yf.download('USDKRW=X', start=str(date.today()), end=end)
today_rate = rate_data['Close'].iloc[-1]

# 원단위 정보를 달러로 변환
amount_in_usd = amount_in_krw / today_rate

# 결과 표시
st.write(f'The amount in USD is {amount_in_usd}')