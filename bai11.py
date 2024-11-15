# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:06:46 2024

@author: PC
"""

#Viết một hàm question_11(n) để trả về số Fibonacci thứ n . Dãy số Fibonacci được định
#nghĩa như sau:
#F(0) = 0
#F(1) = 1
#F(n) = F(n-1) + F(n-2) với n > 1
def question_11(n: int):
    if n<=1 :
        return n
    a,b=0,1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b
print(question_11(5))
    