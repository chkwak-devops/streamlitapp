

import streamlit as st
import inspect
import textwrap
import numpy as np
import pandas as pd
import pydeck as pdk
from datetime import datetime as dt
import datetime
from utils import show_code
import random
# from urllib.error import URLErrorad




def mapping_demo():


    def generate_lotto():
        lotto = set()

        while len(lotto) < 6:
            number = random.randint(1, 46)
            lotto.add(number)

        lotto = list(lotto)
        lotto.sort()
        return lotto


    button = st.button('로또를 생성해 주세요!')

    if button:
        for i in range(1, 6):
            st.subheader(f'{i}. 행운의 번호: :green[{generate_lotto()}]')
        st.write(f"생성된 시각: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")





title_name = "Lotto번호 생성기 예시"
st.set_page_config(page_title=f'''{title_name}''', page_icon="🌍")
st.markdown(f'''# {title_name}''')
st.markdown("___")
# st.sidebar.header("Kwak Demo")

mapping_demo()


show_code(mapping_demo)
