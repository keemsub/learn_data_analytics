"""Python 기초: 변수, 자료형, 리스트, 딕셔너리

이 예제는 데이터 분석을 시작하기 전에 꼭 알아야 하는 기본 문법을 익히는 용도입니다.
"""

# 숫자와 문자열
age = 25
height = 175.5
name = "민수"

# 리스트: 여러 값을 하나로 묶을 때 사용
scores = [90, 85, 88, 95]

# 딕셔너리: 키-값 형태로 데이터 저장
student = {
    "name": name,
    "age": age,
    "height": height,
    "scores": scores,
}

print("이름:", student["name"])
print("나이:", student["age"])
print("점수 목록:", student["scores"])
print("평균 점수:", sum(scores) / len(scores))

# 문자열 포매팅
message = f"{student['name']} 학생의 평균 점수는 {sum(scores) / len(scores):.2f}점입니다."
print(message)

# 리스트를 활용한 간단한 데이터 처리
filtered_scores = [score for score in scores if score >= 90]
print("90점 이상 점수:", filtered_scores)
