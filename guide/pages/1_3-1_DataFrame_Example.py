

import streamlit as st
import inspect
import textwrap
import numpy as np
import pandas as pd
import pydeck as pdk
from utils import show_code
from datetime import datetime as dt
import datetime




def mapping_demo():


    dataframe = pd.DataFrame({
        'A' : ['spam', 'eggs', 'spam', 'eggs'] * 6,
        'B' : ['alpha', 'beta', 'gamma'] * 8,
        'C' : [np.random.choice(pd.date_range(datetime.datetime(2013,1,1),datetime.datetime(2013,1,3))) for i in range(24)],
        'D' : np.random.randn(24),
        'E' : np.random.randint(2,10,24),
        'F' : [np.random.choice(['rand_1', 'rand_2', 'rand_4', 'rand_6']) for i in range(24)],
    })



    # DataFrame
    # use_container_width 기능은 데이터프레임을 컨테이너 크기에 확장할 때 사용합니다. (True/False)
    st.dataframe(dataframe, use_container_width=True)

    # 테이블(static)
    # DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
    st.table(dataframe.head(10))


    st.write("## 그래프") 

    columns1 = st.columns([1,1])
    with columns1[0]:
        st.bar_chart(dataframe['D'])
    with columns1[1]:
        st.line_chart(dataframe['D'])

    columns2 = st.columns([1,1])
    with columns2[0]:
        st.scatter_chart(dataframe['D'])
    with columns2[1]:
        st.area_chart(dataframe['D'])


    st.divider()


    # # 메트릭
    st.metric(label="온도", value="10°C", delta="1.2°C")
    st.metric(label="삼성전자", value="61,000 원", delta="-1,200 원")

    # 컬럼으로 영역을 나누어 표기한 경우
    col1, col2, col3 = st.columns(3)
    col1.metric(label="달러USD", value="1,228 원", delta="-12.00 원")
    col2.metric(label="일본JPY(100엔)", value="958.63 원", delta="-7.44 원")
    col3.metric(label="유럽연합EUR", value="1,335.82 원", delta="11.44 원")




title_name = "DataFrame 예시"
st.set_page_config(page_title=f'''{title_name}''', page_icon="🌍")
st.markdown(f'''# {title_name}''')
st.markdown("___")

mapping_demo()


show_code(mapping_demo)
