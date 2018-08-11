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
        closest = []

        # 固定一个数，从该数后面的左右两端向中间查找
        # nums的最后两个要扔掉，因为后面直接用后2个数
        for i,num in enumerate(nums[0:-2]):
            l,r = i+1,len(nums)-1
            # 当左边两个加固定值比target大时，固定值加左边两个为最接近
            if num + nums[l] + nums[l+1] > target:
                closest.append(num + nums[l] + nums[l+1])
            # 当右边两个加固定值比target小时，固定值加右边两个为最接近
            elif num + nums[r] + nums[r-1] < target:
                closest.append(num + nums[r] + nums[r-1])

            else:
                while l < r:
                    closest.append(num + nums[l] + nums[r])
                    # 当加起来后，比target小，左边加1
                    if num + nums[l] + nums[r] < target:
                        l += 1
                    # 当加起来后，比target大，右边减1
                    elif num + nums[l] + nums[r] > target:
                        r -= 1
                    # 正好等于target
                    else:
                        return target

        # 绝对值排序
        closest.sort(key=lambda x:abs(x-target))
        return closest[0]
