"""기초 통계 확장: 확률, 표본, 추정

품질관리에서 자주 쓰이는 개념입니다.
- 확률: 어떤 사건이 발생할 가능성
- 표본: 전체 데이터의 일부
- 평균과 분산을 이용한 추정
"""

import random

# 제품 불량 확률 예시
products = ["양품", "불량", "양품", "양품", "불량", "양품", "양품", "양품"]
prob_defect = products.count("불량") / len(products)
print("샘플 불량률:", round(prob_defect, 3))

# 표본 추출 시뮬레이션
population = list(range(1, 101))
random_sample = random.sample(population, 10)
print("무작위 표본:", random_sample)
print("표본 평균:", round(sum(random_sample) / len(random_sample), 2))

# 불량률에 대한 해석
print("해석: 전체적으로 불량률이 낮다면 공정이 안정적이라고 평가할 수 있습니다.")
