# Pykored

## 개요
- `pykored` 모듈은 [yako red](https://yakored1.net)에서 비디오를 다운로드하는 Python 기반 도구입니다.
- [다운로드](https://github.com/user-attachments/files/18134933/pykored.zip) 받고 나서 바로 cmd에서 사용해도 됩니다!
- cmd 사용예시
```bash
pykored https://yakored1.net/top/all/video/999999-example-page
```
### 기능:
### 야코 레드 영상을 다운로드합니다.
- 웹페이지에서 비디오 ID와 제목 추출.
- M3U8 플레이리스트를 가져오고 세그먼트 URL을 파싱.
- 비디오 세그먼트를 비동기적으로 다운로드.
- 비디오 세그먼트를 하나의 MP4 파일로 병합.
- 사용자 정의 출력 디렉토리 지원.

## 로컬로 사용하기
```bash
pip install .
```
아래와 같이 cmd에서 직접 사용 가능하다!
```bash
pykored <video_url> [output_directory]
```

## 설치 방법

1. 리포지토리 클론하기:
    ```bash
    git clone <repository_url>
    cd pykored
    ```

2. 의존성 설치:
    ```bash
    pip install -r requirements.txt
    ```

## 사용 방법

이 모듈은 비디오 다운로드를 위한 `Yako` 클래스를 제공합니다.

### 예시

```python
from pykored import Yako

# 비디오 URL로 Yako 초기화
url = "https://yakored1.net/top/all/video/999999-example-page"
yako = Yako(url)

# 기본 './downloads' 디렉토리에 비디오 다운로드
yako.download()

# 사용자 정의 디렉토리에 비디오 다운로드
yako.download(output_dir='./custom_directory')
```

## 파일 구조

```
pykored/
├── __init__.py        
├── __main__.py          
├── downloader.py       
├── m3u8_handler.py      
├── segmenter.py
├── utils.py             
├── video_manager.py    
└── requirements.txt
```

## 작동 원리

1. **초기화**: `Yako` 클래스는 비디오 URL로 초기화됩니다.
2. **비디오 정보 가져오기**: 제공된 URL에서 비디오 ID와 제목을 추출합니다.
3. **M3U8 콘텐츠 가져오기**: 비디오와 연결된 M3U8 플레이리스트 파일을 가져옵니다.
4. **세그먼트 다운로드**: M3U8 파일에 나열된 모든 비디오 세그먼트를 비동기적으로 다운로드합니다.
5. **세그먼트 병합**: 다운로드된 세그먼트를 하나의 MP4 파일로 병합합니다.

## 의존성

- Python 3.8 이상
- aiohttp
- beautifulsoup4

의존성을 설치하려면:
```bash
pip install -r requirements.txt
```
## 참고 사항

- 제공된 비디오 URL이 도구의 추출 로직과 호환되는지 확인하세요.
- 출력 디렉토리가 존재하지 않으면 자동으로 생성됩니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 라이센스가 부여됩니다. 자세한 내용은 `LICENSE` 파일을 참고하세요.

## 기여 방법

1. 리포지토리를 포크(fork)하세요.
2. 기능 추가를 위한 브랜치를 만드세요:
    ```bash
    git checkout -b feature-name
    ```
3. 변경 사항을 커밋하세요:
    ```bash
    git commit -m "변경 사항 설명"
    ```
4. 브랜치에 푸시하세요:
    ```bash
    git push origin feature-name
    ```
5. 새로운 Pull Request를 생성하세요.
