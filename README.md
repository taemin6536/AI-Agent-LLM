# AI Agent & LLM Study Project

이 프로젝트는 AI 에이전트와 대규모 언어 모델(LLM) 학습을 위한 다양한 예제들을 포함하고 있습니다.

## 📁 프로젝트 구조

```
AI-Agent-LLM/
├── chap02/                    # 2장: 기본 LLM 활용 예제
│   ├── gpt_basic.py          # 기본 GPT API 호출 예제
│   ├── single_turn.py       # 단일 턴 대화 예제
│   ├── multi_turn.py        # 다중 턴 대화 예제
│   ├── one_shot.py          # One-shot 학습 예제
│   ├── few_shot.py          # Few-shot 학습 예제
│   ├── mirror_in_snow_white.py  # 캐릭터 롤플레이 예제
│   └── streamlit_basic.py   # Streamlit 웹 인터페이스 예제
├── chap04/                    # 4장: 문서 처리 및 요약
│   ├── data/                 # 원본 PDF 파일
│   │   └── *.pdf            # 처리할 PDF 문서들
│   ├── output/              # 처리된 텍스트 및 요약 결과
│   │   ├── *.txt            # PDF에서 추출된 텍스트
│   │   └── summary_*.txt   # AI가 생성한 요약문
│   ├── pdf_to_txt.py        # PDF를 텍스트로 변환
│   ├── pdf_whitout_header_footer.py  # 헤더/푸터 제거 후 변환
│   └── summary.py           # 텍스트 요약 생성
└── README.md
```

## 🚀 시작하기

### 필수 요구사항

- Python 3.8+
- OpenAI API 키
- 필요한 Python 패키지들

### 설치

1. 저장소 클론:
```bash
git clone <repository-url>
cd AI-Agent-LLM
```

2. 가상환경 생성 및 활성화:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 필요한 패키지 설치:
```bash
pip install openai python-dotenv streamlit pymupdf
```

4. 환경 변수 설정:
`.env` 파일을 생성하고 OpenAI API 키를 설정하세요:
```
OPEN_API_KEY=your_openai_api_key_here
```

## 📚 예제 설명

### 1. 기본 GPT API 호출 (`gpt_basic.py`)
- OpenAI GPT API의 기본적인 사용법을 보여줍니다
- 단순한 질문-답변 형태의 상호작용

### 2. 단일 턴 대화 (`single_turn.py`)
- 매번 새로운 대화 세션으로 시작하는 예제
- 시스템 프롬프트를 통한 AI 역할 설정

### 3. 다중 턴 대화 (`multi_turn.py`)
- 대화 히스토리를 유지하는 채팅 봇
- 연속적인 대화가 가능한 구조

### 4. One-shot 학습 (`one_shot.py`)
- 하나의 예제를 통해 AI에게 패턴을 학습시키는 방법
- 유치원생 역할로 동물 소리 학습 예제

### 5. Few-shot 학습 (`few_shot.py`)
- 여러 예제를 통해 AI에게 패턴을 학습시키는 방법
- 더 정확한 패턴 인식이 가능

### 6. 캐릭터 롤플레이 (`mirror_in_snow_white.py`)
- 특정 캐릭터의 성격과 말투를 모방하는 예제
- 백설공주 이야기의 마법 거울 역할

### 7. Streamlit 웹 인터페이스 (`streamlit_basic.py`)
- 웹 브라우저에서 사용할 수 있는 채팅 인터페이스
- 조커 캐릭터로 설정된 AI와 대화 가능

## 📄 문서 처리 및 요약 (chap04)

### 8. PDF 텍스트 추출 (`pdf_to_txt.py`)
- PDF 파일을 텍스트로 변환하는 기본 예제
- PyMuPDF 라이브러리를 사용한 문서 처리

### 9. PDF 전처리 (`pdf_whitout_header_footer.py`)
- PDF에서 헤더와 푸터를 제거한 후 텍스트 추출
- 더 깔끔한 텍스트 데이터를 위한 전처리 과정

### 10. AI 텍스트 요약 (`summary.py`)
- 추출된 텍스트를 AI를 활용하여 요약
- 저자의 문제 인식과 주장을 파악하는 구조화된 요약 생성
- 학술 논문이나 긴 문서의 핵심 내용을 빠르게 파악

## 🎯 실행 방법

### 개별 예제 실행
```bash
# 기본 GPT 예제
python chap02/gpt_basic.py

# 다중 턴 대화
python chap02/multi_turn.py

# Streamlit 웹 앱
streamlit run chap02/streamlit_basic.py

# PDF 처리 및 요약
python chap04/pdf_to_txt.py                    # PDF를 텍스트로 변환
python chap04/pdf_whitout_header_footer.py     # 헤더/푸터 제거 후 변환
python chap04/summary.py                       # AI 텍스트 요약
```

### Streamlit 웹 앱 사용법
1. 터미널에서 `streamlit run chap02/streamlit_basic.py` 실행
2. 브라우저에서 `http://localhost:8501` 접속
3. 조커 캐릭터와 대화 시작

## 🔧 주요 기능

- **다양한 학습 패턴**: Zero-shot, One-shot, Few-shot 학습 예제
- **대화형 인터페이스**: 콘솔 및 웹 기반 채팅 인터페이스
- **캐릭터 롤플레이**: 특정 캐릭터의 성격을 모방한 AI
- **대화 히스토리 관리**: 연속적인 대화를 위한 컨텍스트 유지
- **문서 처리**: PDF에서 텍스트 추출 및 전처리
- **AI 요약**: 긴 문서의 핵심 내용을 구조화된 요약으로 변환

## 📖 학습 목표

이 프로젝트를 통해 다음을 학습할 수 있습니다:

1. **LLM API 활용**: OpenAI GPT API의 기본 사용법
2. **프롬프트 엔지니어링**: 효과적인 시스템 프롬프트 작성
3. **대화 시스템 구축**: 멀티턴 대화를 위한 구조 설계
4. **웹 인터페이스 개발**: Streamlit을 활용한 사용자 인터페이스
5. **캐릭터 AI**: 특정 성격의 AI 에이전트 개발
6. **문서 처리**: PDF 파일에서 텍스트 추출 및 전처리
7. **AI 요약 시스템**: 긴 문서의 핵심 내용을 구조화된 요약으로 변환

## 🛠️ 기술 스택

- **Python 3.8+**
- **OpenAI API**: GPT 모델 활용
- **Streamlit**: 웹 인터페이스
- **PyMuPDF**: PDF 문서 처리
- **python-dotenv**: 환경 변수 관리

## 📝 주의사항

- OpenAI API 사용 시 비용이 발생할 수 있습니다
- API 키는 안전하게 보관하세요
- `.env` 파일은 버전 관리에 포함하지 마세요

## 🤝 기여하기

이 프로젝트는 학습 목적으로 제작되었습니다. 개선 사항이나 새로운 예제가 있다면 언제든 기여해주세요!

## 📄 라이선스

이 프로젝트는 교육 목적으로 자유롭게 사용할 수 있습니다.
