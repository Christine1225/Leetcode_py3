# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 18:30:58 2018

@author: Abigail
"""

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def _findSubstring(l, r, n, k, t, s, req, ans):
            curr = {}
            while r + k <= n:
                w = s[r:r + k]
                r += k
                if w not in req:
                    l = r
                    curr.clear()
                else:
                    curr[w] = curr[w] + 1 if w in curr else 1
                    while curr[w] > req[w]:
                        curr[s[l:l + k]] -= 1
                        l += k
                    if r - l == t:
                        ans.append(l)

        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words) * k
        req = {}
        for w in words:
            req[w] = req[w] + 1 if w in req else 1
        ans = []
        for i in range(min(k, n - t + 1)):
            _findSubstring(i, i, n, k, t, s, req, ans)
        return ans
ss=Solution()
s,words="lovlovgodmanmanlovgodgod",["god","lov","man"] 
ss.findSubstring(s,words)       