"""제조 도메인 프로젝트: 공정 데이터 분석

이 프로젝트는 생산 공정 데이터를 기반으로 불량률, 생산성, 설비 상태를 분석하고,
간단한 분류 모델로 고불량 구간을 예측하는 흐름을 보여줍니다.
"""

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

matplotlib.rcParams["font.family"] = [
    "NanumGothic",
    "Malgun Gothic",
    "Noto Sans CJK KR",
    "AppleGothic",
    "sans-serif",
]
matplotlib.rcParams["axes.unicode_minus"] = False

# 1) 데이터 로드
factory_df = pd.read_csv("data/manufacturing_data.csv")
print("데이터 샘플:")
print(factory_df.head())

# 2) 기본 KPI 요약
summary = (
    factory_df.groupby("line")
    .agg(
        avg_defect_rate=("defect_rate_pct", "mean"),
        avg_yield=("yield_rate", "mean"),
        avg_throughput=("throughput_per_hr", "mean"),
        avg_downtime=("downtime_min", "mean"),
    )
    .reset_index()
)
print("\n라인별 KPI 요약:")
print(summary)

# 3) 상관관계 확인
corr = factory_df[["temperature_c", "vibration_mm", "pressure_bar", "energy_kwh", "downtime_min", "defect_rate_pct"]].corr()
print("\n공정변수와 불량률 상관관계:")
print(corr[["defect_rate_pct"]].sort_values("defect_rate_pct", ascending=False))

# 4) 시각화
plt.figure(figsize=(10, 5))
plt.bar(summary["line"], summary["avg_defect_rate"], color="tomato")
plt.title("라인별 평균 불량률")
plt.xlabel("라인")
plt.ylabel("불량률(%)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(factory_df["vibration_mm"], factory_df["defect_rate_pct"], c=factory_df["temperature_c"], cmap="viridis")
plt.title("진동과 불량률 관계")
plt.xlabel("진동(mm)")
plt.ylabel("불량률(%)")
plt.colorbar(label="온도(℃)")
plt.tight_layout()
plt.show()

# 5) 분류 모델: 고불량 구간 예측
X = factory_df[["temperature_c", "vibration_mm", "pressure_bar", "downtime_min", "energy_kwh", "throughput_per_hr"]]
y = factory_df["defect_flag"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("\n고불량 예측 정확도:", round(accuracy_score(y_test, pred), 3))
print("\n분류 보고서:")
print(classification_report(y_test, pred, target_names=["정상", "고불량"]))

# 6) 실무 해석
print("\n실무 해석:")
print("- 불량률이 높아지는 구간은 고온, 높은 진동, 장시간 정지와 관련이 큽니다.")
print("- 라인별 KPI를 보면 특정 설비에서 불량률이 상대적으로 높으므로 점검 우선순위를 정할 수 있습니다.")
print("- 분류 모델을 통해 기계 상태와 공정 조건을 기반으로 고불량 가능성을 조기에 탐지할 수 있습니다.")
