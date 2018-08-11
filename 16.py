# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:11:56 2018
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
@author: Abigail
"""
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
#        import collections
        lenn = len(nums)
        if lenn < 3:
            return 
        if lenn == 3:
            return sum(nums)
             
        i,j,k=0,1,2
        ans = 0
        nums.sort()
        goal = nums[i]+nums[j] + nums[k]
        cdistance = abs( goal - target) 
        while i < lenn -2 :
            j = i + 1
            k = lenn-1
          
            while j < k:
                ans = nums[i]+nums[j] + nums[k]
#                print(ans,i,j,k)
                distance = abs(ans - target)
                if distance == 0:
                    return ans
                elif cdistance > distance:
                    cdistance = distance
                    goal = ans
                if ans > target:
                    k-=1
                else:j+=1    
            i+=1    
        return goal
ss = Solution()
#L = [-2,0,1,1,2]
#L= [-2,0,0,2,2]
##L = [-1, 0, 1, ]
L = [-1,2,1,-4]
L = [-3,-2,-5,3,-4] 
target = -1
L = [1,2,4,8,16,32,64,128]
target = 82
L =[13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6]
target = -59
#L = [-1, 0, 1, 2, -1, -4]
#L = [0,0,0]
#L = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
#L = [-4,-2,-2,-2,0,4,4,6,6]
#L = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
print(ss.threeSumClosest(L,target))            