"""TensorFlow 기초

본 예제는 아주 간단한 신경망 모델을 TensorFlow Keras로 구성하는 입문용 코드입니다.
"""

import numpy as np
import tensorflow as tf

# 간단한 입력값과 타깃값
X = np.array([[0.0], [1.0], [2.0], [3.0]], dtype=float)
y = np.array([0.0, 0.0, 1.0, 1.0], dtype=float)

# 모델 구성
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 학습
history = model.fit(X, y, epochs=200, verbose=0)

# 예측
pred = model.predict(np.array([[0.5], [2.5]], dtype=float))
print("모델 예측 확률:", pred.flatten())
print("최종 학습 손실:", round(history.history['loss'][-1], 4))

print("\n핵심 해설:")
print("- Dense는 완전 연결 신경망 층입니다.")
print("- activation='relu'는 비선형성을 추가합니다.")
print("- 출력층의 sigmoid는 이진 분류에 자주 사용됩니다.")
