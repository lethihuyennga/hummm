# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:11:54 2024

@author: PC
"""
import random
def question_12():
    n=random.randint(1,1000)
    if n<2:
        return n,False
    elif n>=2:
        for i in range(2,n):
            n%i==0
            return n,False
        return n,True
print(question_12())