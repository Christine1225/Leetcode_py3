# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:17:34 2018
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。
注意：
答案中不可以包含重复的四元组。
示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
@author: Abigail
"""
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        r,lenn =[], len(nums)
        if lenn < 4:
            return []
        nums.sort()
        Max = nums[-1]
        if 4* nums[0] > target or 4*Max < target:
            return []
        for i,z in enumerate( nums):
#            x = nums[i]
            if i > 0 and z == nums[i-1]:
                continue
            if z + 3*Max < target:
                continue
            if 4*z > target:
                break
            if 4*z == target:
                if i+ 3 < lenn and nums[i+3] == z:
                    r.append([z,z,z,z])
                break
            self.threeSum(nums,target-z,i+1,lenn -1,r,z)
        return r
    def threeSum(self,nums,target,low,high,r,z1):
        if low + 1 >= high:
            return
        Max = nums[high]
        if 3*nums[low] > target or 3* Max < target:
            return
        for i in range(low,high-1):
            z = nums[i]
            if i > low and z== nums[i-1]:continue
            if z + 2*Max < target:continue
            if 3*z > target:break
            if 3*z == target:
                if i+1 < high and nums[i+2] == z:
                    r.append([z1,z,z,z])
                break
            self.twoSum(nums,target-z,i+1,high,r,z1,z)
        return   
    def twoSum(self,nums,target,low,high,r,z1=0,z2=0):
            if low >= high or 2*nums[low] > target or 2*nums[high] < target:
                return
            i,j = low,high
            while i < j:
                sum2 = nums[i] + nums[j]
                if sum2 == target:
                    r.append([z1,z2,nums[i],nums[j]])
                    x = nums[i]
                    while i < j and x== nums[i]:i+=1
                    x=nums[j]
                    while i < j and x== nums[j]:j-=1
                elif sum2 < target:
                     i+=1
                else:
                     j-=1
            return 
ss = Solution()
nums = [1, 0, -1, 0, -2, 2]
target= 0  
print(ss.fourSum(nums,target))          
#        import collections
#        
#        d = collections.Counter(nums)
#        nums_keys = d.keys()
#        
#        # return list(nums_keys)
#        
#        r = []
#        
#        if d.get(0,0) > 3:
#            r.append([0,0,0,0])
#        
#        for i in neg:
#            for j in pos:
#                for k in pos:
#                    tar = - i - j - k 
#                    if tar in nums_keys:
#                        if i< tar < j:
#                            r.append([i,tar,j])
#                        elif (j==tar or i == tar) and d[tar]>1:
#                            r.append([i,tar,j])