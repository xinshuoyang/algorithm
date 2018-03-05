#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171212
#
################################################################################
import sys

class Solution:
    """
    @param: nums: an integer array
    @param: target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here

        snums = sorted(nums)
        
        res = sys.maxint
        
        for i in range(len(snums)):
            nn = self.findclosest(snums[i+1:], target - snums[i])
            
            if res > nn:
                res = nn

        return res


    def findclosest(self, nums, target):
        """
        find the closet number in nums that is closest to target.
        return the difference
        """
        if len(nums) == 0:
            return sys.maxint

        if target < nums[0]:
            return nums[0] - target

        if target > nums[-1]:
            return target - nums[-1]
        
        first = 0
        last = len(nums) - 1

        while last - first > 1:

            mid = first + (last - first) / 2

            if nums[mid] == target:
                return 0
            elif nums[mid] < target:
                first = mid
            else:
                last = mid

        if abs(nums[first] - target) <= abs(nums[last] - target):
            return abs(nums[first] - target)
        else:
            return abs(nums[last] - target)
        
        
if __name__ == '__main__':
    nums = sorted([0,1,2,0,4])

    s = Solution()
    print s.twoSumClosest(nums, 0)
    
