"""시각화 기초: matplotlib, seaborn

데이터를 시각화하면 패턴과 이상치를 빠르게 파악할 수 있습니다.
"""

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

matplotlib.rcParams["font.family"] = [
    "NanumGothic",
    "Malgun Gothic",
    "Noto Sans CJK KR",
    "AppleGothic",
    "sans-serif",
]
matplotlib.rcParams["axes.unicode_minus"] = False

# 샘플 데이터 로드
sales_df = pd.read_csv("data/sample_sales.csv")

# 1) 막대 그래프: 지역별 총 매출
region_sales = sales_df.groupby("region")["sales"].sum().sort_values()
region_sales.plot(kind="bar", color="steelblue")
plt.title("지역별 총 매출")
plt.xlabel("지역")
plt.ylabel("매출")
plt.tight_layout()
plt.show()

# 2) 산점도: 광고비와 매출의 관계
sns.scatterplot(data=sales_df, x="advertising", y="sales", hue="region")
plt.title("광고비와 매출 관계")
plt.tight_layout()
plt.show()

# 3) 박스플롯: 지역별 매출 분포
sns.boxplot(data=sales_df, x="region", y="sales")
plt.title("지역별 매출 분포")
plt.tight_layout()
plt.show()
