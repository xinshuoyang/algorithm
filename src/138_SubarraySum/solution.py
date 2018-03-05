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

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here

        for i in range(len(nums)):
            if nums[i] == 0:
                return i, i

        for i in range(len(nums)):
            s = nums[i]
            
            for j in range(i + 1, len(nums)):
                s += nums[j]

                if s == 0:
                    return i, j

if __name__ == '__main__':

    nums = [-3,1,2,-3,4]

    s = Solution()
    print s.subarraySum(nums)
