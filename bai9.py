# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:34:05 2024

@author: PC
"""

#Viết một hàm để kiểm tra xem một chuỗi có phải là chuỗi palindrome hay không. Một chuỗi được gọi là palindrome nếu, sau 
#khi chuyển tất cả các chữ cái viết hoa thành chữ thường và loại bỏ tất cả các ký tự không phải chữ cái và số, nó đọc giống nhau từ trái sang phải vàtừ phải sang trái.
def question_9(chuoi:str ):
    chuoibodau = [char.lower() for char in chuoi if char.isalnum()]
#char.lower là viết thường kí tự 
#dòng 12 nó sẽ kiểu viết thường kí tự đó nếu trong cái chuỗi là chữ hoặc 
    return chuoibodau == chuoibodau[::-1]
#dòng 15 là so sánh sau khi bỏ hết dấu thì viết xuôi viét ngược có giống nhau hong á
     
s = "A man, a plan, a canal: Panama"
print(s, question_9(s))