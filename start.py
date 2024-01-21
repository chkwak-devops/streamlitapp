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


# 로딩바 구현하기
with st.spinner(text="페이지 로딩중..."):
    sleep(1)

# 페이지 헤더, 서브헤더 제목 설정
st.header("이마트 StoreProduct개발2팀 Streamlit 페이지에 오신걸 환영합니다👋")
st.subheader("페이지 분할 기능")
st.markdown('---')

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


st.subheader("입출력 Form 기능")
st.markdown('---')

# 버튼 클릭
button = st.button('버튼을 눌러보세요')

if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')


# 파일 다운로드 버튼
# 샘플 데이터 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

# 다운로드 버튼 연결
st.download_button(
    label='CSV로 다운로드',
    data=dataframe.to_csv(), 
    file_name='sample.csv', 
    mime='text/csv'
)

# 체크 박스
agree = st.checkbox('동의 하십니까?')

if agree:
    st.write('동의 해주셔서 감사합니다 :100:')

# 라디오 선택 버튼
mbti = st.radio(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ENFP', '선택지 없음'))

if mbti == 'ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ENFP', '선택지 없음'), 
    index=2
)

if mbti == 'ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti == 'ENFP':
    st.write('당신은 :green[활동가] 이시네요')
else:
    st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

# 다중 선택 박스
options = st.multiselect(
    '당신이 좋아하는 과일은 뭔가요?',
    ['망고', '오렌지', '사과', '바나나'],
    ['망고', '오렌지'])

st.write(f'당신의 선택은: :red[{options}] 입니다.')


# 슬라이더
values = st.slider(
    '범위의 값을 다음과 같이 지정할 수 있어요:sparkles:',
    0.0, 100.0, (25.0, 75.0))
st.write('선택 범위:', values)

start_time = st.slider(
    "언제 약속을 잡는 것이 좋을까요?",
    min_value=dt(2020, 1, 1, 0, 0), 
    max_value=dt(2020, 1, 7, 23, 0),
    value=dt(2020, 1, 3, 12, 0),
    step=datetime.timedelta(hours=1),
    format="MM/DD/YY - HH:mm")
st.write("선택한 약속 시간:", start_time)


# 텍스트 입력
title = st.text_input(
    label='가고 싶은 여행지가 있나요?', 
    placeholder='여행지를 입력해 주세요'
)
st.write(f'당신이 선택한 여행지: :violet[{title}]')

# 숫자 입력
number = st.number_input(
    label='나이를 입력해 주세요.', 
    min_value=10, 
    max_value=100, 
    value=30,
    step=5
)
st.write('당신이 입력하신 나이는:  ', number)

st.subheader("탭 분할 기능")
st.markdown('---')


tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', '고양이 갤러리'])

with tab1:
    st.header('Cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')
    
with tab2:
    st.header('Dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with tab3:
    st.header('고양이 갤러리')
    # API 호출
    response = requests.get("https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=100")
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

    st.image(images, caption=captions, width=200)


st.subheader("탭 분할 기능")
st.markdown('---')


def get_random_num_list(n):
    return [random.randint(1, 100) for _ in range(n)]


sample_data = pd.DataFrame(np.random.rand(10, 10), columns=[f"col{i}" for i in range(10)])
st.write(sample_data)  

st.write("## 그래프") 
st.area_chart(sample_data)
