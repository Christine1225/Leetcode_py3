# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:10:36 2018
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:
输入: 123
输出: 321
示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
@author: Abigail
"""
def reverse( x):
        """
        :type x: int
        :rtype: int
        """
        op = -1 if x < 0 else 1
        if x < 0:
            x *= -1
        y=0    
        while x / 10 :
            y=10*y + x%10
            x=x//10
        if op == -1 and y > pow(2,31):
            y= 0
        elif op == 1 and y > pow(2,31) -1: 
            y=0
    
        return y*op    
x=-321
print(reverse(x))        
x=-320
print(reverse(x))        
x=(-1) * (pow(2,31) + 2)
print(reverse(x))        
x=pow(2,31)
print(reverse(x))        
x=1534236469
print(reverse(x)) 