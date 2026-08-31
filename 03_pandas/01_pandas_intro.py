"""pandas 기초

pandas는 테이블 형태의 데이터를 다루는 가장 기본적인 라이브러리입니다.
"""

import pandas as pd

# 딕셔너리를 DataFrame으로 변환
students = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [23, 25, 22, 27],
    "score": [88, 92, 75, 96],
}

df = pd.DataFrame(students)
print(df)
print("\n기본 통계:")
print(df.describe())

print("\n특정 컬럼 선택:")
print(df["score"])

print("\n조건 필터링:")
print(df[df["score"] >= 90])

print("\n새 컬럼 추가:")
df["grade"] = ["A", "A", "C", "A"]
print(df)
