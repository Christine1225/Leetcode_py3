# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 10:23:55 2018
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
@author: Abigail
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        lenh = len(height )
        if lenh < 2:
            return 0
        i,ans,j = 0,0,lenh -1
        
        while i < j:
            
            if height[i] < height[j]:
#                ans = max( height[i] * (j-i) , ans)
                temi = i
                ans = height[i] * (j-i) if height[i] * (j-i) > ans else ans
                i+=1
                while j > i and height[i] < height[temi] :
                    i+=1
            else   :  
#                ans = max( height[j] * (j-i) , ans)
                temj = j
                ans = height[j] * (j-i) if height[j] * (j-i) > ans else ans
                j-=1
                while j > i and height[j] < height[temj] :
                    j-=1
        return ans         
height =  [1,8,6,2,5,4,8,3,7]       
ss=Solution()
print(ss.maxArea(height))        