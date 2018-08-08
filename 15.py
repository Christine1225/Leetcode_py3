# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 18:37:08 2018
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
@author: Abigail
"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import collections
        
        d = collections.Counter(nums)
        nums_keys = d.keys()
        
        # return list(nums_keys)
        
        pos, neg = [],[]
        
        for p in nums_keys:
            if p >= 0:
                pos.append(p)
            else:
                neg.append(p)
                
        r = []
        
        if d.get(0,0) > 2:
            r.append([0,0,0])
        
        for i in neg:
            for j in pos:
                tar = - i - j
                if tar in nums_keys:
                    if i< tar < j:
                        r.append([i,tar,j])
                    elif (j==tar or i == tar) and d[tar]>1:
                        r.append([i,tar,j])
        return r
ss = Solution()
#L = [-2,0,1,1,2]
#L= [-2,0,0,2,2]
##L = [-1, 0, 1, ]
#print(ss.threeSum(L)) 
#L = [-1, 0, 1, 2, -1, -4]
#L = [0,0,0]
#L = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
#L = [-4,-2,-2,-2,0,4,4,6,6]
L = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
print(ss.threeSum(L))    