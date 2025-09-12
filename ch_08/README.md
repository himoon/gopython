# Chapter 08 연관 키워드 경쟁 강도 분석

## 📋 실습 개요
이번 장에서는 **네이버 API 활용과 웹 애플리케이션 개발**을 통해 연관 키워드의 경쟁 강도를 분석하는 프로젝트를 진행합니다.
- **네이버 API**를 활용한 쇼핑 상품 검색 및 연관 키워드 분석
- **datakart** 패키지로 다양한 API 데이터 수집
- **pandas** 패키지로 키워드 데이터 처리 및 경쟁 강도 분석
- **streamlit** 패키지로 인터랙티브 웹 애플리케이션 구축

## ⚙️ 패키지 설치
실습을 원활하게 진행하기 위해 비주얼 스튜디오 코드 터미널에서 아래 명령어를 실행하여 필요한 파이썬 패키지들을 설치해주세요.

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
- **서비스 API** ([step_1_2.py](step_1_2.py)): Client ID와 Client Secret 입력
- **검색광고 API** ([step_1_3.py](step_1_3.py)): 엑세스라이선스, 비밀키, CUSTOMER_ID 입력

### 💡 Streamlit 데이터프레임 스타일링 안내
Streamlit의 `st.dataframe()` 함수 기본 설정이 변경되어 천 단위 구분 기호가 자동으로 적용되지 않습니다.

**숫자 데이터 형식 개선 방법:**

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

## 🚀 실습 단계별 가이드

*   **[step_1_1.py](step_1_1.py)**: 실습 결과물을 저장할 `output` 폴더를 생성하여 기본 작업 환경을 구성합니다.

*   **[step_1_2.py](step_1_2.py)**: `datakart` 패키지를 사용하여 네이버 쇼핑 API에 "원피스"라는 키워드로 상품을 검색하고, 그 결과를 JSON 파일로 저장합니다. (API 키 필요)

*   **[step_1_3.py](step_1_3.py)**: `datakart` 패키지를 사용하여 네이버 검색 광고 API에서 "원피스"와 연관된 키워드 목록을 조회하고, 그 결과를 JSON 파일로 저장합니다. (API 키 필요)

*   **[step_2_1_kwd_tool.py](step_2_1_kwd_tool.py)**: `datakart`의 `keywords_tool`을 사용하여 특정 키워드("화장품") 또는 시즌 테마("반려동물")와 관련된 연관 키워드를 조회하는 방법을 익히는 기본 예제입니다.

*   **[step_2_1.py](step_2_1.py)**: 네이버 검색 광고 API로 특정 키워드(예: "나이키")의 연관 키워드 데이터를 조회한 후, `pandas`를 이용해 DataFrame으로 변환하고 CSV 파일로 저장합니다.

*   **[step_2_2.py](step_2_2.py)**: `step_2_1.py`에서 저장한 연관 키워드 CSV 파일을 읽어와서, 검색량이 10 미만인 데이터를 제거하고, 모바일 검색수 및 클릭률 조건을 적용하여 데이터를 정제한 후 새로운 CSV 파일로 저장합니다.

*   **[step_2_3.py](step_2_3.py)**: 정제된 연관 키워드 목록을 하나씩 네이버 쇼핑 API로 조회하여 각 키워드별 총 상품 수를 수집하고, `tqdm`으로 진행 상황을 표시하며 결과를 CSV 파일로 저장합니다.

*   **[step_2_4.py](step_2_4.py)**: 연관 키워드 데이터와 키워드별 상품 수 데이터를 합치고, '상품 수 / 모바일 검색 수' 공식을 이용해 '경쟁 강도'를 계산한 후, 최종 분석 결과를 CSV 파일로 저장합니다.

*   **[step_3_1.py](step_3_1.py)**: `streamlit`을 사용하여 키워드 분석 웹 앱의 기본 UI를 구성합니다. 사용자가 키워드를 입력하고 '분석하기' 버튼을 누르면, 이전 단계에서 만든 모든 분석 함수들을 순차적으로 실행하고 최종 결과를 `DataFrame`으로 화면에 표시합니다.

*   **[step_3_2.py](step_3_2.py)**: `step_3_1.py`의 웹 앱을 개선하여, `streamlit`의 `column_config`를 이용해 숫자 데이터(검색수, 상품수 등)를 프로그레스 바(Progress Bar) 형태로 시각화하여 보여줍니다.

*   **[step_x.py](step_x.py)**: `step_3_2.py`의 웹 앱에 시즌 테마를 선택할 수 있는 드롭다운 메뉴를 추가합니다. 사용자는 키워드를 직접 입력하거나 시즌 테마를 선택하여 연관 키워드 경쟁 강도를 분석할 수 있습니다.

모든 준비가 완료되었다면 연관 키워드 경쟁 강도 분석 실습을 시작해보세요! 🚀
