# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 02:00:36 2024

@author: PC
"""

def question_27(strs: list[str]):
    if not strs:
        return None
    tiento=strs[0]
    for s in strs[1:]:
        while not s.startswith(tiento):
            tiento=tiento[:-1]
            if not tiento:
                return ""
    return tiento
#strs = ["flower", "flow", "flight"]
#print(strs[1:])
#print(strs[:-1])
#print(question_27(strs))
