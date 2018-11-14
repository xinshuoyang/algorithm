#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20181114
#
################################################################################
class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        if len(nums) <= 1:
            return False
        
        snums = sorted(nums)
        for i in range(len(nums)-1):
            if snums[i] == snums[i+1]:
                return True

        return False
