# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:52:58 2024

@author: PC
"""

def question_23(nums: list[int]):
    socotontairoi=set()
    for num in nums:
        if num in socotontairoi:
            return True
        socotontairoi.add(num)#chức năng dòng này trả số lại từ set vào lại nums nếu dò hết mà vẫn không có thì nums vẫn giữ nguyên.
    return False
        
nums = [1, 2, 3, 5, 2]
print( question_23(nums))