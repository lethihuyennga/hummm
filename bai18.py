# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:40:42 2024

@author: PC
"""

#Viết một hàm để loại bỏ tất cả khoảng trắng thừa trong một chuỗi, bao gồm:
#Loại bỏ khoảng trắng ở đầu và cuối chuỗi.
#Loại bỏ các khoảng trắng dư thừa giữa các từ (chỉ giữ lại một khoảng trắng giữa các
#từ)
def question_18(s: str):
    return ' '.join(s.strip().split())
print(question_18(" hmmm toi an gi ta "))