"""품질관리 통계: 공정관리 기초

품질관리에서는 평균, 표준편차, 관리한계(USL/LSL)를 이해하는 것이 중요합니다.
"""

import statistics

# 예시: 제품 두께 데이터 (mm)
thickness = [10.1, 10.0, 9.9, 10.2, 10.1, 9.8, 10.3, 10.0, 10.2, 10.1]
mean_value = statistics.mean(thickness)
std_value = statistics.pstdev(thickness)

lsl = 9.8
usl = 10.3

print("두께 데이터:", thickness)
print("평균:", round(mean_value, 3))
print("표준편차:", round(std_value, 3))
print("LSL:", lsl)
print("USL:", usl)

# 관리상 경계 내에 있는지 확인
within_spec = all(lsl <= x <= usl for x in thickness)
print("모든 샘플이 규격 내에 있는가?", within_spec)

# 간단한 해석
if within_spec:
    print("공정이 규격 내에서 안정적으로 운영되고 있습니다.")
else:
    print("일부 샘플이 규격을 벗어나므로 공정을 점검해야 합니다.")
