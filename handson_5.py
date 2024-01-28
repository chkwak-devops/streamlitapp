import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from io import BytesIO
from datetime import datetime as dt
import datetime
import random
import requests

st.title(':five 이미지 갤러리 예제')


tab1, tab2 = st.tabs(['고양이 갤러리', '챠트' ])

with tab1:
    with st.spinner(text="페이지 로딩중..."):
        # API 호출
        response = requests.get("https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=10")
        data = response.json()


        col1,col2 = st.columns([1,1])
        with col1 : 
            images = []
            captions = []
            for i in range(0, round(len(data)/2)):
                img_url = data[i]['url']
                response = requests.get(img_url)
                img = Image.open(BytesIO(response.content))
                images.append(img)
                captions.append(f"Image {i+1}")

            st.image(images, caption=captions, width=200)

        with col2 : 
            images = []
            captions = []
            for i in range(round(len(data)/2), len(data)):
                img_url = data[i]['url']
                response = requests.get(img_url)
                img = Image.open(BytesIO(response.content))
                images.append(img)
                captions.append(f"Image {i+1}")

            st.image(images, caption=captions, width=200)


