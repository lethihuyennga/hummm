# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 19:31:59 2024

@author: PC
"""

def question_25(nums: list[int]):
    # Tính bình phương của mỗi phần tử và lưu vào mảng mới
    binh_phuong = [num ** 2 for num in nums]
    # Sắp xếp lại mảng bình phương theo thứ tự không giảm
    binh_phuong.sort()
    return binh_phuong
nums = [-7, -3, 2, 3, 11]
print(question_25(nums))