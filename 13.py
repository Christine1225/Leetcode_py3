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
        lens = len( s )
        i  ,ans = 0, 0
        while i < lens:
            if s[i] == "C":
                if i + 1 < lens and (s[i+1] == "M" or s[i+1] == "D"):
                    ans+= dic[s[i:i+2]]
                    i+=2
                else:
                    ans+=100
                    i+=1
            elif s[i] == "X":
                 if i + 1 < lens and (s[i+1] == "C" or s[i+1] == "L"):
                     ans+= dic[s[i:i+2]]
                     i+=2
                 else:
                     ans+=10
                     i+=1
#                     print(ans,i)
            elif s[i] == "I":
                 if i + 1 < lens and (s[i+1] == "X" or s[i+1] == "V"):
                     ans+= dic[s[i:i+2]]
                     i+=2
#                     print(ans,i)
                 else:
                     ans+=1
                     i+=1  
            elif i < lens:         
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