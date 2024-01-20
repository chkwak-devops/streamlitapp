import streamlit as st
import random


def get_random_num_list(n):
    return [random.randint(1, 100) for _ in range(n)]

# view = [100, 150, 30]  
view = get_random_num_list(3)
st.write("# 유튜브 조회수") 

st.write("## raw")  
view

st.write("## 그래프") 
st.bar_chart(view)
