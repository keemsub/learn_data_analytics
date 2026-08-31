"""머신러닝 기초: 선형 회귀

간단한 회귀 모델로 광고비를 입력받아 매출을 예측하는 예제입니다.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 데이터 로드
sales_df = pd.read_csv("data/sample_sales.csv")

# 입력 변수(X)와 타깃(y) 설정
X = sales_df[["advertising"]]
y = sales_df["sales"]

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 예측
predictions = model.predict(X_test)

# 성능 평가
mse = mean_squared_error(y_test, predictions)
print("모델 계수:", model.coef_)
print("절편:", model.intercept_)
print("평균 제곱 오차(MSE):", round(mse, 2))

# 예측 예시
new_ad = pd.DataFrame({"advertising": [150]})
print("광고비 150일 때 예상 매출:", model.predict(new_ad)[0])
