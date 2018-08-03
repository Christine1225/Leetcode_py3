# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:21:43 2018

@author: Abigail
"""

#def match(text, pattern):
#    if not pattern: return not text
#    first_match = bool(text) and pattern[0] in {text[0], '.'}
#    return first_match and match(text[1:], pattern[1:])
#print(match("abc","a.a")) 

class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
            
ss = Solution()
print(ss.isMatch("aab",".*b"))  