# Chapter 08 연관 키워드 경쟁 강도 분석

## 📋 실습 개요
이번 장에서는 **네이버 API 활용과 웹 애플리케이션 개발**을 통해 연관 키워드의 경쟁 강도를 분석하는 프로젝트를 진행합니다.
- **네이버 API**를 활용한 쇼핑 상품 검색 및 연관 키워드 분석
- **datakart** 패키지로 다양한 API 데이터 수집
- **pandas** 패키지로 키워드 데이터 처리 및 경쟁 강도 분석
- **streamlit** 패키지로 인터랙티브 웹 애플리케이션 구축

## 📁 실습 파일 구조
```
ch_08/
├── step_1_1.py         # 기본 디렉토리 설정
├── step_1_2.py         # 네이버 쇼핑 API 실습
├── step_1_3.py         # 네이버 검색광고 API 키워드 도구 실습
├── step_2_1_kwd_tool.py # 키워드 도구 실습
├── step_2_1.py         # 연관 키워드 추출 함수
├── step_2_2.py         # 연관 키워드 데이터 정제
├── step_2_3.py         # 키워드별 상품 개수 추출
├── step_2_4.py         # 연관 키워드 경쟁 강도 계산
├── step_3_1.py         # Streamlit 웹 앱 기본 구성
├── step_3_2.py         # 고급 Streamlit 데이터 시각화
├── step_x.py           # 미니 프로젝트: 시즌 테마 키워드 분석
└── output/             # 분석 결과 및 데이터 저장 폴더
```

## ⚙️ 패키지 설치
실습을 진행하기 위해 비주얼 스튜디오 코드 터미널에 아래 명령어를 입력하여 파이썬 패키지를 설치하세요.

```shell
pip install -U datakart pandas streamlit tqdm
```

> **📝 참고**: `datakart` 패키지는 네이버 API를 간편하게 사용할 수 있게 해주는 파이썬 패키지입니다. `streamlit`은 파이썬으로 웹 애플리케이션을 빠르게 구축할 수 있는 프레임워크입니다.

## 🚨 중요한 사전 준비사항

### 🔑 API 키 설정 필수!
이번 실습은 네이버의 두 가지 API를 활용하므로 **각각의 API 키 설정**이 필요합니다:
- **서비스 API**: 네이버 개발자센터 가입 및 애플리케이션 등록
  - Client ID와 Client Secret 발급 (쇼핑 검색용)
- **검색광고 API**: 네이버 검색광고 가입 및 API 신청
  - Access License, Secret Key, Customer ID 발급 (키워드 도구용)

### 💡 키워드 분석 실습 개요
이번 실습은 실제 검색 데이터를 활용한 마케팅 분석 프로젝트입니다:
- **실시간 키워드 분석**: 네이버 API에서 최신 검색 트렌드 수집
- **경쟁 강도 측정**: 키워드별 경쟁 정도를 수치화하여 분석
- **웹 애플리케이션**: Streamlit으로 사용자 친화적인 분석 도구 제작
- **데이터 시각화**: 직관적인 차트와 표로 분석 결과 표현

### 🌐 인터넷 연결 필수!
API 데이터 수집을 위해서는 **안정적인 인터넷 연결**이 필요합니다:
- 네이버 API 서버 접속
- 실시간 키워드 데이터 수집
- Streamlit 웹 애플리케이션 실행

### 🔧 API 키 설정 방법
#### 1️⃣ 네이버 개발자센터 가입 (서비스 API)
1. [네이버 개발자센터](https://developers.naver.com/) 접속
2. 네이버 계정으로 로그인
3. "Application → 애플리케이션 등록" 선택
4. `검색` API 선택(네이버 쇼핑 검색 등 다양한 검색 서비스 사용 가능)
5. **Client ID**와 **Client Secret** 발급 확인

#### 2️⃣ 네이버 검색광고 가입 (검색광고 API)
1. [네이버 검색광고](https://searchad.naver.com/) 접속
2. 네이버 계정으로 로그인 후 광고주 가입
3. 사업자 정보 입력 (개인사업자 또는 법인)
4. "도구 → API 사용 관리" 접속
5. API 서비스 사용 신청
6. **엑세스라이선스**와 **비밀키**, **CUSTOMER_ID** 발급 확인

#### 3️⃣ API 키 설정
- **서비스 API** (step_1_2.py):
  - Client ID와 Client Secret 입력
- **검색광고 API** (step_1_3.py):
  - 엑세스라이선스, 비밀키, CUSTOMER_ID 입력

### ⚠️ API 사용 제한 주의사항
- API 호출 횟수 제한이 있을 수 있습니다
- 과도한 요청 시 일시적으로 접근이 제한될 수 있습니다
- 실습용으로만 사용하고 상업적 목적으로 남용하지 마세요

### 💡 Streamlit 데이터프레임 스타일링 안내
Streamlit의 `st.dataframe()` 함수 기본 설정이 변경되어 천 단위 구분 기호가 자동으로 적용되지 않습니다.

#### 📊 숫자 데이터 형식 개선 방법
숫자 데이터에 천 단위 구분 기호나 소수점 형식을 적용하려면:

**1️⃣ pandas 스타일링 방식 (step_3_1.py)**
```python
# 예시: 천 단위 구분 기호 및 소수점 형식 적용
styler = df_result.style.format({
    "검색수M": "{:,}",        # 천 단위 구분 기호, 정수 표시
    "클릭수M": "{:,.1f}",     # 소수점 첫째 자리
    "클릭률M": "{:,.2f}%",    # 소수점 둘째 자리 + % 기호
    "상품수": "{:,.0f}",      # 천 단위 구분 기호, 정수 표시
    "경쟁강도": "{:,.4f}",    # 소수점 넷째 자리
})
st.dataframe(styler, use_container_width=True)
```

**2️⃣ Streamlit column_config 방식 (step_3_2.py)**
```python
# 패키지 업데이트로 format 매개변수 설정 방식 변경
column_config={
    "검색수M": ProgressColumn(format="localized"),    # 기존: format="" → 변경: format="localized"
    "클릭수M": ProgressColumn(format="localized"),
    "클릭률M": ProgressColumn(format="localized"),
    "상품수": ProgressColumn(format="localized"),
    "경쟁강도": NumberColumn(format="%.2f"),          # 기존: format="" → 변경: format="%.2f"
}
```

> **⚠️ 중요**: Streamlit 패키지 업데이트로 인해 `ProgressColumn`의 `format` 매개변수에 빈 문자열(`""`) 대신 `"localized"`를, `NumberColumn`에는 `"%.2f"`와 같은 형식을 전달해야 합니다.

### 🆘 도움이 필요한 경우
- **서비스 API**: 네이버 개발자센터 가입 및 API 키 발급 문제
- **검색광고 API**: 네이버 검색광고 가입 및 사업자 정보 입력 문제
- API 연동 오류 발생
- Streamlit 웹 앱 실행 문제

**👉 저자의 오픈 채팅에 문의해 주세요!**

---

## 🎯 실습 시작 전 체크리스트
- [ ] 인터넷 연결 상태 확인
- [ ] 가상환경 설정 완료 (명령 팔레트 활용)
  - `F1` 또는 `Ctrl/Cmd+Shift+P` → `env` 입력 → `Python: 환경 만들기` 선택
  - `Venv` 선택 → 최신 Python 버전 선택
- [ ] 필수 패키지 설치 완료 (터미널 활용)
- [ ] 네이버 개발자센터 가입 및 API 키 발급
- [ ] 네이버 검색광고 가입 및 API 키 발급

## 🚀 실습 순서
1. **step_1_1.py**: 기본 환경 설정 및 폴더 생성
2. **step_1_2.py**: 네이버 쇼핑 API 연동 및 상품 검색
3. **step_1_3.py**: 네이버 검색광고 API 키워드 도구 실습
4. **step_2_1.py**: 연관 키워드 추출 및 CSV 변환
5. **step_2_2.py**: 연관 키워드 데이터 정제
6. **step_2_3.py**: 키워드별 상품 개수 추출
7. **step_2_4.py**: 연관 키워드 경쟁 강도 계산
8. **step_3_1.py**: Streamlit 기본 웹 애플리케이션 구성
9. **step_3_2.py**: 고급 Streamlit 데이터 시각화
10. **step_x.py**: 미니 프로젝트 - 시즌 테마 키워드 분석

모든 준비가 완료되었다면 연관 키워드 경쟁 강도 분석 실습을 시작해보세요! 🚀
