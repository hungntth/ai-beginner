import numpy as np

#Định nghĩa hàm số
def f(x):
    return 3*x**2 + 4*x + 3

#Tạo dãy giá trị x từ 0 đến 10
x = np.linspace(0, 10, 100)

# Tínhh giá trị y tương ứng với mỗi giá trị x
y = f(x)

#Tính tích phân của hàm số f(x) sử dụng hàm numpy.trapezoid

integral = np.trapezoid(y, x)

print(f"Tích phân của hàm số f(x) từ 0 đến 10 là: {integral}")