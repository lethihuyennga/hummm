# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:58:02 2024

@author: PC
"""

#Viết một hàm nhập vào một danh sách số nguyên từ bàn phím các số nguyên này được
#phân cách bằng khoảng trắng và trả về None nếu danh sách đó trống
def question_10():
    chuoi=input("nhaapj:").strip()
    if not chuoi:
        return None
    danh_sach=list(map(int,chuoi.split()))
    return danh_sach
print(question_10())