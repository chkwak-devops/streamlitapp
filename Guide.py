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
    - 잘 정리된 사용법 및 다양한 예시 제공 
      - Check out (https://docs.streamlit.io)    
    - 활발한 갤러리, 커뮤니티 활동
      - Check out (https://streamlit.io/gallery), (https://streamlit.io/community)
    - Streamlit 자체 배포 관리 기능 제공(최대 3개까지 서브도메인 포함 무료 제공) 
      - Check out (https://share.streamlit.io)      
    - 화면 레코딩 기능 제공
    - 단기간에 기획 아이디어 prototype 신속 구현 가능, 특히 해커톤 행사에 효과적
      - 숙명여대 해커톤 (https://www.smileshark.kr/post/2023-sookmyung-x-aws-x-streamlit-hackathon-mentoring-review-aws-tech-support)  
    """)

    st.markdown("""
    ## Streamlit 개발 환경 구성 
    - VSCode 설치 
    > vscode download [https://code.visualstudio.com/download](https://code.visualstudio.com/download)    
    - anaconda 환경 구성(권장)
    > anaconda download [https://www.anaconda.com/download](https://www.anaconda.com/download)
    ```
    $ conda create -n streamlit-app python=3.9
    $ conda env list
    $ conda activate streamlit-app
    ```
    - streamlit 설치
    ```
    $ pip install streamlit
    ```
    - 필요 라이브러리 화일(requirements.txt) 작성 및 설치
    ```
    $ pip install -r requirements.txt

    ```
    - handson git clone 
    ```
    $ git clone https://github.com/chkwak-devops/streamlitapp

    ```    
    - VSCode IDE 실행
    ```
    $ cd streamlitapp
    $ code .
    ```

    - python 개발 환경 설정
    ```
    $ conda create -n streamlit-app python=3.9
    $ conda env list
    $ conda activate streamlit-app
    ```

    - streamlit 실행
    ```
    $ streamlit run {작성 파일명}
    ```
    
    """)



if __name__ == "__main__":
    run()
