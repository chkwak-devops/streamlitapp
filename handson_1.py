import streamlit as st
import time

st.title(':one: 정적페이지 작성 예제')

















# st.title('this is title')
# st.header('this is header')
# st.subheader('this is subheader')
# st.write('this is a write')
# # emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# st.write(':blue[버튼]안녕하세요 :sparkles:')

# code = '''def hello():
#     print("Hello, Streamlit!")'''
# st.code(code, language='python')
# st.text('this is a text')


# st.markdown('''
# ---
# __Advertisement :)__
# - __[pica](https://nodeca.github.io/pica/demo/)__ - high quality and fast image
#   resize in browser.
# - __[babelfish](https://github.com/nodeca/babelfish/)__ - developer friendly
#   i18n with plurals support and easy syntax.
# You will like those projects!
# ---
# # h1 Heading 8-)
# ## h2 Heading
# ### h3 Heading
# #### h4 Heading
# ##### h5 Heading
# ###### h6 Heading

# ## Emphasis
# **This is bold text**
# __This is bold text__
# *This is italic text*
# _This is italic text_

# ~~Strikethrough~~
# ## Blockquotes

# > Blockquotes can also be nested...
# >> ...by using additional greater-than signs right next to each other...
# > > > ...or with spaces between arrows.

# ## Lists
# + Create a list by starting a line with `+`, `-`, or `*`
# + Sub-lists are made by indenting 2 spaces:
# - Marker character change forces new list start:
#   * Ac tristique libero volutpat at
#   + Facilisis in pretium nisl aliquet
#   - Nulla volutpat aliquam velit
# + Very easy!
# ''')

# st.image('flower.png', width=400, caption='streamlit')
# st.image('https://stimg.emart.com/store/images/new/common/gnb01.png', caption='Emart Logo')





# st.header(' LAYOUT 설정 예제', divider='gray')

# cols  = st.columns([1,1,1,1,])

# with cols[0] :
#   # column 1 영역
#   st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
# with cols[1] :
#   # column 2 영역
#   st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
#   st.divider()
#   st.checkbox('this is checkbox1 in col1')
# with cols[2] :
#   # column 3 영역
#   st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
# with cols[3] :
#   # column 4 영역
#   st.image('flower.png', width=100, caption='streamlit')
  





# st.header('Tab  설정 예제', divider='gray')
# tab1, tab2, tab3= st.tabs(['Tab A' , 'Tab B' , 'Tab C'])
# with tab1:
#   st.subheader("Tab A")
#   st.write('tab A 영역 내용을 표시합니다. ')
#   st.image('https://stimg.emart.com/upload/site/20240126_0957021_009.jpg')
    
# with tab2:
#   st.subheader("Tab B")
#   st.write('tab B 영역 내용을 표시합니다. ')
#   st.image('https://stimg.emart.com/upload/site/20240125_1545015_063.jpg')  

# with tab3:
#   st.subheader("Tab C")
#   st.write('tab B 영역 내용을 표시합니다. ')
#   st.image('https://stimg.emart.com/upload/site/20230607_1945005_315.jpg')  



# st.header(' Sidebar 설정 예제', divider='gray')
# with st.sidebar: 
#     st.title('사이드 메뉴 영역')

#     with st.expander("See explanation"):
#         st.write('''
#         생성형 AI 해커톤 대회 제출용 서비스 컨셉을 소개합니다. 
#         ''')
#         st.image("https://static.streamlit.io/examples/dice.jpg")



    


