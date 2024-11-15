# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 02:07:21 2024

@author: PC
"""

from collections import Counter
def question_30(paragraph):
    ' '.join(paragraph for tu in paragraph if tu.isalnum())
    tu=paragraph.split()
    dem=Counter(tu)
    return dict(dem)
paragraph = "Hello! I love u so much"
print(question_30(paragraph))