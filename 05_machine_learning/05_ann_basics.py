"""인공신경망 기초

초보자용으로 퍼셉트론, 다층 퍼셉트론, 활성화 함수를 이해하는 예제입니다.
"""

import numpy as np

# 1) 퍼셉트론: 단일 뉴런의 동작
# 입력값 x1, x2와 가중치 w1, w2, bias b를 곱하고 합한 뒤 활성화 함수를 적용합니다.

def perceptron(x1, x2, w1=0.5, w2=0.5, bias=-0.3):
    z = w1 * x1 + w2 * x2 + bias
    return 1 if z >= 0 else 0

print("퍼셉트론 예시:")
print(perceptron(1, 1))
print(perceptron(0, 0))

# 2) 활성화 함수 예시: sigmoid, ReLU

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return max(0.0, x)

x = 2.0
print("\nSigmoid:", round(sigmoid(x), 4))
print("ReLU:", relu(x))

# 3) 다층 퍼셉트론은 여러 퍼셉트론이 연결된 구조입니다.
# 일반적으로 입력층 -> 은닉층 -> 출력층으로 구성됩니다.
print("\n다층 퍼셉트론 개념:")
print("입력층 -> 은닉층 -> 출력층")
print("활성화 함수: ReLU, Sigmoid, Softmax 등")

print("\n핵심 해설:")
print("- 퍼셉트론은 가장 단순한 신경망 노드입니다.")
print("- 다층 퍼셉트론(MLP)은 비선형 문제를 해결할 수 있습니다.")
print("- 활성화 함수는 입력값을 비선형적으로 변환해 복잡한 패턴을 학습하게 합니다.")
