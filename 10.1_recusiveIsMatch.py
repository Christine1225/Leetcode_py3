# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:25:33 2018
有两种方法， 一种是递归直接匹配，比较好理解，代码简洁。
另一种是DP，时间复杂度小 ，为O(m*n) 其中m是匹配串长度，n是模式串长度。

先说第一种：
　　设S为匹配串，P为模式串，令i指向匹配串Si，令j指向模式串Pj，判断P[j+1]是否为*  如果不是*，判断S[i] == P[j] ?　如果等于，则递归处理S[i+1] P[j+1]，不等于则返回false。如果P[j+1]是*，则需要综合考虑两种情况，一个是*表示前一个字符重复0次，
　　另一种情况是前一个字符重复 >=1次的情况，并对这两种情况取"或"。 看代码很容易理解的
@author: Abigail
"""
class WhySolutionIsWrong(object):
    def IsMatch(self,a,b):
        return a != '' and (a == b or b== '.')
    def isMatch(self,s,p,i = 0,j = 0):
        
        if p[j:] ==''  :
            return s[i:]==''
        
        if   p[j+1] == '*' and len(p[j:]) >= 2:
            return (self.isMatch(s,p, i+1,j) and self.IsMatch(s[i],p[j])) or self.isMatch(s,p, i,j+2)#0 times         
        
        else:
            return self.IsMatch(s[i],p[j]) and self.isMatch(s,p,i+1,j+1 )

    
ss = Solution()
print(ss.isMatch("aab",".*b"))         