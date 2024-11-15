# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:28:46 2024

@author: PC
"""

#Viết một hàm để tìm phần tử x trong một danh sách lst . Nếu tìm thấy, trả về vị trí (chỉ số)
#của phần tử đó, nếu không, trả về None
def question_5(lst: list, x: int):
    if x in lst:
        return lst.index(x)
    else: 
        return None
lst = [1, 2, 3, 4, 5]
x = 3
print(question_5(lst, x))