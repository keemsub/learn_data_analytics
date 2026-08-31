"""Python 기초: 조건문, 반복문, 함수

데이터 분석에서는 반복적인 계산을 함수로 만들어 재사용하는 것이 중요합니다.
"""

# 조건문
score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"점수 {score}점은 {grade} 등급입니다.")

# 반복문
numbers = [1, 2, 3, 4, 5]
print("짝수만 출력:")
for n in numbers:
    if n % 2 == 0:
        print(n)

# 함수 정의

def average(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


def is_pass(score):
    return score >= 60

scores = [55, 72, 88, 93, 60]
print("평균 점수:", average(scores))
print("합격 여부:", [is_pass(s) for s in scores])

# dictionary로 데이터 구조화
student_records = [
    {"name": "Alice", "score": 80},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 55},
]

for record in student_records:
    status = "합격" if is_pass(record["score"]) else "불합격"
    print(f"{record['name']} : {status}")
