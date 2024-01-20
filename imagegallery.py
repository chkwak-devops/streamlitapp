import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from time import sleep
from datetime import datetime as dt
import datetime



# st.set_page_config(layout="wide")

# 페이지 기본 설정
st.set_page_config(
    page_icon="🐶",
    page_title="이마트 StoreProduct 개발2팀 Streamlit",
    layout="wide",
)
with st.sidebar:
    date = st.date_input(
        "조회 시작일을 선택해 주세요",
        datetime.datetime(2022, 1, 1)
    )

    code = st.text_input(
        '종목코드', 
        value='',
        placeholder='종목코드를 입력해 주세요'
    )






# API 호출
response = requests.get("https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=100")
data = response.json()

# # 이미지 출력
# for i in range(0, len(data)):
#     img_url = data[i]['url']
#     response = requests.get(img_url)
#     img = Image.open(BytesIO(response.content))
#     먀mg = img.resize((100, 100))
#     st.image(img, caption=f"Image {i+1}")


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
# st.image(images, caption=captions, width=200, use_column_width=True, output_format='png', clamp=False)
