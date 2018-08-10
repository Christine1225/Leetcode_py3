# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:15:17 2018
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
@author: Abigail
"""

class Solution:
    def rpn(self, lists,n):
        ans = []
        for i in lists:
            for j in range(n):
                ans.append(i)
        return ans        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = []
        if len(digits) < 1:
            return []
        if len(digits) == 1:
            return list(dic[digits])
        lenn = 1 
        ans = list(dic[digits[0]])
        last_lenn = len(dic[digits[0]])
        for num in digits[1:]:
            lenn = len(dic[num])
            ans = self.rpn(ans,lenn)
            index = 0
#            print(ans)
            for i in range(last_lenn):
                for ch in dic[num]:
                    ans[index] += ch
                    index+=1
            last_lenn *= lenn        

        return ans
ss = Solution()
L = ""
L = "237"
print(ss.letterCombinations(L))                   