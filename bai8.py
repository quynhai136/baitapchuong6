# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:18:05 2024

@author: Student
"""

# Các giá trị trong biểu thức
a = 32
b = 0.2
c = 1/64
d = -0.25
e = 8/27
f = 1/3

# Tính toán biểu thức
A = (a**b) - ((c)**(d)) + ((e)**(f))

# Làm tròn kết quả đến 3 chữ số thập phân
A_rounded = round(A, 3)

# In kết quả
print("Kết quả của biểu thức A là:", A_rounded)
