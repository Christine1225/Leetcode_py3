# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:20:43 2018
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
@author: Abigail
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        lens = len(s)
        if lens == 1:
            return False
        r,d = [],{"(":")","{":"}","[":"]"}    
        for ch in s:
#            print(r)
            if ch in {"(":")","{":"}","[":"]"}:
                r.append(ch)
            elif r== [] :
                return False
            elif ch != d[r[-1]]:
                return False
            else:
                r.pop()#default -1 position
        return not r        
ss = Solution()
#s = ["()","()[]{}",  "(]" ,"([)]","{[]}"]
s=["){"]
s=["(("]      
print([ss.isValid(y) for y in s])     