# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 18:36:39 2018
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
@author: Abigail
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs :
            return ""
        
        shortest = len(strs)
        if shortest == 1 and  strs[0] != "":
            return strs[0]
        shortest = len(strs[0])
        shortest_index = 0
        for index,short in enumerate (strs ):
            shortest_index,shortest =( index,len(short)) if len(short) < shortest else (shortest_index,shortest)
            
        if shortest == 0:
            return ""
        loop = True    
        for index,ic in enumerate (strs[shortest_index]):
            
            for i in strs:
                if i == shortest_index:
                    continue
                if i[index] != ic:
                    loop = False
                    break
            if not loop:
                break
        if  loop:
            return strs[shortest_index]
        return  strs[shortest_index][:index]   
ss = Solution()
#test =["dog","racecar","car"]
#print(ss.longestCommonPrefix(test))            
#test =["flower","flow","flight"]
#print(ss.longestCommonPrefix(test)) 
#test =[""]
#print(ss.longestCommonPrefix(test))
test =["ca","a"]
print(ss.longestCommonPrefix(test))
test =["a"]
print(ss.longestCommonPrefix(test))
test =["aa","aa"]
print(ss.longestCommonPrefix(test))         
test =["a","ab","ac","ad"]
print(ss.longestCommonPrefix(test)) 