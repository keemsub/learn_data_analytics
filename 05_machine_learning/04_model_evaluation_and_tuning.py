"""모델 평가와 튜닝 기초

모델은 단순히 학습만 해서 끝나는 것이 아니라
평가와 튜닝이 필요합니다.
"""

import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 샘플 데이터 로드
quality_df = pd.read_csv("data/manufacturing_data.csv")
X = quality_df[["temperature_c", "vibration_mm", "pressure_bar", "downtime_min"]]
y = quality_df["defect_flag"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 기본 모델
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("기본 모델 정확도:", round(accuracy_score(y_test, pred), 3))
print("혼동 행렬:\n", confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, target_names=["정상", "불량"]))

# 튜닝: GridSearchCV
param_grid = {
    "max_depth": [2, 3, 5, 8],
    "min_samples_split": [2, 5, 10],
}

search = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=3,
    scoring="accuracy",
)
search.fit(X_train, y_train)

print("\n최적 파라미터:", search.best_params_)
print("최적 교차검증 점수:", round(search.best_score_, 3))

print("\n개념 요약:")
print("- 모델 평가: 실제 성능을 측정하는 과정")
print("- 튜닝: 더 좋은 성능을 내는 하이퍼파라미터 탐색")
