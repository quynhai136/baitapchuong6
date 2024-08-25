# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:53:18 2024

@author: Student
"""

a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))
if b == 0:
    print("khong the chia cho 0.")
else:
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong_thuc = a / b
    thuong_nguyen = a // b
    du = a % b
#in ket qua ra man hinh
print("Tong:", tong)
print("Hieu:", hieu)
print("Tich:", tich)
print("Thuong (so thuc):", round(thuong_thuc, 3))
print("Thuong (so nguyen)):", thuong_nguyen)
print("So du:", du)