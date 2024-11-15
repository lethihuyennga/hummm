# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:21:48 2024

@author: PC
"""

#Viết một hàm để kiểm tra xem một chuỗi có phải là chữ số hay không. Chuỗi được coi là
#chữ số nếu tất cả các ký tự trong chuỗi là số và không có ký tự nào khác.
def question_14(s: str):
    if s.isdigit():
        return True
    else: 
        return False
print(question_14("abcd12"))