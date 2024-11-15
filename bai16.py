# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:31:42 2024

@author: PC
"""

#Viết một hàm để tính trung bình cộng, nhận vào số lượng tham số bất kỳ và trả về giá trị
#trung bình cộng của chúng
def question_16(*arg):
    if len(arg)==0:
        return 0
    return sum(arg)/len(arg)
print(question_16(1,4,2,9,0,3))
