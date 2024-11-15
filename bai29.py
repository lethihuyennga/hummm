# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 02:06:54 2024

@author: PC
"""

def question_29(nums):
    nums.sort()
    n=len(nums)
    if n%2!=0:
        return nums[n//2]
    else:
        mid1=nums[n//2 -1]
        mid2=nums[n//2]
        return (mid1+mid2)/2
nums = [1, 2, 3, 4]
print(question_29(nums))