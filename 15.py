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
        lens = len(nums)
        if lens < 3:
            return []
        nums = self.quicksort(nums) 
        print(nums)
        i,j = 1,lens-1
        ans = []
        lastTarget = nums[0] + 1
        for start,target in enumerate ( nums[0:lens-2]):
#            if target + nums[j] + nums[j-1] < 0 :
##                print(target,nums[i],i)
#                target = nums[i]
#                
#                i+=1
#                continue
#            elif target + nums[i] + nums[i+1] > 0:
#                target = nums[i]
#                i+= 1
#                continue
            
            if target == lastTarget:
                continue
            i= start +1
            j = lens-1
#            print(target,i,j)
            while i < j:
                if target + nums[i] + nums[j] == 0 :
                    ans.append([target,nums[i],nums[j]])
                    while nums[i] == nums[i+1] :
                        i = i+1
                        if target == -1: print (target,i,j)
                        if i<= j:break
                    i+=1
#                    print("i",i,nums[i])
                    while nums[j] == nums[j-1] and i < j:    
                        j-=1
                        if i<= j:break
                    j-=1
                    print("j",j)
                elif target + nums[i] + nums[j] > 0:    
                    j-=1
                elif target + nums[i] + nums[j] < 0:
                    i+=1
#                print (i,j)
            lastTarget  = target    
        return ans
    def quicksort(self,data) :
        if len(data) < 1:
            return data
        pivot = data[0]
        left = []
        right = []
        for x in range(1, len(data)):
            if data[x] <= pivot:
                left.append(data[x])
            else:
                right.append(data[x])
        left = self.quicksort(left)
        right = self.quicksort(right)
        foo = [pivot]
        return left + foo + right
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