

import streamlit as st
import inspect
import textwrap
import pandas as pd
import pydeck as pdk
from utils import show_code
# from urllib.error import URLErrorad


def mapping_demo():

    st.title('this is title')
    st.header('this is header')
    st.subheader('this is subheader')
    st.write('this is a write')
    # emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    st.write(':blue[버튼]안녕하세요 :sparkles:')
    st.code('this is a code')  
    st.text('this is a text')


    st.markdown('''
                
    ---
    __Advertisement

    - __[pica](https://nodeca.github.io/pica/demo/)__ - high quality and fast image
    resize in browser.
    - __[babelfish](https://github.com/nodeca/babelfish/)__ - developer friendly
    i18n with plurals support and easy syntax.

    You will like those projects!
    ---

    # h1 Heading 8-)
    ## h2 Heading
    ### h3 Heading
    #### h4 Heading
    ##### h5 Heading
    ###### h6 Heading


    ## Emphasis

    **This is bold text**

    __This is bold text__

    *This is italic text*

    _This is italic text_

    ~~Strikethrough~~


    ## Blockquotes

    > Blockquotes can also be nested...
    >> ...by using additional greater-than signs right next to each other...
    > > > ...or with spaces between arrows.


    ## Lists

    + Create a list by starting a line with `+`, `-`, or `*`
    + Sub-lists are made by indenting 2 spaces:
    - Marker character change forces new list start:
        * Ac tristique libero volutpat at
        + Facilisis in pretium nisl aliquet
        - Nulla volutpat aliquam velit
    + Very easy!

    ''')


    st.divider()



    # 특수 이모티콘 삽입 예시
    # emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
    st.title('스마일 :sunglasses:')

    # Header 적용
    st.header('헤더를 입력할 수 있어요! :sparkles:')

    # Subheader 적용
    st.subheader('이것은 subheader 입니다')

    # 캡션 적용
    st.caption('캡션을 한 번 넣어 봤습니다')

    # 코드 표시
    sample_code = '''
    def function():
        print('hello, world')
    '''
    st.code(sample_code, language="python")

    # 일반 텍스트
    st.text('일반적인 텍스트를 입력해 보았습니다.')

    # 마크다운 문법 지원
    st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
    # 컬러코드: blue, green, orange, red, violet
    st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다.")
    st.markdown(":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:")

    # LaTex 수식 지원
    st.latex(r'\sqrt{x^2+y^2}=1')



st.set_page_config(page_title="Text Example", page_icon="🌍")
st.markdown("# Text 예시")
st.markdown("___")
# st.sidebar.header("Kwak Demo")

mapping_demo()


show_code(mapping_demo)
