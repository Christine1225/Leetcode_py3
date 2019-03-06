# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:54:40 2018
给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
示例 1:
输入:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出: [0,9]
解释: 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2:
输入:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
输出: []
@author: Abigail
"""
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        if not s or not words:
            return []
        
        word_map = Counter(words)
#        print(word_map)
        results = []
        word_size = len(words[0])
        num_word = len(words)
        list_size = word_size*num_word
        for i in range(len(s) - list_size + 1):
            seen = dict(word_map)
            word_used = 0
            for j in range(i, i + list_size, word_size):
                sub_str = s[j: j + word_size]
                print(i,j)
                if sub_str in seen and seen[sub_str] > 0:
                    seen[sub_str] -= 1
                    word_used += 1
                else:
                    break
            if word_used == num_word:
                results.append(i)
        return results
ss=Solution()
s,words="lovlovgodmanmanlovgodgod",["god","lov","man"]
print(ss.findSubstring(s,words))
        