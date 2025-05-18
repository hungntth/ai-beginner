import numpy as np

arr = np.array([10, 20, 30, 40, 50])

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Phép nhân ma trận
result = np.dot(matrix1, matrix2)

print("Kết quả phép nhân ma trận:")
print(result)