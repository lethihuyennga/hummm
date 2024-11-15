# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:02:10 2024

@author: PC
"""

#Bạn được cung cấp một số nguyên dương n . Viết một hàm để xác định xem n có phải là
#số nguyên tố hay không.
#Số nguyên tố là số nguyên dương lớn hơn 1 và chỉ có hai ước số dương là 1 và chính nó.
def question_1(n: int):
    if n<1:
        return False
    if n==2:
        return True
    if n>2:
        for i in range(2,n):
          if  n%i==0:
            return False
        else:
            return True
print(question_1(11))