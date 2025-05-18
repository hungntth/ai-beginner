import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu cho trục x, từ -10 đến 10 với 100 điểm

x = np.linspace(-10, 10, 100)

#tạo dữ liệu cho trục y bằng cách áp dụng hàm y = x^2
y = x ** 2

# Vẽ đồ thị
plt.figure(figsize=(8, 6))  # Kích thước của đồ thị
plt.plot(x, y, label='y = x^2', color='blue', linewidth=2)  # Vẽ đường đồ thị
#Tiêu đề cho đồ thị
plt.title('Đồ thị hàm số y = x^2', fontsize=16)  # Tiêu đề
plt.xlabel('Trục x', fontsize=14)  # Nhãn trục x
plt.ylabel('Trục y', fontsize=14)  # Nhãn trục y
plt.grid(True)  # Hiện lưới
plt.legend()  # Hiện chú thích
plt.show()  # Hiện đồ thị
# Lưu đồ thị vào file