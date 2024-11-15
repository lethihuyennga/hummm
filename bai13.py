# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:17:12 2024

@author: PC
"""

#Viết một hàm để đếm số từ trong một chuỗi. Một từ được định nghĩa là một chuỗi các ký tự
#không phải khoảng trắng.
def question_13(s: str):
    tu=s.split()
    return len(tu)
print(question_13("chos thanh"))