    ## Streamlit 소개 
    #### The fastest way to build and share data apps
    가장 빠르게 데이터 어플리케이션을 만들 수 있는 방법을 제공하는 파이썬 기반 미니멀 프레임워크 
    - Check out [streamlit.io](https://streamlit.io)


    ## Streamlit 장점 
    - 파이썬으로 작성한 코드를 웹기반으로 간편하게 제작 후 배포 가능 
    - 풀스택(프런트와 백엔드 통합) 구현 가능
    - 예시 중심의 간결한 document 사이트 제공 
      - Check out (https://docs.streamlit.io)    
    - 활발한 갤러리, 커뮤니티 활동
      - Check out (https://streamlit.io/gallery), (https://streamlit.io/community)
    - Streamlit 자체 배포 관리 기능 제공(최대 3개까지 서브도메인 포함 무료 제공) 
      - Check out (https://share.streamlit.io)      
    - 화면 레코딩 기능 제공


    ## Streamlit 개발 환경 구성 
    - VSCode 설치 
    > vscode download [https://code.visualstudio.com/download](https://code.visualstudio.com/download)    
    - anaconda 환경 구성(권장)
    > anaconda download [https://www.anaconda.com/download](https://www.anaconda.com/download)
    - handson용 git clone
    ```
    $ git clone https://github.com/chkwak-devops/streamlitapp
    ```
    - VSCode IDE 실행 
    ```
    $ cd streamlitapp
    $ code .
    ```

    - python 환경 설정
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
    - streamlit 실행
    ```
    $ streamlit run {작성 파일명}
    ```
