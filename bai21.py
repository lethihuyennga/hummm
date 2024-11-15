# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:46:22 2024

@author: PC
"""

def question_21(nums: list[int], target: int):
    for num in nums:
        soconlai=target-num
        if soconlai in nums:
            return(num,soconlai)
    return None
nums=[2,7,11,21]
target=18
print(question_21(nums, target))