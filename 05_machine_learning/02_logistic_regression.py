"""머신러닝 기초: 로지스틱 회귀 (분류)

이 예제는 광고비와 고객 수를 기반으로 '높은 매출' 여부를 분류합니다.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# 데이터 로드
sales_df = pd.read_csv("data/sample_sales.csv")

# 목표 변수 생성: 매출이 중앙값 이상이면 1, 아니면 0
sales_df["high_sales"] = (sales_df["sales"] >= sales_df["sales"].median()).astype(int)

# 입력 변수와 타깃 분리
X = sales_df[["advertising", "customers"]]
y = sales_df["high_sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 모델 학습
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 예측 및 평가
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("분류 정확도:", round(accuracy, 3))
print("\n분류 보고서:")
print(classification_report(y_test, predictions, target_names=["낮은 매출", "높은 매출"]))

# 예측 예시
sample = pd.DataFrame({"advertising": [150], "customers": [220]})
result = model.predict(sample)[0]
print("예측 결과:", "높은 매출" if result == 1 else "낮은 매출")
