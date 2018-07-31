# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:09:53 2018
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
@author: Abigail
"""

def isPalindrome( x):
        """
        :type x: int
        :rtype: bool
        """
        if x ==0 : return True
        if x < 0: return False   
        y = x 
        yy = y
        z = 0
        while y / 10 :
            z = 10*z + y%10
            y = y//10
      
        if  yy == z:
            return True
        else: return False    
print( isPalindrome( -1021201 ) )        