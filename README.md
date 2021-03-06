# 빅데이터 팀프로젝트 9조
- 한국외국어대학교 빅데이터 강의
- 자유주제. 단, 수집 및 분석 데이터 1G이상
- 수집/전처리/EDA/분석/시각화/ 결론 과정 상세 설명

---

## Project Intro/Objective
- 광물 수출 중심의 무역 구조가 국가의 HDI(Human Development Index)에 미치는 영향은 무엇일까?

<img src='https://images.velog.io/images/nathan29849/post/0ed90415-49de-4f2c-9727-6a1f124111f4/image.png' width='50%' >

- 수출에서의 광물 의존도 비율의 변동폭 / HDI의 변동폭 : 반비례 관계
- 벤치 마크 국가 : 점차 수출에서 광물 의존도 비율이 낮아지는 국가
- 벤치마크 국가의 HDI 지표 상승
- 광물 수입국 중 어떤 국가가 가장 많은 이익을 편취했는지의 여부


### Member & Role
- 정성우(LT, 15학번) : PPT, 데이터 시각화, 데이터 분석
- 박한석(LT, 16학번) : PPT, 데이터 전처리, 데이터 분석 자료 조사
- 황정연(LT, 16학번) : 프로젝트 발표, 데이터 시각화, 데이터 분석


### Technologies
- Python
- Pandas, jupyter
- etc.

---

## Preprocessing

- 주요 데이터 Size : 1.71GB (전처리 이전 raw data 기준)
- Resource : 
    - WTO STATS (https://stats.wto.org/)
        - WTO 통계 포털에서 무역 이슈와 관련된 상품 거래 및 서비스 통계(연간), 시장 접근 지표(경계, 적용 및 특혜 관세), 비관세 정보 및 기타 지표의 거래를 다룸.
    - HDI (1990 ~ 2019) (http://hdr.undp.org/en/indicators/137506) 
        - 1990 ~ 2019년에 해당하는 HDI(인간 개발 지수)

- Preprocessing : 1948년 ~ 2022년에 해당하는 전체 무역 거래 및 통계 지표 데이터에서 1990년 ~ 2019년에 해당하는 국가별 수출국가, 수출품목(Total, Fuels and Mining)에 따른 연도별 수출 규모(USD)에 해당하는 데이터만 추출 해내고자 함.

### Preprocessing 과정
- 1.1) 관련 행 추출
    - (Indicator, Reporting Economy, Product/Sector, Partner Economy, Value, Unit Code, Indicator Code)
- 1.2) 1-2. 특정 조건의 열 추출
    - 광물 수출 의존도를 보기위해 ~
        - Partner Economy(수출국가)를 World에 국한
        - Product/Sector(수출품목)를 ‘Total merchandise’, ‘Fuels and mining products’에 국한  
- 1.3) 연도 설정 (1990 ~ 2019) 및 연도를 행으로 하는 데이터 프레임 생성
- 1.4) 수출 품목에 따른 데이터 프레임 분류 (분업 목적)
    - ‘Total merchandise’와 ‘Fuels and mining products’를 각각 분류하여 엑셀 파일 생성
   
- 2.1) 결측치 처리를 위한 데이터 확보
    - ‘Fuels and mining products’(원자재) 의존도 및 HDI 엑셀 파일활용
    - 전반부 3년(1990 ~ 1992)과 후반부 3년(2017 ~ 2019)의 평균을 구함
    - 전반부 3년과 후반부 3년을 제외한 1993  ~ 2016년의 값은 분석에 사용하지 않음
    - 전반부 3년 대비 후반부 3년의 원자재 의존도/HDI의 상승률/상승폭을 구해 분석에 활용

- 2.2) 결측치 처리 : 분석 대상에서 제외
    - 전반부 3년의 값이 모두 결측치이거나, 후반부 3년의 값이 모두 결측치인 경우

- 2.3) 결측치 처리 : 정해진 기간의 평균 값을 대입
    - 전반부 3년 중 유효한 값이 하나 이상이면 결측치를 제외한 값들로 평균 계산
    - 후반부 3년 중 유효한 값이 하나 이상이면 결측치를 제외한 값들로 평균 계산


## 가설 검정

### 초기 가설
- 사하라 이남 아프리카 국가들은 자원 의존도가 유지되거나 상승하면서 HDI로 대표되는 국민들의 삶의 질이 낮아졌을 것이다.

### 가설 검정 과정
- 원자재 무역 의존도, HDI의 *1990~1992년 평균, 2017~2019년 평균 계산
- 국가별 약 30년 간의 무역 의존도, HDI 변화 계산
- 사하라 이남 국가와 비교할 벤치마크 국가 선정
- 사하라 이남 국가와 벤치마크 국가의 양 지표 변화 비교

### 가설 검정 결과

<img src='https://images.velog.io/images/nathan29849/post/31b38c27-59cf-4877-9d7f-325a444bc019/image.png' width='50%' >

- 결론적으로, 사하라 이남 국가에서 자원 의존도가 
높아지면 HDI가 하락한다는 가설은 확인하기 어려움.

- 사하라 이남 국가들은 HDI 상승폭과 자원 의존도의 
상승폭이 약한 음의 상관관계를 보이나 단정하기 어려움.
    - 하지만 자원 의존도가 크게 하락하고 HDI 상승폭도 낮은 반례 존재
    - 전체적인 데이터 부족으로 판단 어려움.

- 벤치 마크 국가들은 자원 의존도 상승폭과 HDI 상승폭이 약한 양의 상관관계를 보임

### 추가 검증
- 사하라 이남에 국한하지 않고, 원자재 무역의존도와 HDI 사이의 상관관계가 있을까?

- 조사 대상 국가
    - 1990 ~ 1992년 HDI 평균 0.7 이하의 중진국 이하 국가
    - 1990 ~ 1992년 원자재 무역의존도 평균 0.1 이상의 국가


### 추가 검증 결과

<img src='https://images.velog.io/images/nathan29849/post/840127b9-ad8b-476b-9122-6b6cd97c53c7/image.png' width='50%' >
<img src='https://images.velog.io/images/nathan29849/post/309eb7df-eb72-492b-8e51-daa3ce723050/image.png' width='55%' >

- 추가적인 검증 결과, 자원 의존도가 유지되거나 적은 폭으로 하락할 때 HDI가 가장 크게 상승하는 경향이 있음.

- 자원 의존도가 큰 폭으로 상승하거나 하락하는 경우, HDI 상승이 비교적 낮은 경향이 있음.

---

## 추가 가설 검정

### 추가 가설
- 자원 의존도가 높은 국가들은 그 생산 구조가 고착화 되었을 것이다.
- 비단 “사하라 이남 아프리카”같은 특정 지역 뿐 아니라, 빈민국과 개발도상국을 고착화시키려는 선진국들의 사다리 걷어 차기이다. 

### 자원 의존도 Heatmap(사하라 이남 국가를 제외한 국가들)
- 기존보다 빨강색이 옅어진 국가보다 전반적으로 짙어진 경향 확인 가능

<img src='https://images.velog.io/images/nathan29849/post/b6472343-e65d-40c9-8afe-88a462ba5091/image.png' width='50%' >

### Re-Preprocessing 과정
- 3.1) 기준 데이터 확보
    - 급격한 의존도의 변화가 없다고 가정, 전체 데이터 중 초기 10년에 의존도가 40% 이상 측정된 국가들 선별, 평균 도출 후 정리

- 3.2) 대조 데이터 형성
    - 3-1과정에서 추려진 국가들 대상으로 마지막 10년 의존도의 평균을 도출 후 정리


- 3.3) 데이터 비교
    - 대부분의 국가가 의존도의 평균이 높아진다면 가설과 부합하는 것으로 판단

### 추가 가설 검정 결과

<img src='https://images.velog.io/images/nathan29849/post/5baf5c85-d111-46cb-ad1b-0263a45ec1d4/image.png' width='50%' >
- 실제, 자원 의존도가 높은 국가들은 과거 대비 78%의 국가들이 의존도 상승

- 단, 기존 자원 의존도가 높았던 선진국들의 80%가 자원 의존도 상승

- 전반적으로 자원 의존도가 높은 대부분의 국가들이 의존도가 상승하는 것은 사실, 그러나 선진국들에게만 유리한 국제무역구조라는 점, 소위 “사다리 걷어차기”가 존재한다고 증명하기는 부족


--- 

### Appendix. 벤치마크 국가 선정 기준
- 1990 ~ 1992년 자원 의존도보다 2017 ~ 2019년 자원 의존도가 0.03 이상 하락한 국가(ratio gap이 0.03이하인 것이 기존 경제에서 자원 의존도가 있는 국가가 유의미하게 비중이
감소한 것으로 판단함.)

- 1990 ~ 1992년 HDI가 0.7 이하인 국가(사하라 이남 국가 중 최대값 : 0.63)