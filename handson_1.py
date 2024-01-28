import streamlit as st

st.title(':one: Text 예제')

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
__Advertisement :)__

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

Unordered

+ Create a list by starting a line with `+`, `-`, or `*`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!


''')

st.title(' LAYOUT 설정 예제')
st.divider()

col1,col2, col3 = st.columns([1,1, 1])

with col1 :
  # column 1 에 담을 내용
  st.text('column1 영역')
with col2 :
  # column 2 에 담을 내용
  st.text('column2 영역')
  st.divider()
  st.checkbox('this is checkbox1 in col1')
with col3 :
  # column 1 에 담을 내용
  st.text('column1 영역')
  

st.title('Tab 설정 예제')
st.divider()


tab1, tab2, tab3= st.tabs(['Tab A' , 'Tab B' , 'Tab C'])

with tab1:
  st.subheader("Tab A")
  st.write('tab A 영역 내용을 표시합니다. ')
    
with tab2:
  st.subheader("Tab B")
  st.write('tab B 영역 내용을 표시합니다. ')

with tab3:
  st.subheader("Tab C")
  st.write('tab B 영역 내용을 표시합니다. ')



st.title('Sidebar 설정 예제')
st.divider()

with st.sidebar: 
    st.title('사이드 메뉴 영역')
    st.write('message ...')


