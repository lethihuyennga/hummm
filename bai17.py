# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:36:31 2024

@author: PC
"""

#Viết một hàm để tạo ra một danh sách gồm n số nguyên ngẫu nhiên từ 1 đến 100. Sau đó,
#sắp xếp danh sách theo thứ tự giảm dần.
import random
def question_17(n: int):
    m=[random.randint(1,100) for _ in range(n)]
    m.sort(reverse=True)
    return m
print(question_17(6))
    