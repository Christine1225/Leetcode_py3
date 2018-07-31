# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:01:00 2018
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false i p
@author: Abigail
"""
def isMatch( s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lp,ls = len(p), len(s)
        if lp < 2  and p!="." and p!= "*":
            if p == s:
                return True
            else: return False
        if (ls ==0 and p != "" ) or (lp ==0 and s !=''):return    False 
        i,j=0,0
        while i + 1 < lp and j < ls:
            if p[i:i+2] == ".*":
                return True
            elif p[i] == ".":i,j=i+1,j+1
            elif p[i+1] == "*":
                while s[j] == p[i] :
                    j+=1
#                    print(i,j)
                    if j == ls: 
                       if i+ 2 >= lp: return True
                       else:return False
                           
                i+=2
                if i >= lp : return False
                if p[i] == "." and i+1 == lp and j+1 == ls:return True
                elif p[i] == "." and i+1 == lp: return False
#                if p[i] == "*" and i+1 = lp :return True 
            elif p[i] == s[j]:
                i,j=i+1,j+1 
#                print("i,j",i,j)
            else: return False
        if p[-1] == "*" and( s[-1] == p[-2] or s[-1] == p[-1]  ):return True  
        else: return p[-1] == s[-1]
s,p="aaa","aa"                
print(isMatch( s, p))        
#s,p="mississippi","mis*is*ip*."                
#print(isMatch( s, p))        
#s,p="","abc"                
#print(isMatch( s, p))
#s,p="a",""                
#print(isMatch( s, p))
#s,p="aa","a"                
#print(isMatch( s, p))                
#s,p="aa","a*"                
#print(isMatch( s, p))                   
#s,p="ab",".*"                
#print(isMatch( s, p))                   
#s,p="aab","c*a*b"                
#print(isMatch( s, p))  
#s,p="mississippi","mis*is*ip*"                
#print(isMatch( s, p))                   
