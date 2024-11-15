# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 02:00:50 2024

@author: PC
"""

from collections import Counter
def question_28(s: str):
    dem=Counter(s)
    return dict(dem)
#s = "hello"
#print(question_28(s))


def question_29(nums):
    nums.sort()
    n=len(nums)
    if n%2!=0:
        return nums[n//2]
    else:
        mid1=nums[n//2 -1]
        mid2=nums[n//2]
        return (mid1+mid2)/2
#nums = [1, 2, 3, 4]
#print(question_29(nums))



def question_31(paragraph: str, n: int):
    tu=paragraph.split()
    dem_tu={}
    for word in tu:
        if word in dem_tu:
            dem_tu[word]+= 1
        else:
            dem_tu[word]=1
    tong_tu=len(tu)
    kq=[]
    for word,count in dem_tu.items():
        if (count/tong_tu)>0.2:
             kq.append(word)
    return kq[:n]
#paragraph = "apple apple banana orange orange apple"
#n = 2
#print(question_31(paragraph,n))

def question_32(nums):
    dsle=[]
    dschan=[]
    for num in nums:
        if num%2==0:
            dschan.append(num)
        else:
            dsle.append(num)
    dschan.sort(reverse=True)
    dsle.sort(reverse=False)
    return dschan, dsle
#nums = [4, 1, 3, 2, 7, 8, 5]
#print(question_32(nums))

def question_33(nums):
    dsmoi=list(set(nums))
    dsmoi.sort()
    if len(dsmoi)<2:
        solonthu2=None
    else:
         solonthu2=dsmoi[-2]
    if len(dsmoi)<5:
        so_nho_thu5=None
    else:
        so_nho_thu5=dsmoi[3]    
    return solonthu2 , so_nho_thu5
#nums = [3, 1, 4, 5, 9, 2, 6, 8, 7]
#print(question_33(nums))


def question_34(s: str) -> int:
    start = 0  # Điểm bắt đầu của cửa sổ
    max_length = 0  # Độ dài lớn nhất
    window = set()  # Tập ký tự trong cửa sổ

    # Lặp qua từng ký tự
    for end in range(len(s)):
        # Nếu ký tự hiện tại đã có trong cửa sổ
        while s[end] in window:
            # Loại bỏ ký tự ở đầu cửa sổ
            window.remove(s[start])
            # Dịch cửa sổ sang phải
            start += 1

        # Thêm ký tự mới vào cửa sổ
        window.add(s[end])
        # Cập nhật độ dài lớn nhất
        max_length = max(max_length, end - start + 1)
    #Trả về kết quả
    return max_length

#s = "pwwkew"
#print(question_34(s))

def question_35_m(chuoi):
    chuoi_con_dai_nhat = ""
    n = len(chuoi)
    for i in range(1, n // 2 + 1):
        chuoi_con_da_gap = set()
        for m in range(n - i + 1):
            chuoi_con = chuoi[m:m + i]
            if chuoi_con in chuoi_con_da_gap:
                if len(chuoi_con) > len(chuoi_con_dai_nhat):
                    chuoi_con_dai_nhat = chuoi_con
            else:
                chuoi_con_da_gap.add(chuoi_con)
    return chuoi_con_dai_nhat
#chuoi = "aabcdeaabcd"
#ketqua = question_35_m(chuoi)
#print("Chuỗi con lặp lại dài nhất là:", ketqua)


from itertools import permutations
def question_36(nums):
    return [list(p) for p in permutations(nums)]
#học hàm nếu nhớ
#nums=[1,2,3]
#print(question_36(nums))

def question_37(chuoi: str):
    chuoi_kt = []
    cap = {')': '(', '}': '{', ']': '['}
    for char in chuoi:
        if char in cap:
           if not chuoi_kt:
               return False
           kt_dau = chuoi_kt[-1]
           if cap[char] != kt_dau:
               return False
           chuoi_kt = chuoi_kt[:-1]
        else:
           chuoi_kt.append(char)
    return not chuoi_kt
#chuoi = inp)ut("Nhập vào chuỗi kí tự: ")
#s = "([()])"
#q="()()[]"
#print(s[-1])
#print(question_37(s))
#print(question_37(q))

import random 
def question_38_m(n):
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b
#print(question_38_m(5))
#print(question_38_m(2))
#print(question_38_m(3))

def question_39_m(prices):
    if not prices:
       return 0
    min_price = prices[0]
    max_profit = 0  
    for price in prices:
       min_price = min(min_price, price)  # Cập nhật giá mua thấp nhất
       profit = price - min_price         # Tính lợi nhuận khi bán vào ngày hiện tại
       max_profit = max(max_profit, profit)  # Cập nhật lợi nhuận tối đa

    return max_profit
#prices = [6, 7, 8, 9, 20, 5]
#gia=[7, 1, 5, 3, 6, 4]
#loinhuan=[7, 6, 4, 3, 1]
#print(question_39_m(prices))
#print(question_39_m(gia))
#print(question_39_m(loinhuan))



