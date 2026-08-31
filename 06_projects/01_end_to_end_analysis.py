"""종합 프로젝트 예제

샘플 판매 데이터를 기반으로 간단한 분석 흐름을 보여줍니다.
"""

import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.rcParams["font.family"] = [
    "NanumGothic",
    "Malgun Gothic",
    "Noto Sans CJK KR",
    "AppleGothic",
    "sans-serif",
]
matplotlib.rcParams["axes.unicode_minus"] = False

sales_df = pd.read_csv("data/sample_sales.csv")

# 기본 전처리
print("데이터 샘플:")
print(sales_df.head())

# 지역별 평균 매출
avg_by_region = sales_df.groupby("region", as_index=False)["sales"].mean()
print("\n지역별 평균 매출:")
print(avg_by_region)

# 간단한 시각화
plt.figure(figsize=(8, 5))
plt.bar(avg_by_region["region"], avg_by_region["sales"], color="darkorange")
plt.title("지역별 평균 매출")
plt.xlabel("지역")
plt.ylabel("평균 매출")
plt.tight_layout()
plt.show()

# 광고비와 매출 상관관계
corr = sales_df["advertising"].corr(sales_df["sales"])
print(f"\n광고비와 매출의 상관계수: {corr:.3f}")
