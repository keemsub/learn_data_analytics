"""머신러닝 기초: 지도학습 vs 비지도학습

- 지도학습: 정답 라벨이 있는 데이터로 학습
- 비지도학습: 라벨 없이 패턴을 찾는 데이터로 학습
"""

from sklearn.cluster import KMeans
import pandas as pd

# 지도학습 예시: 품질 분류 데이터
quality_df = pd.DataFrame({
    "temperature_c": [70, 72, 68, 74, 66, 76],
    "vibration_mm": [2.0, 2.5, 1.8, 2.8, 1.6, 3.1],
    "label": ["정상", "주의", "정상", "주의", "정상", "고위험"],
})
print("지도학습 데이터 예시:")
print(quality_df)

# 비지도학습 예시: KMeans 클러스터링
features = quality_df[["temperature_c", "vibration_mm"]]
model = KMeans(n_clusters=2, random_state=42, n_init=10)
clusters = model.fit_predict(features)
print("\n비지도학습 클러스터 결과:")
print(clusters)

print("\n개념 정리:")
print("- 지도학습: 예측할 정답(라벨)이 있음")
print("- 비지도학습: 정답 없이 유사한 그룹을 찾음")
