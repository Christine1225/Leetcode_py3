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
@author: Abigail
"""

def convert( s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ns=''
        if numRows == 1:return s
        stride = 2*(numRows - 1)
        
        for i in range((numRows)):
            k=0
            while k*stride + i < len(s):
                ns+=s[k*stride+i]
                if i !=0 and i != numRows -1 and (k+1)*stride -i <  len(s):
                    ns+=s[(k+1)*stride -i]
                k+=1
        return ns
s="123456789abcdef"         
print(convert(s,6))
                