# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:03:28 2024

@author: Student
"""

dia_chi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings_1 = dia_chi.split(", ")
sub_strings_2 = []
for sub in sub_strings_1:
    if "P." in sub:
        sub_strings_2.append(sub[2:])
    elif "Q." in sub:
        sub_strings_2.append(sub[2:])
    elif "Tp." in sub:
        sub_strings_2.append(sub[3:])
    else:
        sub_strings_2.append(sub)
print("Kết quả 1:")
for sub in sub_strings_1:
    print(sub)

print("\nKết quả 2:")
for sub in sub_strings_2:
    print(sub)
