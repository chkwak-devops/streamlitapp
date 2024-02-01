import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from time import sleep
from datetime import datetime as dt
import datetime
import random
from utils import show_code


def mapping_demo():

    
    def selectAnimal(kind):
        api_url = "https://api.thedogapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=10"
        if kind == "cat":
            api_url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=10"

        response = requests.get(api_url)
        return response.json()


    def draw_layout():  
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




    tab1, tab2 = st.tabs(['고양이 갤러리', '강아지 갤러리' ])

    with tab1:
        with st.spinner(text="페이지 로딩중..."):
            data = selectAnimal("cat")
            draw_layout()

    with tab2:
        with st.spinner(text="페이지 로딩중..."):
            data = selectAnimal("dog")
            draw_layout()



title_name = "포토갤러리 예시"
st.set_page_config(page_title=f'''{title_name}''', page_icon="🌍")
st.markdown(f'''# {title_name}''')
st.markdown("___")
# st.sidebar.header("Kwak Demo")

mapping_demo()


show_code(mapping_demo)
