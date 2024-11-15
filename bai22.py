# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:35:15 2024

@author: PC
"""

def question_22(nums: list[int]):
    index = 0

    # Duyệt qua mảng, đưa các phần tử không phải số 0 lên đầu
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1

    # Sau khi các phần tử không phải số 0 đã được di chuyển lên đầu,
    # gán các phần tử còn lại (từ vị trí index trở đi) thành 0
    for i in range(index, len(nums)):
        nums[i] = 0

    return nums
nums=[0,2,9,0,3,2,4,5]
print(question_22(nums))