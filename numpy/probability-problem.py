# Bài toán kinh điển tung xúc xắc 6 mặt
import numpy as np

num_throws = 1000000  # Số lần tung xúc xắc
throws = np.random.randint(1, 7, num_throws)  # Tung xúc xắc
num_sixes = np.sum(throws == 6)  # Đếm số lần ra mặt 6

#Tính xác suất
probability = num_sixes / num_throws
print(f"Xác suất ra mặt 6: {probability}")