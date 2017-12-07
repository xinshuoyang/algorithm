#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20171206
#
################################################################################
import sys

class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        
        min_ending_here = sys.maxint

        min_so_far = sys.maxint

        for nn in nums:
            if min_ending_here > 0:
                min_ending_here = nn
            else:
                min_ending_here += nn

            min_so_far = min(min_ending_here, min_so_far)

        return min_so_far

if __name__ == '__main__':
    nums = [-19,1,1,1,1,1,1,1,-2,1,1,1,1,1,1,1,1,-2,1,-15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    s = Solution()
    print  s.minSubArray(nums)
