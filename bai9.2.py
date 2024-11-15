# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:40:17 2024

@author: PC
"""

def question_9(s: str) -> bool:
    s = ''.join(char for char in s if char.isalnum())
    s = s.lower()
    return s == s[::-1]
print(question_9("A man, a plan, a canal: Panama"))


    