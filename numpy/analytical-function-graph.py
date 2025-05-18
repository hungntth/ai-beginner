# Tính đạo hàm cho hàm số f(x) = x^3 + 2x^2 - 3x + 1

import numpy as np
import matplotlib.pyplot as plt

# Định nghĩa hàm số
def f(x):
    return x**3 + 2*x**2 - 3*x + 1

#Tạo dãy giá trị x từ -5 đến 5
x = np.linspace(-5, 5, 100)

# Tính giá trị y tương ứng với mỗi giá trị x
y = f(x)

#Tính đạo hàm của hàm số f(x)
dy_dx = np.gradient(y, x)

# Vẽ đồ thị hàm số f(x)
plt.figure(num="Đạo hàm", figsize=(10, 6))
plt.plot(x, y, label='f(x)', color='blue')
plt.plot(x, dy_dx, label="f'(x)", color='red')
plt.title('Đồ thị hàm số và đạo hàm')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
