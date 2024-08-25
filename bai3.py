# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:11:11 2024

@author: Student
"""

N = int(input("nhap so nguyen duong N có 2 chu so: "))
if N>=10 and N<=99:
    print("ket qua ", N%10+N//10 )
else:
    print("khong xac dinh ")