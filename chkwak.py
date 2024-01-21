# app.py

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from io import BytesIO
from time import sleep
from datetime import datetime as dt
import datetime
import random
import requests

# 페이지 기본 설정
st.set_page_config(
    # emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    page_icon="🐶",
    page_title="이마트 StoreProduct 개발2팀 Streamlit :sunglasses:",
    layout="wide",
)


# 사이드 바 설정 
with st.sidebar:

    st.markdown(
        """ ## Streamlit 설치 방법 
        """)
    console_command = '''
    $ conda create --name streamlit python=3.9
    $ conda activate streamlit
    $ pip install streamlit 
    '''
    st.code(console_command, language="shellSession")

    st.markdown(
        """ ## Streamlit 실행  방법 
        """)
    console_command = '''
    $ streamlit run [작성화일명]
    '''
    st.code(console_command, language="shellSession")

    
    st.markdown(
        """ ## Streamlit 상세 가이드
          """)
    
    st.markdown(
        """ [https://docs.streamlit.io](https://docs.streamlit.io)
          """)

    st.markdown('---')

# 페이지 헤더, 서브헤더 제목 설정
st.header("반려동물 사진첩👋")

tab1, tab2 = st.tabs(['고양이 갤러리', '챠트' ])

with tab1:
    with st.spinner(text="페이지 로딩중..."):
        # API 호출
        response = requests.get("https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=10")
        data = response.json()
        

        # 이미지 출력
        images = []
        captions = []
        for i in range(0, len(data)):
            img_url = data[i]['url']
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
            images.append(img)
            captions.append(f"Image {i+1}")

        st.subheader('고양이 갤러리')
        st.image(images, caption=captions, width=200)

with tab2:
    st.subheader('챠트')
    # 페이지 컬럼 분할(예: 부트스트랩 컬럼, 그리드)
    cols = st.columns((1, 1, 2))
    cols[0].metric("10/11", "15 °C", "2")
    cols[0].metric("10/12", "17 °C", "2 °F")
    cols[0].metric("10/13", "15 °C", "2")
    cols[1].metric("10/14", "17 °C", "2 °F")
    cols[1].metric("10/15", "14 °C", "-3 °F")
    cols[1].metric("10/16", "13 °C", "-1 °F")

    # 라인 그래프 데이터 생성(with. Pandas)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    # 컬럼 나머지 부분에 라인차트 생성
    cols[2].line_chart(chart_data)

    def get_random_num_list(n):
        return [random.randint(1, 100) for _ in range(n)]


    sample_data = pd.DataFrame(np.random.rand(10, 10), columns=[f"col{i}" for i in range(10)])
    st.write(sample_data)  



    

