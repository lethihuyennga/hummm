# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:15:30 2024

@author: PC
"""

#Viết một hàm nhận vào một chuỗi, sau đó đếm và in ra số lượng ký tự viết hoa và ký tự viết
#thường trong chuỗi đó.
def question_3(s: str):
    hoa=0
    thuong=0
    for i in s:
        if i.isupper():
            hoa+=1
        if i.islower():
            thuong+=1
    return hoa,thuong
print(question_3("Hello World"))