# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 11:43:27 2018

@author: Abigail
"""
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
#        closest = []
        goal = nums[0]+nums[1] + nums[2]
        cdistance = abs(goal- target)
        ans = goal
        # 固定一个数，从该数后面的左右两端向中间查找
        # nums的最后两个要扔掉，因为后面直接用后2个数
        for i,num in enumerate(nums[0:-2]):
            l,r = i+1,len(nums)-1
            if num + nums[l] + nums[l+1] > target:
                distance = num + nums[l] + nums[l+1] - target
                if cdistance > distance:
                    ans = num + nums[l] + nums[l+1]
                    cdistance = distance
            # 当右边两个加固定值比target小时，固定值加右边两个为最接近
            elif num + nums[r] + nums[r-1] < target:
                distance = target - (num + nums[r] + nums[r-1])
                if cdistance > distance:
                    ans = num + nums[r] + nums[r-1]
                    cdistance = distance

            else:
                while l < r:
                    goal = num + nums[l] + nums[r] 
                    distance = abs (target - goal)
                    if cdistance > distance:
                        ans = goal
                        cdistance = distance
                    # 当加起来后，比target小，左边加1
                    if goal < target:
                        l += 1
                    # 当加起来后，比target大，右边减1
                    elif goal > target:
                        r -= 1
                    # 正好等于target
                    else:
                        return target
      
        return ans
ss = Solution()
L =[13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6]
target = -59
#L = [0,2,1,-3]
#L = [-3,0,1,2]
#target = 1
#L = [-1, 0, 1, 2, -1, -4]
#L = [0,0,0]
#L = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
#L = [-4,-2,-2,-2,0,4,4,6,6]
#L = [-2,0,3,-1,4,0,3,4,1,1,1,-3,-5,4,0]
print(ss.threeSumClosest(L,target))