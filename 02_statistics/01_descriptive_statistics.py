"""기초 통계: 기술통계

주요 개념:
- 평균
- 중앙값
- 분산/표준편차
- 최솟값/최댓값
"""

import statistics

sales = [120, 150, 170, 100, 130, 140, 160, 180, 190, 110, 145, 175]

mean_value = statistics.mean(sales)
median_value = statistics.median(sales)
variance_value = statistics.pvariance(sales)  # 모집단 분산
std_value = statistics.pstdev(sales)  # 모집단 표준편차

print("매출 데이터:", sales)
print(f"평균: {mean_value:.2f}")
print(f"중앙값: {median_value}")
print(f"분산: {variance_value:.2f}")
print(f"표준편차: {std_value:.2f}")
print(f"최솟값: {min(sales)}")
print(f"최댓값: {max(sales)}")

# 설명: 데이터의 중심 경향과 산포를 함께 봐야 해석이 정확합니다.
