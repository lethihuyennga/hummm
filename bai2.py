# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:11:02 2024

@author: PC
"""

#Viết một hàm tạo ra n số nguyên ngẫu nhiên từ 1 đến 100. Sau đó, tính tổng và trung bình
#ủa các số này
import random
def question_2(n: int):
    m=[random.randint(1,100) for _ in range(n)]
    tong=sum(m)
    tb=tong/n
    return tong,tb
print(question_2(8))