import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit 앱의 타이틀 설정
st.title('Product Price Comparison')

# 사용자로부터 상품명 입력 받기
product_name = st.text_input('Enter the product name')


print(product_name)


# 상품명이 입력된 경우에만 크롤링 수행
if product_name:
    # 쿠팡에서 상품 가격 정보 크롤링
    url = f'https://www.coupang.com/np/search?component=&q={product_name}'
    print(url)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    print(response)

    soup = BeautifulSoup(response.text, 'html.parser')
    price_coupang = soup.find('strong', {'class': 'price-value'}).get_text()


    print(price_coupang)

    # 이마트에서 상품 가격 정보 크롤링
    url = f'https://emart.ssg.com/search.ssg?target=all&query={product_name}'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_emart = soup.find('em', {'class': 'ssg_price'}).get_text()

    # 가격 정보를 데이터프레임으로 변환
    df = pd.DataFrame({'Store': ['Coupang', 'Emart'], 'Price': [price_coupang, price_emart]})

    # 가격 정보를 차트로 표시
    fig, ax = plt.subplots()
    ax.bar(df['Store'], df['Price'])
    st.pyplot(fig)