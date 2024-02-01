import streamlit as st
import datetime
import random
import time

st.title(':four: lotto 예제')


def generate_lotto():
        
    lotto = set()

    while len(lotto) < 6:
        number = random.randint(1, 46)
        lotto.add(number)

    lotto = list(lotto)
    lotto.sort()

    return lotto

def getNowTime(): 
    now = datetime.datetime.now()
    return f"생성시간 : {now.strftime('%Y-%m-%d %H:%M:%S')}"


# 사이드 바 설정 
with st.sidebar:
    button = st.button('로또번호 생성하기', type="primary")
    if button: 
        st.write(getNowTime())

if button:
        for i in range(1, 6):
            st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
