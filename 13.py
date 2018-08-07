# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 18:32:27 2018

@author: Abigail
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
        spec = {"C","X","I"}
        lens = len( s )
        i  ,ans = 0, 0
        while i < lens:
            if s[i] in spec  and i+ 1 < lens and s[i:i+2] in dic:
                ans += dic[s[i:i+2]]
                i+=2
            else:
                ans += dic[s[i]]
                i+=1

                
        return ans
ss = Solution()        
print(ss.romanToInt("IV"))
print(ss.romanToInt("X"))
print(ss.romanToInt("XIV"))
print(ss.romanToInt("XIX"))
print(ss.romanToInt("LVIII"))
print(ss.romanToInt("MCMXCIV"))           