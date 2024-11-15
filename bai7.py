# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:39:36 2024

@author: PC
"""

#Viết một hàm tạo ra n số thực ngẫu nhiên trong khoảng từ 0 đến 1. Sau đó, tìm số lớn nhất
#và số nhỏ nhất trong danh sách đó
import random
def question_7(n: int):
    n=[random.random() for _ in range( n)]
    ln=round(max(n),4)
    nn=round(min(n),4)
    return ln, nn
print(question_7(2))