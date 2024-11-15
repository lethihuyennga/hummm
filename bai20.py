# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:49:42 2024

@author: PC
"""

#Viết một hàm yêu cầu người dùng nhập một giá trị từ bàn phím. Nếu người dùng không
#nhập bất kỳ giá trị nào từ bàn phím (chỉ nhấn Enter), hàm sẽ trả về None .
def question_20():
    n=str(input("nhap:"))
    if n=="":
        return None
    return n
print(question_20())