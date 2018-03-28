#!/usr/bin/python

################################################################################
# NAME : solution.py
#
# DESC : 
#
# AUTH : Xinshuo Yang
#
# DATE : 20180327
#
################################################################################

class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        dmin = float(min(nums))
        dmax = float(max(nums))

        while abs(dmax - dmin) > 1.0e-5:
            mid = dmin + (dmax - dmin) / 2.0
            if self.checkAverage(nums, k, mid):
                dmin = mid
            else:
                dmax = mid

        return dmax


    def checkAverage(self, nums, k, target):
        """
        check whether there exist a subarray of length >= k
        such that the average of the subarray > target
        """
        s = 0
        prev = 0
        min_sum = 0

        for i in range(k):
            s += nums[i] - target

        if s > 0:
            return True

        for i in range(k, len(nums)):
            s += nums[i] - target
            prev += nums[i - k] - target
            min_sum = min(min_sum, prev)
            if s - min_sum > 0:
                return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print sol.maxAverage([1, 12, -5, -6, 50, 3], 3)
