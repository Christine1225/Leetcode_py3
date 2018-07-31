# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 09:36:10 2018
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R
之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);
示例 1:

输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"
示例 2:

输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I

very clever algorithm
['1', '', '', '', '', '']
['1', '2', '', '', '', '']
['1', '2', '3', '', '', '']
['1', '2', '3', '4', '', '']
['1', '2', '3', '4', '5', '']
['1', '2', '3', '4', '5', '6']
['1', '2', '3', '4', '57', '6']
['1', '2', '3', '48', '57', '6']
['1', '2', '39', '48', '57', '6']
['1', '2a', '39', '48', '57', '6']
['1b', '2a', '39', '48', '57', '6']
['1b', '2ac', '39', '48', '57', '6']
['1b', '2ac', '39d', '48', '57', '6']
['1b', '2ac', '39d', '48e', '57', '6']
['1b', '2ac', '39d', '48e', '57f', '6']
1b2ac39d48e57f6
@author: Abigail
"""

def convert( s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows == 1:return s
        
        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            if index == 0:step = 1
            elif index == numRows-1:step = -1
            L[index] += x
            index += step
        return ''.join(L)
s="123456789abcdef"         
print(convert(s,6))
                