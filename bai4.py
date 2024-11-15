# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:25:29 2024

@author: PC
"""

#Viết một hàm để kiểm tra xem một số nguyên được nhập vào có phải là số chẵn hay không.
#Trả về True nếu số đó là số chẵn, và False nếu là số lẻ.
def question_4(n: int):
    if n%2==0:
        return True
    elif n%2!=0:
        return False
print(question_4(2))