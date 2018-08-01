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
def isMatch( text, pattern):
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)
        
#        lp,ls = len(p), len(s)
#        if lp < 2  and p!="." and p!= "*":
#            if p == s:
#                return True
#            else: return False
#        if (ls ==0 and p != "" ) or (lp ==0 and s !=''):return    False 
#        i,j=0,0
#        while i + 1 < lp and j < ls:
#            if p[i:i+2] == ".*":
#                i+=2
#                if i == lp:
#                    return True
#                else:
#                    for jj,c in enumerate(s[j:]):
#                        if c == p[i]:
#                            j=jj
#                           
#            elif p[i] == ".":i,j=i+1,j+1
#            elif p[i+1] == "*":
#                while s[j] == p[i] :
#                    j+=1
##                    print(i,j)
#                    if j == ls: #s is end
#                       if i+ 2 >= lp: return True
#                       elif (p[i+2] == "." or p[i+2] == s[-1]) and i+3 == lp : return True 
#                           
#                       else:            return False                  
#                i+=2
#                if i >= lp : return False
#                if p[i] == "." and i+1 == lp and j+1 == ls:return True
#                elif p[i] == "." and i+1 == lp: return False
##                if p[i] == "*" and i+1 = lp :return True 
#            elif p[i] == s[j]:
#                i,j=i+1,j+1 
##                print("i,j",i,j)
#            else: return False
#        if p[-1] == "*" :
#            for c in s[j:]:
#                if c != p[-2]:
#                    return False
#            return True  
#        elif p[-1] != "*" and s[-1] == p[-1] and j + 1 ==ls   : return True
#        else:return False
#s1,s2,p="aabcb","cb",".*cb"                
#print(isMatch( s1, p),isMatch( s2, p))                  
#s,p="aab","c*a*b"                
#print(isMatch( s, p))
s,p="aaa","ab*a*c*a"                
print(isMatch( s, p))  
#s,p="mississippi","mis*is*ip*"                
#print(isMatch( s, p))                   
#s,p="","abc"                
#print(isMatch( s, p))
#s,p="a",""                
#print(isMatch( s, p))
#s,p="aaa","aa"                
#print(isMatch( s, p))        
#s,p="mississippi","mis*is*ip*."                
#print(isMatch( s, p))        
#s,p="aa","a"                
#print(isMatch( s, p))                
#s,p="aa","a*"                
#print(isMatch( s, p)) 
                  
#s,p="ab",".*"                
#print(isMatch( s, p)) 