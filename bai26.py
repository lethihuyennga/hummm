# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 01:38:34 2024

@author: PC
"""

def question_26(s: str):
    dem = {}
    for ki_tu in s:
        dem[ki_tu] = dem.get(ki_tu, 0) + 1
    do_dai = 0
    for count in dem.values():
        do_dai += (count // 2) * 2 
    if any(count % 2 == 1 for count in dem.values()):
        do_dai += 1
    return do_dai

s = "abccccdd"
print( question_26(s))
