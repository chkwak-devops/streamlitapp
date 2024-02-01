import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

st.title(':two: 입출력 UI 작성 예제')


# 텍스트 입력
name = st.text_input(
    label='이름을 입력해 주세요', 
    placeholder='이름 입력'
)

birthday = st.date_input("당신의 생일을 입력해 주세요")

# 숫자 입력
age = st.number_input(
    label='나이를 입력해 주세요.', 
    min_value=10, 
    max_value=100, 
    value=30,
    step=5
)

# 선택 박스
gender = st.selectbox(
    '당신의 성별은 무엇입니까?',
    ('남성', '여성'), 
    index=0
)


button = st.button("확인", type="primary") 

if button:  
    container = st.container(border=True)
    container.write(f'당신의 이름은 :violet[{name}] 입니다.')    
    container.write(f'당신의 생일은 :violet[{birthday}] 입니다.')        
    container.write(f'당신의 나이는 :violet[{age}] 입니다')            
    container.write(f'당신의 성별은 :violet[{gender}] 입니다')        


















# columns = st.columns([1,1,1,1,1,1,1,])
# with columns[0]:
#     button1 = st.button("confrim", type="primary") 
# with columns[1]:
#     button2 = st.button("reset", type="secondary")

# if button1: 
#     st.write(':blue[버튼]이 눌렸습니다 :sparkles:')      


# # 파일 다운로드 버튼
# # 샘플 데이터 생성
# dataframe = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40],
# })

# # 다운로드 버튼 연결
# st.download_button(
#     label='CSV로 다운로드',
#     data=dataframe.to_csv(), 
#     file_name='sample.csv', 
#     mime='text/csv'
# )

# # 체크 박스
# agree = st.checkbox('동의 하십니까?')

# if agree:
#     st.write('동의 해주셔서 감사합니다 :100:')

# # 라디오 선택 버튼
# mbti = st.radio(
#     '당신의 MBTI는 무엇입니까?',
#     ('ISTJ', 'ENFP', 'ISTF', '선택지 없음'))

# if mbti == 'ISTJ':
#     st.write('당신은 :blue[현실주의자] 이시네요')
# elif mbti == 'ENFP' or mbti == 'ISTF':
#     st.write('당신은 :green[활동가] 이시네요')
# else:
#     st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

# # 선택 박스
# mbti = st.selectbox(
#     '당신의 MBTI는 무엇입니까?',
#     ('ISTJ', 'ENFP', '선택지 없음'), 
#     index=2
# )

# if mbti == 'ISTJ':
#     st.write('당신은 :blue[현실주의자] 이시네요')
# elif mbti == 'ENFP':
#     st.write('당신은 :green[활동가] 이시네요')
# else:
#     st.write("당신에 대해 :red[알고 싶어요]:grey_exclamation:")

# # 다중 선택 박스
# options = st.multiselect(
#     '당신이 좋아하는 과일은 뭔가요?',
#     ['망고', '오렌지', '사과', '바나나'],
#     ['망고', '오렌지'])

# st.write(f'당신의 선택은: :red[{options}] 입니다.')



# # 텍스트 입력
# title = st.text_input(
#     label='가고 싶은 여행지가 있나요?', 
#     placeholder='여행지를 입력해 주세요'
# )
# st.write(f'당신이 선택한 여행지: :violet[{title}]')

# # 숫자 입력
# number = st.number_input(
#     label='나이를 입력해 주세요.', 
#     min_value=10, 
#     max_value=100, 
#     value=30,
#     step=5
# )
# st.write('당신이 입력하신 나이는:  ', number)

# # 날짜 입력
# d = st.date_input("당신의 생일을 입력해 주세요")
# st.write('Your birthday is:', d)
