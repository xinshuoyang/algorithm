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
    @param nums: An array of integers.
    @return: nothing
    """
    def arrayReplaceWithGreatestFromRight(self, nums):
        if len(nums) == 0:
            return
        nmax = nums[-1]
        nums[-1] = -1

        for i in range(-2, -len(nums)-1, -1):
            temp = nmax
            if nums[i] > nmax:
                nmax = nums[i]
            nums[i] = temp

if __name__ == '__main__':
    ss = Solution()
    nums = [16, 17, 4, 3, 5, 2]
    print nums
    ss.arrayReplaceWithGreatestFromRight(nums)
    print nums
