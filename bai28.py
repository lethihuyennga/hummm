# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 02:06:05 2024

@author: PC
"""

from collections import Counter
def question_28(s: str):
    dem=Counter(s)
    return dict(dem)
s = "hello"
print(question_28(s))