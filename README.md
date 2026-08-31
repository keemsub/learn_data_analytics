# 데이터 분석 교육 자료 프로젝트

이 프로젝트는 파이썬 기초 문법부터 통계, 데이터 분석, 시각화, 머신러닝, 그리고 딥러닝 기초까지 순서대로 학습할 수 있도록 구성한 교육용 예제 모음입니다. 특히 초보자용으로 설명을 쉽게 하며, 품질관리와 제조 데이터를 중심으로 실무적인 이해를 돕도록 구성했습니다.

## 폴더 구조

- `01_python_basics/`: 파이썬 기본 문법
- `02_statistics/`: 기초 통계, 확률, 품질관리 통계
- `03_pandas/`: pandas를 이용한 데이터 처리
- `04_visualization/`: 시각화 예제
- `05_machine_learning/`: 지도학습, 비지도학습, 모델 평가, 튜닝, 딥러닝 기초
- `06_projects/`: 종합 분석 프로젝트 및 품질관리 실무 사례
- `notebooks/`: Jupyter Notebook 버전 예제
- `data/`: 실습용 데이터

### 품질관리 실무 프로젝트
- `06_projects/02_manufacturing_case_study.py`: 제조 공정 데이터를 활용한 품질관리 사례
- `notebooks/07_manufacturing_project.ipynb`: 제조 품질관리 실습용 노트북

### 머신러닝 핵심 포인트
- 지도학습(Supervised Learning): 레이블이 있는 데이터로 학습
- 비지도학습(Unsupervised Learning): 레이블 없이 패턴을 찾는 학습
- 회귀(Regression): 연속형 값 예측
- 분류(Classification): 범주형 값 예측
- 모델 평가(Model Evaluation): 정확도, 정밀도, 재현율, F1 점수, 혼동행렬
- 모델 튜닝(Model Tuning): 하이퍼파라미터 탐색과 교차 검증
- 인공신경망(ANN): 퍼셉트론, 다층 퍼셉트론, 활성화 함수
- TensorFlow 기초: 신경망 모델을 간단히 구성하는 입문 예제

## 설치

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

TensorFlow는 초기 학습용으로 선택적으로 설치할 수 있습니다. 설치가 아직 되지 않았다면 아래처럼 직접 추가해도 됩니다.

```bash
pip install tensorflow-cpu
```

## 실행 예시

### Python 스크립트로 실행

```bash
python 01_python_basics/01_variables_and_data_types.py
python 02_statistics/01_descriptive_statistics.py
python 02_statistics/02_probability_and_sampling.py
python 02_statistics/03_quality_control.py
python 03_pandas/01_pandas_intro.py
python 04_visualization/01_matplotlib_and_seaborn.py
python 05_machine_learning/01_linear_regression.py
python 05_machine_learning/02_classification_model.py
python 05_machine_learning/03_supervised_vs_unsupervised.py
python 05_machine_learning/04_model_evaluation_and_tuning.py
python 05_machine_learning/05_ann_basics.py
python 05_machine_learning/06_tensorflow_intro.py
python 06_projects/01_end_to_end_analysis.py
python 06_projects/02_manufacturing_case_study.py
```

### Jupyter Notebook으로 실행

```bash
jupyter notebook notebooks
```

## 학습 순서

1. Python 기초 문법
2. 기본 통계 개념
3. 확률과 표본추출, 품질관리 통계
4. pandas로 데이터 다루기
5. 시각화로 패턴 확인
6. 머신러닝 기초: 지도학습/비지도학습
7. 모델 평가와 튜닝
8. 인공신경망 기초
9. TensorFlow 입문
10. 제조 품질관리 프로젝트 실습
11. Jupyter Notebook으로 정리 복습

## 참고

이 프로젝트는 교육용 샘플로서, 각 예제를 확장해 실제 데이터 분석 및 품질관리 실습으로 발전시킬 수 있습니다.
