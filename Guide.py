# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Streamlit Guide",
        page_icon="👋",
    )

    st.write("# Streamlit Guide! 👋")
    st.sidebar.success("Select a demo above.")

    st.markdown("""
    ## Streamlit 소개 
    The fastest way to build and share data apps
    가장 빠르게 데이터 어플리케이션을 만들 수 있는 방법을 제공하는 파이썬 기반 미니멀 프레임워크 
    - Check out [streamlit.io](https://streamlit.io)

    """)

    st.image('mpa-hero.gif', caption='streamlit demo')

    st.markdown("""
    ## Streamlit 장점 
    - 파이썬으로 작성한 코드를 웹기반으로 간편하게 제작 후 배포 가능 
    - 풀스택(프런트와 백엔드 통합) 구현 가능
    - 다양한 예시 제공
    - 활발한 커뮤니티 지원
    - Streamlit 자체 배포 관리 기능 제공(최대 3개까지 서브도메인 포함 무료 제공) 
    - 화면 레코딩 기능 제공
    """)

    st.markdown("""
    ## Streamlit 개발 환경 구성 
    - VSCode 설치 
    > vscode download [https://code.visualstudio.com/download](https://code.visualstudio.com/download)    
    - anaconda 환경 구성(권장)
    > anaconda download [https://www.anaconda.com/download](https://www.anaconda.com/download)
    ```
    $ conda create -n streamlit-app python3.9
    $ conda env list
    $ conda acivate streamlit-app
    ```
    - streamlit 설치
    ```
    $ pip install streamlit
    ```
    """)





    # st.markdown(
    #     """
    #     Streamlit is an open-source app framework built specifically for
    #     Machine Learning and Data Science projects.
    #     **👈 Select a demo from the sidebar** to see some examples
    #     of what Streamlit can do!
    #     ### Want to learn more?
    #     - Check out [streamlit.io](https://streamlit.io)
    #     - Jump into our [documentation](https://docs.streamlit.io)
    #     - Ask a question in our [community
    #       forums](https://discuss.streamlit.io)
    #     ### See more complex demos
    #     - Use a neural net to [analyze the Udacity Self-driving Car Image
    #       Dataset](https://github.com/streamlit/demo-self-driving)
    #     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    # """
    # )


if __name__ == "__main__":
    run()
