#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180402
#
################################################################################
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here

        if len(nums) == 0:
            return
        
        p1 = 0
        p2 = 1
        
        while p2 != len(nums):
            if nums[p1] == nums[p2]:
                p2 += 1
            else:
                nums[p1 + 1] = nums[p2]
                p1 += 1
                p2 += 1
        return p1 + 1        
        
