# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:37:17 2018
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
n=1 ()
n=2 ()(),(())
例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
@author: Abigail
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        else:
            r = set()
            for p in self.generateParenthesis(n-1):
                for i,c in enumerate(p):
                    if c != '(':continue
                    r.add(p[:i+1] + "()"+p[i+1:])
                r.add("()"+p)
            return list(r)
ss = Solution()
print(ss.generateParenthesis(3))